from memory.long_term import save_fact
from memory.short_term import remember_temporarily

def handle_memory(structured_input, reasoning_result):
    if reasoning_result["status"] == "new":
        remember_temporarily(structured_input)
    elif reasoning_result["status"] == "@true":
        save_fact(structured_input["subject"], structured_input["predicate"], structured_input["object"])