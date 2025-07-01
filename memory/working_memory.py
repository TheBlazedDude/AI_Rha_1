# Temporärer Speicher für laufende Schlussfolgerungen

working_memory = {}

def add_to_working_memory(key, value):
    working_memory[key] = value

def get_from_working_memory(key):
    return working_memory.get(key)