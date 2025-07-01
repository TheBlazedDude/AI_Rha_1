def interpret_question(text):
    lowered = text.lower()
    if lowered.startswith("was ist"):
        return {"type": "definition", "target": lowered.replace("was ist", "").strip(" ?")}
    elif lowered.startswith("wer ist"):
        return {"type": "identity", "target": lowered.replace("wer ist", "").strip(" ?")}
    elif lowered.startswith("warum"):
        return {"type": "reason", "target": lowered.replace("warum", "").strip(" ?")}
    elif lowered.startswith("wann"):
        return {"type": "time", "target": lowered.replace("wann", "").strip(" ?")}
    return {"type": "unknown", "raw": text}