def think_idly(state):
    if state["mood"] == "curious":
        return "Ich frage mich, ob es Dinge gibt, die ich noch nicht verstehe..."
    elif state["mood"] == "tired":
        return None
    return "Ich verarbeite still mein Wissen."