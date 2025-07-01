from core.knowledge_graph import check_contradiction, concept_exists

def reason_about(structured_input):
    if structured_input["type"] != "assertion":
        return {"status": "unclear", "message": "Ich verstehe das nicht."}

    subj = structured_input["subject"]
    obj = structured_input["object"]

    contradiction = check_contradiction(subj, obj)
    known = concept_exists(subj, obj)

    if contradiction:
        return {"status": "contradiction", "message": contradiction}
    elif known:
        return {"status": "known", "message": f"Ich wusste schon, dass {subj} ein {obj} ist."}
    else:
        return {"status": "new", "message": f"Heißt das, {subj} ist ein {obj}?"}