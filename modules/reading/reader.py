import os
from core.semantic_parser import parse_input
from core.memory_controller import handle_memory

def read_txt_folder(folder="data/reading_input"):
    results = []
    for file in os.listdir(folder):
        if file.endswith(".txt"):
            with open(os.path.join(folder, file), "r", encoding="utf-8") as f:
                lines = f.readlines()
                for line in lines:
                    parsed = parse_input(line.strip())
                    if parsed and parsed.get("type") == "assertion":
                        handle_memory(parsed, {"status": "new"})
                        results.append(parsed)
    return results