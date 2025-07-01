import os
import json

db_path = os.path.join("data", "ontologies", "facts.json")

def save_fact(subj, pred, obj):
    if not os.path.exists(db_path):
        knowledge = {}
    else:
        with open(db_path, "r") as f:
            knowledge = json.load(f)

    if subj not in knowledge:
        knowledge[subj] = []
    if obj not in knowledge[subj]:
        knowledge[subj].append(obj)

    with open(db_path, "w") as f:
        json.dump(knowledge, f, indent=2)