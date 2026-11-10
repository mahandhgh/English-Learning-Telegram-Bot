"""English lessons, short quizzes and durable per-user progress."""
import logging
import os
from pathlib import Path
import re

from telegram import BotCommand, InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes

from curriculum import BY_ID, LESSONS, LEVELS
from storage import Store
from learning import (available, checkpoint_passed, checkpoint_plan, mastered,
                      practice_plan, session_plan, weak_lessons)
from roadmap import ORDER, SOURCES, TRACKS, attempt_passed


def store(context):
    return context.bot_data["store"]


def keyboard(rows):
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(label, callback_data=data) for label, data in row]
        for row in rows
    ])


def text_chunks(text, limit=3500):
    """Stay below Telegram's limit even with non-BMP symbols (UTF-16 units)."""
    chunk, size = [], 0
    for char in text:
        width = 2 if ord(char) > 0xFFFF else 1
        if size + width > limit:
            yield "".join(chunk)
            chunk, size = [], 0
        chunk.append(char)
        size += width
    if chunk:
        yield "".join(chunk)


async def send_text(update, text):
    for chunk in text_chunks(text):
        await update.effective_message.reply_text(chunk)


async def private_chat(update):
    if update.effective_chat.type != "private":
        if update.callback_query:
            await update.callback_query.answer("Please open a private chat with me.")
        else:
            await update.effective_message.reply_text("Please open a private chat with me to learn and track your progress.")
        return False
    return True


async def choose_level(update):
    await update.effective_message.reply_text(
        "Choose your current English level. You can change it later with /level.\n"
        "This is your own estimate, not a placement test or an earned promotion.",
        reply_markup=keyboard([[(label, f"level:{key}")] for key, label in LEVELS.items()]),
    )


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not await private_chat(update):
        return
    await update.effective_message.reply_text(
        "Welcome! 👋\nFollow your roadmap: learn, practise, review mistakes and take a checkpoint.\n\n"
        "/roadmap — your goals and next steps\n"
        "/resources — extra listening, reading and skills practice\n"
        "/lesson — learn or review\n/quiz — start or resume a quiz\n"
        "/progress — see your results\n/review — repair weak areas\n"
        "/advance — checkpoint and next course track\n/level — change your starting level\n"
        "/privacy — what we save\n/delete — delete your learning data\n\n"
        "Your progress is saved, even when the bot restarts."
    )
    if not store(context).user(update.effective_user.id):
        await choose_level(update)
    else:
        await show_lessons(update, context)


async def level(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if await private_chat(update):
        await choose_level(update)


def passed_ids(attempts):
    return {a["lesson_id"] for a in attempts if a["kind"] == "lesson" and attempt_passed(a)}


async def show_lessons(update, context, page=None):
    user_id = update.effective_user.id
    user = store(context).user(user_id)
    if not user:
        await choose_level(update)
        return
    completed = passed_ids(store(context).attempts(user_id, user["level"]))
    lessons = LESSONS[user["level"]]
    next_lesson = next((item for item in lessons if item["id"] not in completed), None)
    page_size = 6
    if page is None:
        page = lessons.index(next_lesson) // page_size if next_lesson else 0
    page = max(0, min(page, (len(lessons) - 1) // page_size))
    visible = lessons[page * page_size:(page + 1) * page_size]
    text = f'Level: {LEVELS[user["level"]]}\n✅ passed · ▶ available · 🔒 finish earlier lessons\nNew quizzes require at least 80%.'
    if next_lesson:
        text += f'\nSuggested next: {next_lesson["title"]}'
    else:
        text += "\nAll lesson quizzes passed. Review mistakes with /review, then use /advance."
    text += f'\nPage {page + 1}/{(len(lessons) + page_size - 1) // page_size}'
    rows = [[(f'{"✅" if item["id"] in completed else "▶" if available(store(context), user_id, user["level"], item["id"]) else "🔒"} [{item["cefr"]}] {item["title"]}', f'lesson:{item["id"]}')] for item in visible]
    navigation = []
    if page > 0:
        navigation.append(("← Previous", f'page:{user["level"]}:{page - 1}'))
    if (page + 1) * page_size < len(lessons):
        navigation.append(("Next →", f'page:{user["level"]}:{page + 1}'))
    if navigation:
        rows.append(navigation)
    await update.effective_message.reply_text(text, reply_markup=keyboard(rows))


async def lesson_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if await private_chat(update):
        await show_lessons(update, context)


async def send_question(update, context, session):
    plan = session_plan(session)
    index = session["question_index"]
    entry = plan[index]
    item = BY_ID[entry[0]]
    question = item["questions"][entry[1]]
    order = entry[2] if len(entry) > 2 else range(len(question["options"]))
    await update.effective_message.reply_text(
        f'{"Checkpoint · " if session["kind"] == "checkpoint" else ""}{item["title"]}\nQuestion {index + 1}/{len(plan)}\n\n{question["prompt"]}',
        reply_markup=keyboard([
            [(question["options"][i], f'a:{session["token"]}:{index}:{i}')]
            for i in order
        ]),
    )


async def quiz_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not await private_chat(update):
        return
    session = store(context).session(update.effective_user.id)
    if session:
        await send_question(update, context, session)
    else:
        await update.effective_message.reply_text("Read a lesson first, then tap 'Start quiz'.")
        await show_lessons(update, context)


async def callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not await private_chat(update):
        return
    query = update.callback_query
    data = query.data
    db = store(context)
    user_id = update.effective_user.id
    user = db.user(user_id)

    if data.startswith("level:"):
        selected = data.split(":", 1)[1]
        if selected not in LEVELS:
            await query.answer("Unknown level.")
            return
        db.set_level(user_id, selected)
        await query.answer()
        await query.edit_message_text(
            f'Level saved: {LEVELS[selected]}\nPast results are kept. Any unfinished quiz has been cancelled.'
        )
        await show_lessons(update, context)
        return

    if not user:
        await query.answer("Please choose your level first.")
        await choose_level(update)
        return

    if data.startswith("page:"):
        match = re.fullmatch(r"page:([a-z]+):([0-9]+)", data)
        if not match or match[1] != user["level"]:
            await query.answer("That menu is outdated. Use /lesson.")
            return
        await query.answer()
        await show_lessons(update, context, int(match[2]))
        return

    if data.startswith(("lesson:", "quiz:")):
        action, lesson_id = data.split(":", 1)
        item = next((x for x in LESSONS[user["level"]] if x["id"] == lesson_id), None)
        if not item:
            await query.answer("That lesson is not in your current level. Use /lesson.")
            return
        if not available(db, user_id, user["level"], lesson_id):
            await query.answer("Finish the earlier lessons first. See /roadmap.")
            return
        if action == "lesson":
            await query.answer()
            repair = bool(db.mistakes(user_id, lesson_id))
            body = item["remedial"] if repair else item["text"]
            await update.effective_message.reply_text(
                f'{"Repair lesson · " if repair else ""}{item["title"]} [{item["cefr"]}]\nGoal: {item["objective"]}\n\n{body}\n\n'
                + ("Your next quiz mixes missed questions with unseen or less-practised questions." if repair else "Read the examples, then try the quiz."),
                reply_markup=keyboard([[("Start quiz", f'quiz:{lesson_id}')]]),
            )
            db.studied(user_id, lesson_id)
            if repair:
                db.read_remedial(user_id, lesson_id)
            tasks = item["tasks"]
            await send_text(update,
                f'Apply it · {item["title"]}\n\nWriting / practical task: {tasks["writing"]}\n\n'
                f'Speaking / partner practice: {tasks["speaking"]}\n\n{tasks["self_check"]}\n\n'
                'These tasks need self, partner or teacher feedback; the bot does not automatically grade writing or speech. '
                'For audio/video and longer texts, use /resources.')
        else:
            if not db.was_studied(user_id, lesson_id):
                await query.answer("Please open the lesson before taking its quiz.")
                return
            session = db.session(user_id)
            if session and session["lesson_id"] != lesson_id:
                await query.answer("Finish your current quiz first. Use /quiz to resume.")
                return
            if not session:
                if db.needs_remedial(user_id, lesson_id):
                    await query.answer("Open the repair lesson first with /review or /lesson.")
                    return
                session = db.begin(user_id, lesson_id, update.effective_chat.id, practice_plan(db, user_id, lesson_id))
            await query.answer()
            await send_question(update, context, session)
        return

    if data.startswith("a:"):
        match = re.fullmatch(r"a:([a-f0-9]{16}):([0-9]+):([0-9]+)", data)
        session = db.session(user_id)
        if not match or not session:
            await query.answer("This question is no longer active. Use /quiz.")
            return
        token, index, choice = match.groups()
        result = db.submit(user_id, update.effective_chat.id, token, int(index), int(choice))
        if result is None:
            await query.answer("This question is no longer active. Use /quiz.")
            return
        await query.answer()
        item = BY_ID[result["lesson_id"]]
        question = item["questions"][result["bank_index"]]
        feedback = "✅ Correct!" if result["correct"] else "Not quite. Keep learning!"
        await query.edit_message_text(
            f'{feedback}\n\n{question["prompt"]}\n'
            f'Answer: {question["options"][question["correct"]]}\n\n{question["explanation"]}'
        )
        if result["finished"]:
            total = result["total"]
            if result["kind"] == "checkpoint":
                guidance = ("Checkpoint passed! Use /review to clear any remaining mistakes, then /advance to complete this track."
                            if result["passed"] else "Let's strengthen the weak areas. Use /review for repair lessons, then /advance to retry.")
            else:
                guidance = ("Lesson passed! 🎉 Review any mistakes with /review or continue with /lesson."
                            if result["passed"] else "Let's try a different explanation. Use /review for a repair lesson and a mixed retry quiz.")
            await update.effective_message.reply_text(
                f'Quiz complete: {result["score"]}/{total}\n'
                + guidance
                + "\nYour result is saved. See /progress."
            )
        else:
            await send_question(update, context, db.session(user_id))
        return
    await query.answer("Please use /lesson to continue.")


async def progress(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not await private_chat(update):
        return
    db = store(context)
    user_id = update.effective_user.id
    user = db.user(user_id)
    if not user:
        await choose_level(update)
        return
    attempts = db.attempts(user_id, user["level"])
    completed = passed_ids(attempts)
    lines = [f'Your level: {LEVELS[user["level"]]}',
             f'Lessons passed: {len(completed)}/{len(LESSONS[user["level"]])}',
             f'Completed quizzes at this level: {len(attempts)}']
    for item in LESSONS[user["level"]]:
        results = [a for a in attempts if a["lesson_id"] == item["id"] and a["kind"] == "lesson"]
        if results:
            first, latest = results[0], results[-1]
            best = max(results, key=lambda a: a["score"] / a["total"])
            lines.append(f'\n{item["title"]}\nFirst: {first["score"]}/{first["total"]} · Latest: {latest["score"]}/{latest["total"]} · Best: {best["score"]}/{best["total"]}')
    weak = weak_lessons(db, user_id, user["level"])
    lines.append(f'\nUnresolved mistakes: {sum(len(db.mistakes(user_id, x["id"])) for x in weak)}')
    lines.append(f'Checkpoint: {"passed" if checkpoint_passed(db, user_id, user["level"]) else "not passed yet"}')
    lines.append('Next step: /roadmap')
    lines.append(f'\nCompleted quizzes across all levels: {len(db.attempts(user_id))}')
    if db.session(user_id):
        lines.append('You have an unfinished quiz. Use /quiz to resume.')
    await send_text(update, "\n".join(lines))


async def roadmap_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not await private_chat(update):
        return
    db = store(context)
    user_id = update.effective_user.id
    user = db.user(user_id)
    if not user:
        await choose_level(update)
        return
    level_id = user["level"]
    track = TRACKS[level_id]
    done = mastered(db, user_id, level_id)
    lines = [f'Your roadmap · {LEVELS[level_id]}', f'Learning target: {track["target"]}',
             track["goal"], "\nCourse units, in order:"]
    for i, item in enumerate(LESSONS[level_id]):
        status = "✅" if item["id"] in done else "▶" if available(db, user_id, level_id, item["id"]) else "🔒"
        lines.append(f'{status} {i + 1}. [{item["cefr"]}] {item["title"]}\nGoal: {item["objective"]}')
    checkpoint_count = len(checkpoint_plan(level_id))
    lines.extend([
        "\nTo complete this course track:\n1. Pass every lesson quiz (80% or more).\n"
        f"2. Correct outstanding mistakes using /review.\n3. Pass the {checkpoint_count}-question checkpoint (80% or more).\n"
        "4. Correct any checkpoint mistakes, then use /advance.",
        f'\nBeyond the bot: {track["outside"]}',
        f'\nFurther coverage needed for a full course: {track["next_topics"]}',
        "\nThe internal quizzes assess selected-response language use and reading. "
        "Completion is not CEFR certification; listening, speaking and free writing are not automatically assessed. /resources /sources",
    ])
    weak = weak_lessons(db, user_id, level_id)
    if weak:
        lines.append(f'\nRecommended now: /review — {len(weak)} lesson(s) with unresolved mistakes.')
    elif len(done) < len(LESSONS[level_id]):
        lines.append('\nRecommended now: /lesson — continue your next unit.')
    else:
        lines.append('\nRecommended now: /advance — checkpoint or track completion.')
    await send_text(update, "\n".join(lines))


async def review(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not await private_chat(update):
        return
    db = store(context)
    user_id = update.effective_user.id
    user = db.user(user_id)
    if not user:
        await choose_level(update)
        return
    weak = weak_lessons(db, user_id, user["level"])
    if not weak:
        await update.effective_message.reply_text("No outstanding mistakes at this level! Use /lesson to practise or /advance when ready.")
        return
    await update.effective_message.reply_text(
        "Let's repair the difficult parts. Choose a lesson for a different explanation and worked examples. "
        "Then take a quiz containing your missed questions plus unseen or less-practised questions. "
        "A mistake leaves this list after you answer that question correctly.",
        reply_markup=keyboard([
            [(f'{item["title"]} · {len(db.mistakes(user_id, item["id"]))} to review', f'lesson:{item["id"]}')]
            for item in weak
        ]),
    )


async def advance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not await private_chat(update):
        return
    db = store(context)
    user_id = update.effective_user.id
    user = db.user(user_id)
    if not user:
        await choose_level(update)
        return
    level_id = user["level"]
    session = db.session(user_id)
    if session:
        await update.effective_message.reply_text("You have an unfinished quiz. Use /quiz to finish it first.")
        return
    if len(mastered(db, user_id, level_id)) != len(LESSONS[level_id]):
        await update.effective_message.reply_text("Pass every lesson quiz at this level first. Your next steps are in /roadmap.")
        return
    if weak_lessons(db, user_id, level_id):
        await update.effective_message.reply_text("Correct your outstanding mistakes before advancing. Use /review for repair lessons.")
        return
    if checkpoint_passed(db, user_id, level_id):
        db.record_completion(user_id, level_id)
        position = ORDER.index(level_id)
        if position + 1 == len(ORDER):
            await update.effective_message.reply_text("🎉 You completed all units and the checkpoint in this advanced course track! "
                                                      "Continue with the wider practice goals in /roadmap. This is not a CEFR certificate.")
        else:
            next_level = ORDER[position + 1]
            db.set_level(user_id, next_level)
            await update.effective_message.reply_text(f'🎉 Course track completed! Next track: {LEVELS[next_level]}.\nYour history is saved. See /roadmap.')
            await show_lessons(update, context)
        return
    plan = checkpoint_plan(level_id)
    session = db.begin(user_id, f"@{level_id}", update.effective_chat.id, plan, "checkpoint")
    required = (len(plan) * 80 + 99) // 100
    await update.effective_message.reply_text(
        f'Checkpoint: {len(plan)} questions covering all {len(LESSONS[level_id])} units. Aim for at least 80% ({required}/{len(plan)}). '
        "These questions differ from the initial lesson practice. On later attempts, some questions repeat."
    )
    await send_question(update, context, session)


async def sources(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if await private_chat(update):
        await send_text(update,
            "Curriculum references:\n\n" + "\n\n".join(f"{label}\n{url}" for label, url in SOURCES)
            + "\n\nOur lesson texts and questions are original. Our sequence and 80% rule are project design choices. "
            "The bot is independent and is not an official Duolingo or CEFR course."
        )


async def resources(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not await private_chat(update):
        return
    user = store(context).user(update.effective_user.id)
    target = TRACKS[user["level"]]["target"] if user else "Choose a level with /level."
    await send_text(update,
        f'Extra skills practice · {target}\nChoose the suitable level on each official site.\n\n'
        'Listening (recordings, A1–C1):\nhttps://learnenglish.britishcouncil.org/free-resources/listening\n\n'
        'Reading (A1–C1):\nhttps://learnenglish.britishcouncil.org/free-resources/reading\n\n'
        'Writing models (A1–C1):\nhttps://learnenglish.britishcouncil.org/free-resources/writing\n\n'
        'Speaking videos (A1–B2):\nhttps://learnenglish.britishcouncil.org/free-resources/speaking\n\n'
        'C2 assessment scope:\nhttps://www.cambridgeenglish.org/exams-and-tests/qualifications/proficiency/format/\n\n'
        'External work is not tracked or marked by this bot. For starting learners, use the A1 material with help from a partner or teacher. '
        'Advanced learners also need long texts, varied audio, spontaneous interaction and feedback on substantial writing.')


async def privacy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if await private_chat(update):
        await update.effective_message.reply_text(
            "I save your Telegram user ID, chat ID for an active quiz, selected level and level changes, "
            "opened lessons and repair lessons, quiz answers, scores, track completions and learning timestamps in the operator's database. "
            "I do not save your name or message text.\n\nUse /delete to delete your learning data."
        )


async def delete(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if await private_chat(update):
        if context.args == ["confirm"]:
            store(context).delete_user(update.effective_user.id)
            await update.effective_message.reply_text("Your learning data has been deleted. Use /start to begin again.")
        else:
            await update.effective_message.reply_text("To permanently delete your saved learning data, send /delete confirm.")


async def on_error(update: object, context: ContextTypes.DEFAULT_TYPE):
    logging.getLogger(__name__).error("Bot operation failed: %s", type(context.error).__name__)
    if isinstance(update, Update) and update.effective_message:
        try:
            await update.effective_message.reply_text("Something went wrong. Use /quiz to resume, or /lesson to continue.")
        except Exception:
            pass


async def on_ready(application: Application):
    await application.bot.set_my_commands([
        BotCommand("start", "Welcome and help"), BotCommand("level", "Choose your level"),
        BotCommand("lesson", "Learn or review a lesson"), BotCommand("quiz", "Resume your quiz"),
        BotCommand("roadmap", "Your goals and next steps"), BotCommand("review", "Repair weak areas"),
        BotCommand("advance", "Checkpoint and next course track"), BotCommand("sources", "Curriculum references"),
        BotCommand("resources", "Official skills practice and audio"),
        BotCommand("progress", "See your learning progress"), BotCommand("privacy", "Stored learning data"),
        BotCommand("delete", "Delete your learning data"),
    ])
    print("Connected to Telegram. Press Ctrl+C to stop.", flush=True)


def build_app(token, db_path):
    app = Application.builder().token(token).post_init(on_ready).build()
    app.bot_data["store"] = Store(db_path)
    app.bot_data["store"].seed_catalog(LESSONS)
    for commands, handler in [(["start", "help"], start), (["level"], level),
                              (["lesson"], lesson_command), (["quiz"], quiz_command),
                              (["progress", "score"], progress), (["privacy"], privacy), (["delete"], delete),
                              (["roadmap"], roadmap_command), (["review"], review),
                              (["advance"], advance), (["sources"], sources), (["resources"], resources)]:
        app.add_handler(CommandHandler(commands, handler))
    app.add_handler(CallbackQueryHandler(callback))
    app.add_error_handler(on_error)
    return app


def main():
    token = os.environ.get("TELEGRAM_BOT_TOKEN", "").strip()
    if not re.fullmatch(r"[0-9]+:[A-Za-z0-9_-]+", token):
        raise SystemExit("Missing or invalid TELEGRAM_BOT_TOKEN. Run run.ps1 and paste only the BotFather token.")
    logging.basicConfig(level=logging.WARNING)
    db_path = Path(__file__).resolve().parent / "data" / "learning.sqlite3"
    app = build_app(token, db_path)
    print("Connecting to Telegram...", flush=True)
    app.run_polling(allowed_updates=["message", "callback_query"])


if __name__ == "__main__":
    main()
