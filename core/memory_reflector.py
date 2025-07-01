from core.conversation_tracker import conversation_log
from core.knowledge_graph import _load_knowledge, concept_exists

def reflect_and_learn():
    knowledge = _load_knowledge()
    new_links = []
    for turn in conversation_log[-10:]:
        parsed = turn.get("parsed")
        if parsed and parsed.get("type") == "assertion":
            subj = parsed["subject"]
            obj = parsed["object"]
            if not concept_exists(subj, obj):
                new_links.append((subj, obj))
    return new_links