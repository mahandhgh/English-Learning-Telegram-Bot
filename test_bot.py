"""Offline regression checks; no real token or Telegram connection required."""

import tempfile
import sqlite3
from contextlib import closing
import unittest
from pathlib import Path
from types import SimpleNamespace as NS
from unittest.mock import AsyncMock

import bot
from curriculum import BY_ID, LESSONS, LEVELS
from storage import Store
from learning import checkpoint_plan, mastered, practice_plan, session_plan, weak_lessons


class LearningTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        temp_root = Path(__file__).parent / ".setup-temp"
        temp_root.mkdir(exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(dir=temp_root)
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / "test.sqlite3"
        self.db = Store(self.path)
        self.context = NS(bot_data={"store": self.db}, args=[])

    def update(self, data=None, user_id=100, chat_type="private"):
        message = NS(reply_text=AsyncMock())
        query = NS(data=data, answer=AsyncMock(), edit_message_text=AsyncMock()) if data else None
        return NS(effective_user=NS(id=user_id), effective_chat=NS(id=user_id, type=chat_type),
                  effective_message=message, callback_query=query)

    def complete(self, level="beginner", score=3, user_id=100):
        self.db.set_level(user_id, level)
        item = LESSONS[level][0]
        session = self.db.begin(user_id, item["id"], user_id)
        for i, question in enumerate(item["questions"][:3]):
            choice = question["correct"] if i < score else (question["correct"] + 1) % 3
            result = self.db.submit(user_id, user_id, session["token"], i, choice, item)
        return result

    def test_curriculum(self):
        self.assertEqual(len(LEVELS), 5)
        self.assertEqual(len(BY_ID), 100)
        for level, lessons in LESSONS.items():
            self.assertIn(level, LEVELS)
            for item in lessons:
                self.assertTrue(item["text"])
                self.assertEqual(len(item["questions"]), 7)
                self.assertNotEqual(item["remedial"], item["text"])
                for question in item["questions"]:
                    self.assertEqual(len(set(question["options"])), 3)
                    self.assertIn(question["correct"], range(3))
                    self.assertTrue(question["explanation"])

    async def test_application_configuration(self):
        app = bot.build_app("123456:offline_test_token", self.path)
        self.assertIsInstance(app.bot_data["store"], Store)
        self.assertEqual(len(app.handlers[0]), 13)
        self.assertIs(app.post_init, bot.on_ready)
        await app.shutdown()

    def test_restarts_duplicates_and_isolation(self):
        self.db.set_level(100, "advanced")
        self.db.set_level(200, "starter")
        item = BY_ID["a1"]
        session = self.db.begin(100, "a1", 100)
        args = (100, 100, session["token"], 0, item["questions"][0]["correct"], item)
        self.assertIsNone(self.db.submit(200, *args[1:]))
        self.assertIsNone(self.db.submit(100, 999, *args[2:]))
        self.assertTrue(self.db.submit(*args)["correct"])
        reopened = Store(self.path)
        self.assertEqual(reopened.session(100)["question_index"], 1)
        self.assertIsNone(reopened.submit(*args))
        self.assertIsNone(reopened.submit(100, 100, session["token"], 2, 0, item))
        self.assertEqual(reopened.user(100)["level"], "advanced")
        self.assertFalse(reopened.attempts(200))

    def test_results_and_level_change(self):
        self.assertEqual(self.complete(score=1)["score"], 1)
        self.assertFalse(bot.passed_ids(self.db.attempts(100)))
        self.assertEqual(self.complete(score=3)["score"], 3)
        self.assertEqual(bot.passed_ids(self.db.attempts(100)), {"b1"})
        self.db.begin(100, "b1", 100)
        self.db.set_level(100, "advanced")
        reopened = Store(self.path)
        self.assertIsNone(reopened.session(100))
        self.assertEqual(len(reopened.attempts(100, "beginner")), 2)
        self.assertEqual(len(reopened.attempts(100, "advanced")), 0)

    def test_deletion_is_per_user(self):
        self.complete(user_id=100)
        self.complete(user_id=200)
        self.db.studied(100, "b1")
        self.db.delete_user(100)
        self.assertIsNone(self.db.user(100))
        self.assertFalse(self.db.attempts(100))
        self.assertFalse(self.db.was_studied(100, "b1"))
        with self.db.connect() as db:
            for table in ("answers", "level_history", "sessions"):
                self.assertEqual(db.execute(f"SELECT COUNT(*) FROM {table} WHERE user_id=100").fetchone()[0], 0)
        self.assertEqual(len(self.db.attempts(200)), 1)

    async def test_complete_learning_flow_all_levels(self):
        for level in LEVELS:
            with self.subTest(level=level):
                await bot.callback(self.update(f"level:{level}"), self.context)
                item = LESSONS[level][0]
                await bot.callback(self.update(f'lesson:{item["id"]}'), self.context)
                await bot.callback(self.update(f'quiz:{item["id"]}'), self.context)
                for i in range(3):
                    session = self.db.session(100)
                    entry = session_plan(session)[i]
                    question = BY_ID[entry[0]]["questions"][entry[1]]
                    update = self.update(f'a:{session["token"]}:{i}:{question["correct"]}')
                    # Recreate the storage object to simulate a restart mid-quiz.
                    self.context.bot_data["store"] = Store(self.path)
                    await bot.callback(update, self.context)
                    update.callback_query.edit_message_text.assert_awaited_once()
                self.assertIsNone(self.db.session(100))
                self.assertEqual(self.db.attempts(100, level)[-1]["score"], 3)
        update = self.update()
        await bot.progress(update, self.context)
        self.assertIn("First: 3/3", update.effective_message.reply_text.call_args.args[0])

    async def test_lesson_gate_and_old_buttons(self):
        self.db.set_level(100, "beginner")
        await bot.callback(self.update("quiz:b1"), self.context)
        self.assertIsNone(self.db.session(100))
        await bot.callback(self.update("lesson:b1"), self.context)
        await bot.callback(self.update("quiz:b1"), self.context)
        token = self.db.session(100)["token"]
        self.db.set_level(100, "advanced")
        update = self.update(f"a:{token}:0:1")
        await bot.callback(update, self.context)
        self.assertFalse(self.db.attempts(100))
        update = self.update("lesson:b1")
        await bot.callback(update, self.context)
        update.effective_message.reply_text.assert_not_awaited()

    async def test_onboarding_and_groups(self):
        update = self.update()
        await bot.start(update, self.context)
        self.assertEqual(update.effective_message.reply_text.await_count, 2)
        choices = update.effective_message.reply_text.call_args.kwargs["reply_markup"]
        self.assertEqual(len(choices.inline_keyboard), 5)
        update = self.update(chat_type="group")
        await bot.start(update, self.context)
        self.assertIn("private chat", update.effective_message.reply_text.call_args.args[0])

    def test_retry_includes_all_mistakes_and_unseen_questions(self):
        self.complete(score=1)
        errors = {a["bank_index"] for a in self.db.mistakes(100, "b1")}
        plan = practice_plan(self.db, 100, "b1")
        indices = {entry[1] for entry in plan}
        self.assertTrue(errors <= indices)
        self.assertTrue({3, 4} <= indices)
        self.assertTrue(self.db.needs_remedial(100, "b1"))
        self.db.read_remedial(100, "b1")
        self.assertFalse(Store(self.path).needs_remedial(100, "b1"))
        session = self.db.begin(100, "b1", 100, plan)
        reopened = Store(self.path)
        self.assertEqual(session_plan(reopened.session(100)), plan)
        for i, entry in enumerate(plan):
            question = BY_ID[entry[0]]["questions"][entry[1]]
            reopened.submit(100, 100, session["token"], i, question["correct"])
        self.assertFalse(reopened.mistakes(100, "b1"))
        self.assertEqual(len(reopened.attempts(100)), 2)

    async def test_locked_lesson_and_repair_gate(self):
        self.db.set_level(100, "beginner")
        update = self.update("lesson:b2")
        await bot.callback(update, self.context)
        update.effective_message.reply_text.assert_not_awaited()
        self.complete(score=0)
        update = self.update("quiz:b1")
        self.db.studied(100, "b1")
        await bot.callback(update, self.context)
        self.assertIsNone(self.db.session(100))
        await bot.callback(self.update("lesson:b1"), self.context)
        await bot.callback(self.update("quiz:b1"), self.context)
        self.assertIsNotNone(self.db.session(100))

    def pass_lesson(self, item):
        plan = [[item["id"], i] for i in range(3)]
        session = self.db.begin(100, item["id"], 100, plan)
        for i in range(3):
            self.db.submit(100, 100, session["token"], i, item["questions"][i]["correct"])

    async def test_checkpoint_and_promotion_requires_correction(self):
        self.db.set_level(100, "starter")
        await bot.advance(self.update(), self.context)
        self.assertIsNone(self.db.session(100))
        for item in LESSONS["starter"]:
            self.pass_lesson(item)
        await bot.advance(self.update(), self.context)
        session = self.db.session(100)
        self.assertEqual(session["kind"], "checkpoint")
        plan = session_plan(session)
        self.assertEqual(len(plan), len(LESSONS["starter"]) * 2)
        for i, entry in enumerate(plan):
            question = BY_ID[entry[0]]["questions"][entry[1]]
            choice = (question["correct"] + 1) % 3 if i == 0 else question["correct"]
            self.db.submit(100, 100, session["token"], i, choice)
        self.assertEqual(self.db.attempts(100)[-1]["score"], len(plan) - 1)
        self.assertTrue(self.db.attempts(100)[-1]["passed"])
        await bot.advance(self.update(), self.context)
        self.assertEqual(self.db.user(100)["level"], "starter")
        wrong = plan[0]
        # Repair the missed checkpoint question; this also persists across restarts.
        repair = self.db.begin(100, wrong[0], 100, [wrong])
        question = BY_ID[wrong[0]]["questions"][wrong[1]]
        self.db.submit(100, 100, repair["token"], 0, question["correct"])
        await bot.advance(self.update(), self.context)
        self.assertEqual(self.db.user(100)["level"], "beginner")
        with self.db.connect() as db:
            self.assertEqual(db.execute("SELECT COUNT(*) FROM completions WHERE user_id=100").fetchone()[0], 1)
        self.assertGreater(len(self.db.attempts(100, "starter")), 0)

    async def test_failed_checkpoint_routes_to_repair(self):
        self.db.set_level(100, "upper")
        for item in LESSONS["upper"]:
            self.pass_lesson(item)
        session = self.db.begin(100, "@upper", 100, checkpoint_plan("upper"), "checkpoint")
        for i, entry in enumerate(session_plan(session)):
            question = BY_ID[entry[0]]["questions"][entry[1]]
            choice = question["correct"] if i < 6 else (question["correct"] + 1) % 3
            update = self.update(f'a:{session["token"]}:{i}:{choice}')
            await bot.callback(update, self.context)
        self.assertFalse(self.db.attempts(100)[-1]["passed"])
        self.assertIn("/review", update.effective_message.reply_text.call_args.args[0])
        await bot.advance(self.update(), self.context)
        self.assertEqual(self.db.user(100)["level"], "upper")
        self.assertTrue(weak_lessons(self.db, 100, "upper"))

    def test_legacy_database_migration(self):
        path = Path(self.temp.name) / "legacy.sqlite3"
        with closing(sqlite3.connect(path)) as db:
            db.executescript('''
                CREATE TABLE attempts (id INTEGER PRIMARY KEY, user_id INTEGER, level TEXT,
                    lesson_id TEXT, score INTEGER, total INTEGER, finished_at TEXT DEFAULT CURRENT_TIMESTAMP);
                INSERT INTO attempts(user_id,level,lesson_id,score,total) VALUES (100,'beginner','b1',2,3);
                CREATE TABLE sessions(user_id INTEGER PRIMARY KEY,token TEXT,lesson_id TEXT,chat_id INTEGER,
                    question_index INTEGER DEFAULT 0, score INTEGER DEFAULT 0);
                INSERT INTO sessions(user_id,token,lesson_id,chat_id) VALUES(100,'0123456789abcdef','b1',100);
                CREATE TABLE answers (id INTEGER PRIMARY KEY, user_id INTEGER, session_token TEXT,
                    lesson_id TEXT, question_index INTEGER, choice INTEGER, correct INTEGER,
                    answered_at TEXT DEFAULT CURRENT_TIMESTAMP, UNIQUE(session_token,question_index));
                INSERT INTO answers(user_id,session_token,lesson_id,question_index,choice,correct)
                    VALUES(100,'old_session','b1',1,0,0);
            ''')
        migrated = Store(path)
        self.assertEqual(len(session_plan(migrated.session(100))), 3)
        self.assertEqual(migrated.mistakes(100, "b1")[0]["bank_index"], 1)
        migrated.set_level(100, "beginner")
        self.assertEqual(mastered(migrated, 100, "beginner"), {"b1"})
        migrated.begin(100, "b1", 100)
        self.assertEqual(len(session_plan(migrated.session(100))), 3)
        migrated.seed_catalog(LESSONS)
        migrated.seed_catalog(LESSONS)
        with migrated.connect() as db:
            self.assertEqual(db.execute("SELECT COUNT(*) FROM lesson_catalog").fetchone()[0], len(BY_ID))

    def test_expanded_content_metadata_and_message_sizes(self):
        bands = {item["cefr"] for item in BY_ID.values()}
        self.assertTrue({"Pre-A1", "A1", "A2", "B1", "B2", "C1", "C2"} <= bands)
        for item in BY_ID.values():
            self.assertTrue(item["objective"])
            self.assertTrue(item["references"])
            self.assertTrue(item["tasks"]["writing"])
            self.assertTrue(item["tasks"]["speaking"])
            unique = {(q["prompt"], tuple(q["options"])) for q in item["questions"]}
            self.assertEqual(len(unique), 7, item["id"])
            rendered = f'{item["title"]}\n{item["objective"]}\n{item["text"]}'
            self.assertLess(len(rendered.encode("utf-16-le")) // 2, 3500, item["id"])
            for q in item["questions"]:
                self.assertIn(q["correct"], range(len(q["options"])))

    async def test_paginated_menu_roadmaps_and_resources(self):
        for level in LEVELS:
            self.db.set_level(100, level)
            update = self.update()
            await bot.roadmap_command(update, self.context)
            rendered = "".join(call.args[0] for call in update.effective_message.reply_text.call_args_list)
            for item in LESSONS[level]:
                self.assertIn(item["title"], rendered)
            for call in update.effective_message.reply_text.call_args_list:
                self.assertLessEqual(len(call.args[0].encode("utf-16-le")) // 2, 3500)
            update = self.update()
            await bot.show_lessons(update, self.context, 2)
            menu = update.effective_message.reply_text.call_args.kwargs["reply_markup"]
            self.assertLessEqual(len(menu.inline_keyboard), 7)
        update = self.update("page:beginner:1")
        await bot.callback(update, self.context)
        update.effective_message.reply_text.assert_not_awaited()
        update = self.update()
        await bot.resources(update, self.context)
        self.assertIn("listening", update.effective_message.reply_text.call_args.args[0])

    def test_old_checkpoint_does_not_pass_expanded_syllabus(self):
        from learning import checkpoint_passed
        self.db.set_level(100, "starter")
        old_plan = [[key, i] for key in ("s1", "s2", "s3", "s4") for i in (5, 6)]
        session = self.db.begin(100, "@starter", 100, old_plan, "checkpoint")
        for i, (key, index) in enumerate(old_plan):
            self.db.submit(100, 100, session["token"], i, BY_ID[key]["questions"][index]["correct"])
        self.assertTrue(self.db.attempts(100)[-1]["passed"])
        self.assertFalse(checkpoint_passed(self.db, 100, "starter"))

    def test_standalone_curriculum_export(self):
        from export_course import export
        database, report = export(Path(self.temp.name) / "catalog")
        with closing(sqlite3.connect(database)) as db:
            self.assertEqual(db.execute("SELECT COUNT(*) FROM lessons").fetchone()[0], 100)
            self.assertEqual(db.execute("SELECT COUNT(*) FROM questions").fetchone()[0], 700)
            self.assertEqual(db.execute("PRAGMA integrity_check").fetchone()[0], "ok")
            self.assertFalse(db.execute("PRAGMA foreign_key_check").fetchall())
        self.assertIn("C2", report.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
