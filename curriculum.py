"""Original course material. IDs and released question indices remain stable."""

LEVELS = {
    "starter": "No English yet — start here",
    "beginner": "Beginner",
    "intermediate": "Intermediate",
    "upper": "Upper-intermediate",
    "advanced": "Advanced — C1 to C2",
}


def q(prompt, options, correct, explanation):
    return dict(prompt=prompt, options=options, correct=correct, explanation=explanation)


def lesson(id, title, text, questions):
    return dict(id=id, title=title, text=text, questions=questions)


LESSONS = {
    "starter": [
        lesson("s1", "Hello!", "👋 Hello = Hi\nSay 'Hello' when you meet someone.\n\n"
               "👋 Goodbye = Bye\nSay 'Goodbye' when you leave.\n\n"
               "🙂 My name is Sam.\nUse 'My name is ...' + your name.\n\n"
               "Example:\nA: Hello! My name is Sam.\nB: Hi, Sam! My name is Alex.", [
            q("👋 You meet Alex. What do you say?", ["Hello!", "Goodbye!", "Good night!"], 0, "Use 'Hello' when you meet someone."),
            q("Your name is Sam. Choose the sentence.", ["My Sam name.", "My name is Sam.", "Goodbye Sam name."], 1, "Use 'My name is' + your name."),
            q("👋 You leave. What do you say?", ["My name is ...", "Hello!", "Goodbye!"], 2, "Use 'Goodbye' when you leave."),
        ]),
        lesson("s2", "One, two, three", "1 = one\n2 = two\n3 = three\n\n"
               "🍎 one apple\n🍎🍎 two apples\n🍎🍎🍎 three apples\n\n"
               "One apple. Two apples. Three apples.\nWith two or three, add -s: apple → apples.", [
            q("🍎🍎 How many?", ["One", "Two", "Three"], 1, "🍎🍎 = two apples."),
            q("Choose the correct phrase.", ["one apples", "three apple", "three apples"], 2, "Use 'apples' with three."),
            q("Which word means 1?", ["one", "three", "two"], 0, "1 = one."),
        ]),
    ],
    "beginner": [
        lesson("b1", "Present simple: habits", "Use the present simple for habits and routines.\n\n"
               "I/you/we/they + base verb: I work every day.\nHe/she/it + verb with -s: She works every day.\n"
               "After a consonant, -y changes to -ies: study → studies.\n\n"
               "Negatives: I don't work on Sundays. He doesn't work on Sundays.\n"
               "After doesn't, use the base verb: doesn't work, not doesn't works.", [
            q("She ___ English every day.", ["study", "studies", "studying"], 1, "With 'she', study changes to studies."),
            q("Choose the correct negative.", ["He doesn't works here.", "He don't work here.", "He doesn't work here."], 2, "Use doesn't + the base verb work."),
            q("Which sentence describes a routine?", ["I walk to school every day.", "I am walking right now.", "I walked yesterday."], 0, "Every day signals a routine; use the present simple."),
        ]),
        lesson("b2", "Present continuous: now", "Use am/is/are + verb-ing for an action happening now.\n\n"
               "I am reading. She is cooking. They are studying.\n"
               "Negative: She isn't cooking.\nQuestion: Are they studying?\n\n"
               "Compare: I read every evening (habit). I am reading now (in progress).", [
            q("Look! They ___ football.", ["play", "is playing", "are playing"], 2, "They takes are; an action happening now uses verb-ing."),
            q("Choose the correct question.", ["Is she working?", "Does she working?", "She is work?"], 0, "Move is before she: Is she working?"),
            q("Which action is in progress now?", ["I cook every day.", "I am cooking now.", "I cooked yesterday."], 1, "Am cooking is the present continuous."),
        ]),
    ],
    "intermediate": [
        lesson("i1", "Present perfect or past simple?", "Present perfect: have/has + past participle. "
               "Use it for experience up to now when no finished past time is specified.\n"
               "I've visited Rome twice. Have you ever tried sushi?\n\n"
               "Past simple: use it with a finished past time.\nI visited Rome in 2022.\n\n"
               "With since (a starting point) or for (a duration), the present perfect can describe "
               "a state continuing now: I've known her since 2020 / for six years.", [
            q("I ___ that film yesterday.", ["have seen", "saw", "have see"], 1, "Yesterday is a finished past time, so use saw."),
            q("___ you ever ___ to Japan?", ["Did / been", "Have / went", "Have / been"], 2, "Use Have you ever been for life experience up to now."),
            q("We still live here. We ___ here since 2020.", ["have lived", "lived", "are live"], 0, "Have lived connects a past starting point with the present."),
        ]),
        lesson("i2", "First and second conditionals", "First conditional: if + present simple, will + base verb. "
               "Use it for a real future possibility: If it rains, we'll stay home.\n\n"
               "Second conditional: if + past simple, would + base verb. "
               "Use it for an imagined or unlikely present/future situation: "
               "If I had more time, I would travel.\n\n"
               "In formal hypothetical statements, use were: If I were you, I'd ask.", [
            q("A real possibility: If she calls tonight, I ___ her.", ["would tell", "told", "will tell"], 2, "Use if + present, will + base verb for a real future possibility."),
            q("I don't have a car. If I ___ one, I would drive to work.", ["had", "have", "will have"], 0, "Use past simple for an imagined present situation."),
            q("Choose the formal advice.", ["If I am you, I would wait.", "If I were you, I would wait.", "If I will be you, I wait."], 1, "If I were you introduces hypothetical advice."),
        ]),
    ],
    "upper": [
        lesson("u1", "Past deductions", "Use modal + have + past participle for deductions about the past.\n\n"
               "Must have: strong positive deduction. The ground is wet; it must have rained.\n"
               "Might/may/could have: a possibility. She might have missed the train.\n"
               "Can't have: strong negative deduction. He can't have taken it; he was abroad.\n\n"
               "These express your judgement, not a confirmed fact.", [
            q("The lights were on all night. Someone ___ forgotten to switch them off. (strong deduction)", ["must have", "can't have", "must"], 0, "Must have + past participle expresses a strong past deduction."),
            q("I'm not sure why she's late. She ___ missed the bus.", ["must", "might have", "can't"], 1, "Might have expresses a possible past explanation."),
            q("He was in Canada all week. He ___ attended yesterday's meeting in person in London.", ["must have", "might", "can't have"], 2, "Can't have expresses a strong negative deduction about a past event."),
        ]),
        lesson("u2", "Mixed conditionals", "A mixed conditional can connect a past cause to a present result.\n\n"
               "If + past perfect, would + base verb (present result).\n"
               "If I had studied medicine, I would be a doctor now.\n"
               "Reality: I didn't study medicine; I'm not a doctor now.\n\n"
               "Compare a past result: If I had studied, I would have passed yesterday. "
               "That is a third conditional, not this past-to-present pattern.", [
            q("If I had accepted that job, I ___ in Paris now.", ["would have lived", "will live", "would live"], 2, "A present result takes would + base verb."),
            q("Which sentence links a past cause to a present result?", ["If she had saved more, she would be debt-free now.", "If she saves, she will buy a bike.", "If she had saved, she would have bought it last year."], 0, "Had saved is the past cause; would be ... now is the present result."),
            q("If we ___ the map, we wouldn't be lost now.", ["check", "had checked", "would check"], 1, "Use past perfect for the unreal past cause."),
        ]),
    ],
    "advanced": [
        lesson("a1", "Inversion for emphasis", "In formal or emphatic writing, fronted negative or restrictive expressions "
               "can trigger auxiliary–subject inversion.\n\n"
               "I had rarely seen such precision. → Rarely had I seen such precision.\n"
               "She understood only then. → Only then did she understand.\n\n"
               "Use do/does/did if there is no existing auxiliary; keep the main verb in its base form.\n"
               "With 'Not until ...', invert the main clause: Not until the meeting ended did she speak.", [
            q("Rarely ___ such a convincing argument.", ["I have heard", "have I heard", "have heard I"], 1, "Fronted rarely triggers inversion: have I heard."),
            q("Only then ___ the implications.", ["she understood", "did she understood", "did she understand"], 2, "Use did + subject + base verb after fronted Only then."),
            q("Choose the correct formal sentence.", ["Not until he arrived did we begin.", "Not until did he arrive we began.", "Not until he arrived we did began."], 0, "Invert the main clause (did we begin), not the clause after until."),
        ]),
        lesson("a2", "Hedging academic claims", "Match the strength of a claim to the evidence.\n\n"
               "An observational association does not, by itself, establish causation.\n"
               "Overstated: This survey proves that exercise causes better sleep.\n"
               "Calibrated: These results suggest an association between exercise and better sleep.\n\n"
               "Useful forms: may indicate, appears to, is consistent with.\n"
               "State scope and limitations: in this sample; further research is needed. "
               "Avoid piling up hedges that obscure your meaning.", [
            q("An observational survey finds a correlation. Which claim matches the evidence?", ["Exercise always cures insomnia.", "The survey proves exercise causes better sleep.", "The findings suggest an association between exercise and sleep quality."], 2, "An observed association alone does not establish causation."),
            q("Which revision communicates uncertainty without excessive hedging?", ["This pattern may indicate a sampling effect.", "This pattern might perhaps possibly seem to maybe indicate an effect.", "This pattern certainly proves every hypothesis."], 0, "One clear hedge communicates uncertainty without clutter."),
            q("The study examined 30 volunteers at one university. Which limitation is appropriate?", ["The result applies to every population.", "The findings may not generalize beyond this sample.", "The small sample guarantees causation."], 1, "A small, restricted sample limits generalization."),
        ]),
    ],
}

from course_expansion import expand

expand(LESSONS, q, lesson)
from extended_course import extend
extend(LESSONS)
BY_ID = {item["id"]: item for lessons in LESSONS.values() for item in lessons}
