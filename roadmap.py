"""Project curriculum targets inspired by CEFR, not an official CEFR syllabus."""

SOURCES = [
    ("Council of Europe: CEFR descriptors", "https://www.coe.int/en/web/common-european-framework-reference-languages/cefr-descriptors"),
    ("Duolingo: learning path and personalised practice", "https://blog.duolingo.com/duolingo-101-how-to-learn-a-language-on-duolingo/"),
    ("Duolingo: reviewing previous lessons", "https://blog.duolingo.com/how-to-review-lessons-on-duolingo/"),
    ("British Council: grammar reference and practice", "https://learnenglish.britishcouncil.org/free-resources/grammar"),
    ("British Council: C1 grammar", "https://learnenglish.britishcouncil.org/free-resources/grammar/c1"),
    ("English Profile: English Grammar Profile", "https://englishprofile.org/?menu=egp-online"),
    ("Cambridge English: C2 skills and assessment format", "https://www.cambridgeenglish.org/exams-and-tests/qualifications/proficiency/format/"),
]

TRACKS = {
    "starter": {
        "target": "Pre-A1 to early A1 foundations",
        "goal": "Recognise basic greetings, names, small quantities and polite requests.",
        "goals": ["Introduce yourself and greet someone.", "Recognise one, two and three and simple plurals.", "Match I/you/he/she with am/are/is.", "Ask for a simple item and respond to thanks."],
        "outside": "Say your name aloud; count real objects; practise a short greeting with another person.",
        "next_topics": "Recorded sound contrasts, illustrated comprehension and supported interaction still need audio/visual assets and human feedback.",
    },
    "beginner": {
        "target": "A1–A2 foundations",
        "goal": "Describe routines, current actions, past events and simple future plans.",
        "goals": ["Describe regular activities.", "Describe what is happening now.", "Ask and answer about a finished past event.", "Discuss intentions, arrangements and immediate decisions."],
        "outside": "Write a short daily diary and record a one-minute description of your plans.",
        "next_topics": "Broader vocabulary in varied situations, sustained listening and spontaneous interaction need additional materials and assessment.",
    },
    "intermediate": {
        "target": "B1-oriented practice",
        "goal": "Connect experiences, explain a problem, propose a solution and relay a message.",
        "goals": ["Distinguish experience up to now from a finished past event.", "Discuss realistic and imagined possibilities.", "Identify a problem, cause, solution and drawback.", "Report what another person said."],
        "outside": "Summarise a short article; tell a past experience aloud and ask a partner follow-up questions.",
        "next_topics": "Longer authentic texts and audio, productive feedback and delayed retention checks remain necessary.",
    },
    "upper": {
        "target": "B2-oriented practice",
        "goal": "Evaluate explanations, connect causes and results, and discuss competing proposals.",
        "goals": ["Express different degrees of certainty about past events.", "Relate an unreal past cause to a present result.", "Separate claims, evidence, assumptions and counterarguments.", "Disagree diplomatically and negotiate a practical alternative."],
        "outside": "Compare two opinion pieces; record a balanced argument with a counterargument and response.",
        "next_topics": "Extended reading across genres, spontaneous discussion, pronunciation feedback and marked free writing remain necessary.",
    },
    "advanced": {
        "target": "C1 and C2-oriented practice (separate labelled units)",
        "goal": "Progress from advanced grammatical control to nuance, complex interpretation, critical synthesis and mediation.",
        "goals": ["Use inversion for formal emphasis.", "Calibrate a claim to the strength and scope of its evidence.", "Interpret irony and indirect meaning using context.", "Synthesise contrasting sources with attribution and limitations."],
        "outside": "Write a synthesis of two sources; present it aloud and answer challenging follow-up questions.",
        "next_topics": "Full-length demanding reading/audio, extensive lexical breadth, spontaneous spoken mediation and expert assessment of free writing are not covered by the selected-response tests.",
    },
}

ORDER = list(TRACKS)
PASS_PERCENT = 80  # A product rule, not a CEFR or Duolingo standard.


def is_pass(score, total):
    return total > 0 and score * 100 >= total * PASS_PERCENT


def attempt_passed(attempt):
    return bool(attempt["passed"]) if attempt["passed"] is not None else attempt["score"] * 3 >= attempt["total"] * 2
