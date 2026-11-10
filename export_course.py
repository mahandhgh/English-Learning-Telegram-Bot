"""Export the original curriculum as a standalone SQLite catalog and coverage map."""

from collections import Counter
from contextlib import closing
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sqlite3

from curriculum import LESSONS, LEVELS
from roadmap import SOURCES, TRACKS


def export(root):
    root = Path(root)
    root.mkdir(parents=True, exist_ok=True)
    database = root / "curriculum.sqlite3"
    payload = json.dumps(LESSONS, ensure_ascii=False, sort_keys=True)
    revision = hashlib.sha256(payload.encode("utf-8")).hexdigest()
    with closing(sqlite3.connect(database)) as db:
        db.execute("PRAGMA foreign_keys=ON")
        db.executescript('''
            CREATE TABLE IF NOT EXISTS metadata(key TEXT PRIMARY KEY,value TEXT NOT NULL);
            CREATE TABLE IF NOT EXISTS lessons(
                id TEXT PRIMARY KEY, track TEXT NOT NULL, position INTEGER NOT NULL,
                cefr TEXT NOT NULL, domain TEXT NOT NULL, title TEXT NOT NULL,
                objective TEXT NOT NULL, teaching TEXT NOT NULL, remedial TEXT NOT NULL,
                tasks_json TEXT NOT NULL, references_json TEXT NOT NULL,
                assessment_scope TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS questions(
                lesson_id TEXT NOT NULL REFERENCES lessons(id), bank_index INTEGER NOT NULL,
                role TEXT NOT NULL, prompt TEXT NOT NULL, options_json TEXT NOT NULL,
                correct_index INTEGER NOT NULL, explanation TEXT NOT NULL,
                PRIMARY KEY(lesson_id,bank_index)
            );
            CREATE TABLE IF NOT EXISTS reference_sources(title TEXT PRIMARY KEY,url TEXT NOT NULL);
        ''')
        with db:
            db.execute("DELETE FROM questions")
            db.execute("DELETE FROM lessons")
            db.execute("DELETE FROM reference_sources")
            db.executemany("INSERT INTO reference_sources VALUES (?,?)", SOURCES)
            metadata = {
                "revision": revision, "exported_utc": datetime.now(timezone.utc).isoformat(),
                "scope": "Original five-track course; CEFR bands are editorial targets, not validated certification.",
                "limitations": "No embedded audio/video, automatic speech/free-writing assessment or independent teacher validation. Not exhaustive English coverage.",
            }
            db.executemany("INSERT OR REPLACE INTO metadata VALUES (?,?)", metadata.items())
            for level, items in LESSONS.items():
                for position, item in enumerate(items, 1):
                    db.execute("INSERT INTO lessons VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", (
                        item["id"], level, position, item["cefr"], item["domain"], item["title"],
                        item["objective"], item["text"], item["remedial"],
                        json.dumps(item["tasks"], ensure_ascii=False), json.dumps(item["references"]), item["assessment"],
                    ))
                    for i, question in enumerate(item["questions"]):
                        db.execute("INSERT INTO questions VALUES (?,?,?,?,?,?,?)", (
                            item["id"], i, "practice" if i < 5 else "checkpoint", question["prompt"],
                            json.dumps(question["options"], ensure_ascii=False), question["correct"], question["explanation"],
                        ))
        if db.execute("PRAGMA integrity_check").fetchone()[0] != "ok" or db.execute("PRAGMA foreign_key_check").fetchall():
            raise RuntimeError("Export integrity check failed")
    report = ["# Curriculum inventory and coverage", "",
              f"Content revision: `{revision}`", "",
              f"{sum(map(len, LESSONS.values()))} lessons; {sum(len(x['questions']) for items in LESSONS.values() for x in items)} distinct questions.", "",
              "Each lesson has teaching, a repair explanation, seven explained questions and writing/speaking tasks.", "",
              "CEFR labels are editorial learning targets. Topic presence is not proof of full CEFR coverage or learner mastery.", "",
              "## Assessment boundaries", "",
              "- Automatically marked: selected-response reading and language-use questions.",
              "- Self/partner/teacher reviewed: writing, spoken responses and practical tasks.",
              "- External resources: authentic listening/video and longer reading.",
              "- Not implemented: embedded audio/video, automatic speech/free-writing assessment, full-length standardised tests and delayed spaced review.",
              "- Not independently validated: content difficulty, distractor quality, CEFR placement and learning effectiveness.", ""]
    for level, items in LESSONS.items():
        report.extend([f"## {LEVELS[level]}", "", TRACKS[level]["target"], "",
                       f"{len(items)} lessons / {sum(len(x['questions']) for x in items)} questions", "",
                       "| Order | ID | Target band | Domain | Unit and objective |", "| --- | --- | --- | --- | --- |"])
        for i, item in enumerate(items, 1):
            report.append(f'| {i} | {item["id"]} | {item["cefr"]} | {item["domain"]} | {item["title"]}: {item["objective"]} |')
        report.extend(["", f'Further development: {TRACKS[level]["next_topics"]}', ""])
    report.extend(["## Source references", ""] + [f"- [{title}]({url})" for title, url in SOURCES])
    report.extend(["", "## Count by target band", ""])
    report.extend(f"- {band}: {count} lessons" for band, count in Counter(x["cefr"] for items in LESSONS.values() for x in items).items())
    report_path = root / "CURRICULUM_COVERAGE.md"
    report_path.write_text("\n".join(report) + "\n", encoding="utf-8")
    return database, report_path


if __name__ == "__main__":
    for path in export(Path(__file__).resolve().parent / "output"):
        print(path)
