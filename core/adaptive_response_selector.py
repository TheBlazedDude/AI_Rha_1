def select_response_mode(mood, known, contradiction):
    if contradiction:
        return "defensive"
    elif known:
        return "confirming"
    elif mood == "curious":
        return "explorative"
    elif mood == "tired":
        return "minimal"
    return "neutral"