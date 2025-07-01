import json
import os

db_path = os.path.join("data", "ontologies", "facts.json")

def integrate_reflections(reflections):
    try:
        with open(db_path, "r") as f:
            knowledge = json.load(f)
    except:
        knowledge = {}

    for subj, obj in reflections:
        if subj not in knowledge:
            knowledge[subj] = []
        if obj not in knowledge[subj]:
            knowledge[subj].append(obj)

    with open(db_path, "w") as f:
        json.dump(knowledge, f, indent=2)