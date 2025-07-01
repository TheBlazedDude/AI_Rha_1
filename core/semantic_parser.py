def parse_input(user_input):
    # Primitive semantische Zerlegung (Struktur: Subjekt-Prädikat-Objekt)
    if " ist ein " in user_input:
        subj, obj = user_input.split(" ist ein ")
        pred = "ist_ein"
    elif " ist eine " in user_input:
        subj, obj = user_input.split(" ist eine ")
        pred = "ist_eine"
    elif " ist " in user_input:
        subj, obj = user_input.split(" ist ")
        pred = "ist"
    else:
        return {"type": "unknown", "raw": user_input}
    return {
        "type": "assertion",
        "subject": subj.strip(),
        "predicate": pred,
        "object": obj.strip()
    }