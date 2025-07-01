from core.knowledge_graph import _load_knowledge

def generate_self_questions():
    questions = []
    data = _load_knowledge()
    for subject, objs in data.items():
        if "Ding" in objs and len(objs) == 1:
            questions.append(f"Was genau ist ein {subject}?")
        if len(objs) > 2:
            questions.append(f"Gibt es einen Oberbegriff für {subject}?")
    return questions[:5]