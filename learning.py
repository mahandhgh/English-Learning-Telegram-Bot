"""Selection and progression policy, independent from Telegram."""

import json
import random
from collections import Counter

from curriculum import BY_ID, LESSONS
from roadmap import attempt_passed


def session_plan(session):
    return json.loads(session["plan"]) if session["plan"] else [[session["lesson_id"], i] for i in range(3)]


def mastered(db, user_id, level):
    return {a["lesson_id"] for a in db.attempts(user_id, level)
            if a["kind"] == "lesson" and attempt_passed(a)}


def available(db, user_id, level, lesson_id):
    done = mastered(db, user_id, level)
    if lesson_id in done or db.was_studied(user_id, lesson_id):
        return True  # Preserve access to previously opened units after an upgrade.
    for item in LESSONS[level]:
        if item["id"] == lesson_id:
            return True
        if item["id"] not in done:
            return False
    return False


def practice_plan(db, user_id, lesson_id):
    history = db.question_history(user_id, lesson_id)
    errors = [a["bank_index"] for a in db.mistakes(user_id, lesson_id)]
    counts = Counter(a["bank_index"] for a in history)
    pool = list(range(5))  # Last two questions are reserved for the checkpoint initially.
    if not history:
        selected = [0, 1, 2]
    else:
        remaining = [i for i in pool if i not in errors]
        random.shuffle(remaining)
        remaining.sort(key=lambda i: counts[i])  # Unseen first, then least-practised.
        selected = errors + remaining[:max(2, 3 - len(errors))]
    random.shuffle(selected)
    plan = []
    for index in selected:
        order = list(range(len(BY_ID[lesson_id]["questions"][index]["options"])))
        random.shuffle(order)
        plan.append([lesson_id, index, order])
    return plan


def checkpoint_plan(level):
    plan = [[item["id"], i] for item in LESSONS[level] for i in (5, 6)]
    random.shuffle(plan)
    for entry in plan:
        order = [0, 1, 2]
        random.shuffle(order)
        entry.append(order)
    return plan


def weak_lessons(db, user_id, level):
    return [item for item in LESSONS[level] if db.mistakes(user_id, item["id"])]


def checkpoint_passed(db, user_id, level):
    required = sorted(item["id"] for item in LESSONS[level])
    return any(a["kind"] == "checkpoint" and attempt_passed(a)
               and a["coverage"] and json.loads(a["coverage"]) == required
               for a in db.attempts(user_id, level))
