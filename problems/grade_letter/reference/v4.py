def grade(score):
    if score is None or not 0 <= score <= 100:
        raise ValueError(f"score must be in [0, 100], got {score!r}")
    score = int(score + 0.5)  # round half UP (scores are non-negative)
    if score >= 90:
        return "A" if score >= 93 else "A-"
    for letter, lo in (("B", 80), ("C", 70), ("D", 60)):
        if score >= lo:
            if score >= lo + 7:
                return letter + "+"
            if score < lo + 3:
                return letter + "-"
            return letter
    return "F"
