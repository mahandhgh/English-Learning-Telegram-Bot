"""SQLite persistence for profiles, lessons, quiz sessions and results."""

import secrets
import json
import sqlite3
from contextlib import contextmanager
from pathlib import Path


class Store:
    def __init__(self, path):
        self.path = str(path)
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        with self.connect() as db:
            db.executescript('''
                CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY, level TEXT NOT NULL,
                    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
                );
                CREATE TABLE IF NOT EXISTS level_history (
                    id INTEGER PRIMARY KEY, user_id INTEGER NOT NULL,
                    level TEXT NOT NULL, changed_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
                );
                CREATE TABLE IF NOT EXISTS studied (
                    user_id INTEGER NOT NULL, lesson_id TEXT NOT NULL,
                    PRIMARY KEY (user_id, lesson_id)
                );
                CREATE TABLE IF NOT EXISTS attempts (
                    id INTEGER PRIMARY KEY, user_id INTEGER NOT NULL,
                    level TEXT NOT NULL, lesson_id TEXT NOT NULL,
                    score INTEGER NOT NULL, total INTEGER NOT NULL,
                    finished_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
                );
                CREATE TABLE IF NOT EXISTS sessions (
                    user_id INTEGER PRIMARY KEY, token TEXT NOT NULL,
                    lesson_id TEXT NOT NULL, chat_id INTEGER NOT NULL,
                    question_index INTEGER NOT NULL DEFAULT 0,
                    score INTEGER NOT NULL DEFAULT 0
                );
                CREATE TABLE IF NOT EXISTS answers (
                    id INTEGER PRIMARY KEY, user_id INTEGER NOT NULL,
                    session_token TEXT NOT NULL, lesson_id TEXT NOT NULL,
                    question_index INTEGER NOT NULL, choice INTEGER NOT NULL,
                    correct INTEGER NOT NULL,
                    answered_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    UNIQUE (session_token, question_index)
                );
                CREATE INDEX IF NOT EXISTS attempts_user ON attempts(user_id, level);
                CREATE TABLE IF NOT EXISTS remedial_reads (
                    user_id INTEGER NOT NULL, lesson_id TEXT NOT NULL,
                    error_marker INTEGER NOT NULL, PRIMARY KEY(user_id, lesson_id)
                );
                CREATE TABLE IF NOT EXISTS completions (
                    user_id INTEGER NOT NULL, level TEXT NOT NULL,
                    finished_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    PRIMARY KEY(user_id, level)
                );
                CREATE TABLE IF NOT EXISTS lesson_catalog (
                    lesson_id TEXT PRIMARY KEY, level TEXT NOT NULL, content_json TEXT NOT NULL
                );
            ''')
            # Additive migration preserves old attempts and unfinished three-question quizzes.
            for table, column, definition in (
                ("sessions", "plan", "TEXT"),
                ("sessions", "kind", "TEXT NOT NULL DEFAULT 'lesson'"),
                ("attempts", "kind", "TEXT NOT NULL DEFAULT 'lesson'"),
                ("attempts", "passed", "INTEGER"),
                ("attempts", "coverage", "TEXT"),
                ("answers", "bank_index", "INTEGER"),
            ):
                columns = {row["name"] for row in db.execute(f"PRAGMA table_info({table})")}
                if column not in columns:
                    db.execute(f"ALTER TABLE {table} ADD COLUMN {column} {definition}")
            db.execute("UPDATE answers SET bank_index=question_index WHERE bank_index IS NULL")
            db.execute("CREATE INDEX IF NOT EXISTS answers_user ON answers(user_id, lesson_id, bank_index)")

    @contextmanager
    def connect(self):
        db = sqlite3.connect(self.path, timeout=10)
        db.row_factory = sqlite3.Row
        try:
            with db:
                yield db
        finally:
            db.close()

    def user(self, user_id):
        with self.connect() as db:
            return db.execute("SELECT * FROM users WHERE user_id=?", (user_id,)).fetchone()

    def set_level(self, user_id, level):
        with self.connect() as db:
            db.execute("INSERT INTO users(user_id,level) VALUES (?,?) ON CONFLICT(user_id) DO UPDATE SET level=excluded.level", (user_id, level))
            db.execute("INSERT INTO level_history(user_id,level) VALUES (?,?)", (user_id, level))
            db.execute("DELETE FROM sessions WHERE user_id=?", (user_id,))

    def studied(self, user_id, lesson_id):
        with self.connect() as db:
            db.execute("INSERT OR IGNORE INTO studied VALUES (?,?)", (user_id, lesson_id))

    def was_studied(self, user_id, lesson_id):
        with self.connect() as db:
            return bool(db.execute("SELECT 1 FROM studied WHERE user_id=? AND lesson_id=?", (user_id, lesson_id)).fetchone())

    def session(self, user_id):
        with self.connect() as db:
            return db.execute("SELECT * FROM sessions WHERE user_id=?", (user_id,)).fetchone()

    def begin(self, user_id, lesson_id, chat_id, plan=None, kind="lesson"):
        with self.connect() as db:
            db.execute("INSERT OR REPLACE INTO sessions(user_id, token, lesson_id, chat_id, plan, kind) VALUES (?,?,?,?,?,?)", (user_id, secrets.token_hex(8), lesson_id, chat_id, json.dumps(plan) if plan else None, kind))
        return self.session(user_id)

    def submit(self, user_id, chat_id, token, index, choice, lesson=None):
        from curriculum import BY_ID
        from roadmap import is_pass
        # Serialize read/check/write so duplicate clicks cannot score twice.
        with self.connect() as db:
            db.execute("BEGIN IMMEDIATE")
            session = db.execute("SELECT * FROM sessions WHERE user_id=?", (user_id,)).fetchone()
            if not session or (session["token"], session["question_index"], session["chat_id"]) != (token, index, chat_id):
                return None
            plan = json.loads(session["plan"]) if session["plan"] else [[session["lesson_id"], i] for i in range(3)]
            if not 0 <= index < len(plan):
                return None
            lesson_id, bank_index = plan[index][:2]
            question = BY_ID[lesson_id]["questions"][bank_index]
            if not 0 <= choice < len(question["options"]):
                return None
            correct = choice == question["correct"]
            score = session["score"] + int(correct)
            db.execute("INSERT INTO answers(user_id,session_token,lesson_id,question_index,choice,correct,bank_index) VALUES (?,?,?,?,?,?,?)", (user_id, token, lesson_id, index, choice, int(correct), bank_index))
            finished = index + 1 == len(plan)
            passed = is_pass(score, len(plan))
            if finished:
                level = db.execute("SELECT level FROM users WHERE user_id=?", (user_id,)).fetchone()["level"]
                coverage = json.dumps(sorted({entry[0] for entry in plan}))
                db.execute("INSERT INTO attempts(user_id,level,lesson_id,score,total,kind,passed,coverage) VALUES (?,?,?,?,?,?,?,?)", (user_id, level, session["lesson_id"], score, len(plan), session["kind"], int(passed), coverage))
                db.execute("DELETE FROM sessions WHERE user_id=?", (user_id,))
            else:
                db.execute("UPDATE sessions SET question_index=question_index+1,score=? WHERE user_id=?", (score, user_id))
            return dict(correct=correct, score=score, finished=finished, passed=passed,
                        total=len(plan), lesson_id=lesson_id, bank_index=bank_index, kind=session["kind"])

    def seed_catalog(self, lessons):
        with self.connect() as db:
            for level, items in lessons.items():
                for item in items:
                    db.execute("INSERT INTO lesson_catalog VALUES (?,?,?) ON CONFLICT(lesson_id) DO UPDATE SET level=excluded.level,content_json=excluded.content_json", (item["id"], level, json.dumps(item, ensure_ascii=False)))

    def question_history(self, user_id, lesson_id):
        with self.connect() as db:
            return db.execute("SELECT * FROM answers WHERE user_id=? AND lesson_id=? ORDER BY id", (user_id, lesson_id)).fetchall()

    def mistakes(self, user_id, lesson_id):
        latest = {}
        for answer in self.question_history(user_id, lesson_id):
            latest[answer["bank_index"]] = answer
        return [answer for answer in latest.values() if not answer["correct"]]

    def error_marker(self, user_id, lesson_id):
        errors = self.mistakes(user_id, lesson_id)
        return max((answer["id"] for answer in errors), default=0)

    def read_remedial(self, user_id, lesson_id):
        marker = self.error_marker(user_id, lesson_id)
        with self.connect() as db:
            db.execute("INSERT OR REPLACE INTO remedial_reads VALUES (?,?,?)", (user_id, lesson_id, marker))

    def needs_remedial(self, user_id, lesson_id):
        marker = self.error_marker(user_id, lesson_id)
        with self.connect() as db:
            row = db.execute("SELECT error_marker FROM remedial_reads WHERE user_id=? AND lesson_id=?", (user_id, lesson_id)).fetchone()
        return marker > 0 and (not row or row["error_marker"] < marker)

    def record_completion(self, user_id, level):
        with self.connect() as db:
            db.execute("INSERT OR IGNORE INTO completions(user_id,level) VALUES (?,?)", (user_id, level))

    def attempts(self, user_id, level=None):
        with self.connect() as db:
            if level is None:
                return db.execute("SELECT * FROM attempts WHERE user_id=? ORDER BY id", (user_id,)).fetchall()
            return db.execute("SELECT * FROM attempts WHERE user_id=? AND level=? ORDER BY id", (user_id, level)).fetchall()

    def delete_user(self, user_id):
        with self.connect() as db:
            for table in ("answers", "sessions", "attempts", "studied", "level_history", "remedial_reads", "completions", "users"):
                db.execute(f"DELETE FROM {table} WHERE user_id=?", (user_id,))
