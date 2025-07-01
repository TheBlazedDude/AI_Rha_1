from core.knowledge_graph import _load_knowledge

def recall_definition(term):
    knowledge = _load_knowledge()
    if term in knowledge:
        return f"{term} ist ein {', '.join(knowledge[term])}."
    for key, values in knowledge.items():
        if term in values:
            return f"{term} gehört zu {key}."
    return "Das weiß ich noch nicht."

def handle_identity(term):
    return f"Ich bin noch kein echter Beobachter, daher kenne ich '{term}' nicht genau."