from core.memory_reflector import reflect_and_learn
from core.graph_integrator import integrate_reflections

def optimize_knowledge():
    reflections = reflect_and_learn()
    if reflections:
        integrate_reflections(reflections)
        return f"{len(reflections)} neue Konzepte dauerhaft gespeichert."
    return "Keine neuen Konzepte zur Integration erkannt."