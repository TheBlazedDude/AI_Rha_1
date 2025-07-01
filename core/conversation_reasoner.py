from core.dialog_memory import recall_definition, handle_identity
from core.question_interpreter import interpret_question

def process_question(text):
    intent = interpret_question(text)
    if intent["type"] == "definition":
        return recall_definition(intent["target"])
    elif intent["type"] == "identity":
        return handle_identity(intent["target"])
    elif intent["type"] == "reason":
        return "Ich kann dir Gründe nur nennen, wenn ich sie vorher gelernt habe."
    elif intent["type"] == "time":
        return "Ich besitze noch kein echtes Zeitgefühl."
    return "Diese Frageform kenne ich noch nicht."