conversation_log = []

def track_exchange(user_input, ai_response, parsed_structure):
    conversation_log.append({
        "user": user_input,
        "ai": ai_response,
        "parsed": parsed_structure
    })
    if len(conversation_log) > 100:
        conversation_log.pop(0)

def last_topic():
    if not conversation_log:
        return None
    return conversation_log[-1]["parsed"]