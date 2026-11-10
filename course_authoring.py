"""Compact authoring format for original, independently written course content."""

REFERENCES = {
    "cefr": "https://www.coe.int/en/web/common-european-framework-reference-languages/cefr-descriptors",
    "grammar": "https://learnenglish.britishcouncil.org/free-resources/grammar",
    "advanced_grammar": "https://learnenglish.britishcouncil.org/free-resources/grammar/c1",
    "profile": "https://englishprofile.org/?menu=egp-online",
    "c2": "https://www.cambridgeenglish.org/exams-and-tests/qualifications/proficiency/format/",
}


def unit(id, title, band, domain, goal, text, remedial, questions, task):
    """Each row is authored: prompt | 3 options | answer index | rationale."""
    bank = []
    for row in questions.strip().splitlines():
        fields = [field.strip() for field in row.split("|")]
        if len(fields) != 6:
            raise ValueError(f"Invalid question row in {id}")
        prompt, a, b, c, correct, explanation = fields
        bank.append(dict(prompt=prompt, options=[a, b, c], correct=int(correct), explanation=explanation))
    if len(bank) != 7:
        raise ValueError(f"Expected seven distinct authored questions in {id}")
    refs = ["cefr", "c2" if band == "C2" else "advanced_grammar" if band == "C1" else "grammar"]
    return dict(id=id, title=title, cefr=band, domain=domain, objective=goal,
                text=text, remedial=remedial, questions=bank,
                tasks={"writing": task,
                       "speaking": f"Explain your response to this task aloud, then ask a partner one follow-up question: {task}",
                       "self_check": "Check: Did I answer the task? Is my meaning clear? Are the forms and vocabulary appropriate? Can I correct one weakness?"},
                references=[REFERENCES[key] for key in refs],
                assessment="Selected-response practice; productive tasks are self/teacher reviewed.")
