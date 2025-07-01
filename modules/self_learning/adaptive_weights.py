# Simuliert Gewichtsanpassungen bei Rückmeldung

feedback_log = {}

def adjust_by_feedback(concept, score):
    if concept not in feedback_log:
        feedback_log[concept] = []
    feedback_log[concept].append(score)