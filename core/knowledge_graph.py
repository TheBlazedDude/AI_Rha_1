import os
import json

db_path = os.path.join("data", "ontologies", "facts.json")

def _load_knowledge():
    if not os.path.exists(db_path):
        return {}
    with open(db_path, "r") as f:
        return json.load(f)

def concept_exists(subj, obj):
    data = _load_knowledge()
    return subj in data and obj in data[subj]

def check_contradiction(subj, obj):
    # Beispielregel: Ein Subjekt kann nicht gleichzeitig "Mensch" und "Maschine" sein
    contradiction_pairs = [("Mensch", "Maschine"), ("Tier", "Pflanze")]
    data = _load_knowledge()
    if subj in data:
        for existing_obj in data[subj]:
            if (existing_obj, obj) in contradiction_pairs or (obj, existing_obj) in contradiction_pairs:
                return f"Widerspruch: {subj} kann nicht gleichzeitig {existing_obj} und {obj} sein."
    return None