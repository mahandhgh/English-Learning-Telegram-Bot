"""Assemble the expanded course without changing released lesson/question IDs."""
from course_starter import UNITS as STARTER
from course_beginner import UNITS as BEGINNER
from course_intermediate import UNITS as INTERMEDIATE
from course_upper import UNITS as UPPER
from course_advanced import UNITS as ADVANCED
from course_authoring import REFERENCES
from course_supplement import UNITS as SUPPLEMENT

ADDITIONS = dict(starter=STARTER, beginner=BEGINNER, intermediate=INTERMEDIATE, upper=UPPER, advanced=ADVANCED)
BANDS = dict(starter="Pre-A1", beginner="A1–A2", intermediate="B1", upper="B2", advanced="C1")
SEQUENCES = {
    "starter": "s1 s05 s06 s3 s2 s07 s08 s09 s10 s11 s12 s13 s14 s15 s16 s4 s17 s18 s19 s20",
    "beginner": "b1 b17 b13 b05 b06 b12 b14 b2 b07 b08 b09 b3 b10 b4 b11 b18 b19 b20 b15 b16",
    "intermediate": "i1 i06 i05 i07 i2 i08 i09 i10 i11 i12 i13 i3 i14 i4 i15 i16 i17 i18 i19 i20",
    "upper": "u1 u11 u10 u05 u2 u06 u07 u08 u09 u12 u13 u14 u15 u3 u16 u4 u17 u18 u19 u20",
    "advanced": "a1 a05 a06 a07 a08 a09 a10 a17 a2 a3 a4 a11 a12 a13 a14 a15 a16 a18 a19 a20",
}


def extend(lessons):
    for level, items in lessons.items():
        for item in items:
            item.setdefault("cefr", BANDS[level])
            item.setdefault("domain", "language_use")
            item.setdefault("objective", f'Apply {item["title"].lower()} in a meaningful context.')
            item.setdefault("references", [REFERENCES["cefr"], REFERENCES["grammar"]])
            item.setdefault("assessment", "Selected-response practice; productive tasks are self/teacher reviewed.")
            item.setdefault("tasks", {
                "writing": f'Create a short real-life example demonstrating {item["title"].lower()}. Explain your choices and revise one sentence.',
                "speaking": f'Explain your example of {item["title"].lower()} aloud to a partner and answer one follow-up question.',
                "self_check": "Check task completion, clarity, appropriate language and one possible improvement with a teacher or partner.",
            })
        items.extend(ADDITIONS[level])
        items.extend(SUPPLEMENT[level])
        by_id = {item["id"]: item for item in items}
        sequence = SEQUENCES[level].split()
        if set(sequence) != set(by_id) or len(sequence) != len(items):
            raise ValueError(f"Syllabus order is incomplete for {level}")
        items[:] = [by_id[key] for key in sequence]
