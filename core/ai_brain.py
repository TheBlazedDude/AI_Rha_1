from core.semantic_parser import parse_input
from core.reasoning_engine import reason_about
from core.memory_controller import handle_memory
from interface.output_generator import generate_output

def process_input(user_input):
    structured = parse_input(user_input)
    reasoning = reason_about(structured)
    handle_memory(structured, reasoning)
    return generate_output(reasoning)