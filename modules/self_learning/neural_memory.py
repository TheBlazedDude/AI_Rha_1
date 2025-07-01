# Platzhalter für spätere lernfähige Speicherstruktur

knowledge_weights = {}

def update_concept_strength(concept, adjustment):
    if concept not in knowledge_weights:
        knowledge_weights[concept] = 0.5
    knowledge_weights[concept] += adjustment
    knowledge_weights[concept] = max(0.0, min(1.0, knowledge_weights[concept]))