from config import CASUAL_SALUTATION, URGENCY_WORDS
import re


def punctuation_risk(text):
    score = 0
    if "!!!" in text or "???" in text:
        score += 8
    if text.count("!") > 3:
        score += 5
    return score


def capitalization_risk(text):
    words = text.split()
    if not words:
        return 0

    caps = [w for w in words if len(w) > 2 and w.isupper()]
    ratio = len(caps) / len(words)

    if ratio > 0.1:
        return 10
    elif ratio > 0.05:
        return 5
    return 0


def wording_risk(text):
    score = 0
    text_lower = text.lower()

    for word in CASUAL_SALUTATION:
        if re.search(rf"\b{word}\b", text_lower):
            score += 3

    for word in URGENCY_WORDS:
        if re.search(rf"\b{word}\b", text_lower):
            score += 5

    return score


def phishing_phrase_risk(text):
    score = 0
    text_lower = text.lower()

    patterns = [
        "verify your account",
        "click below",
        "login immediately",
        "account suspended",
        "update your information",
        "confirm your identity",
        "unauthorized login",
        "security alert",
        "act now",
    ]

    for phrase in patterns:
        if phrase in text_lower:
            score += 10

    return score


def suspicious_structure_risk(text):
    score = 0

    if text.lower().count("click") > 1:
        score += 5

    if len(text.split()) < 20:
        score += 5

    return score


def language_risk_score(text):
    return (
        punctuation_risk(text)
        + capitalization_risk(text)
        + wording_risk(text)
        + phishing_phrase_risk(text)
        + suspicious_structure_risk(text)
    )
