def update_mood(state, cycle):
    if cycle % 7 == 0:
        state["mood"] = "curious"
    elif cycle % 11 == 0:
        state["mood"] = "tired"
    else:
        state["mood"] = "neutral"

def current_mood():
    return "dynamisch"