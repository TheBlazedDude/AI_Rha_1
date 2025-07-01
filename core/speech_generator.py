def generate_response(reasoning, context=None):
    if reasoning.get("status") == "contradiction":
        return f"⚠️ Widerspruch erkannt: {reasoning['message']}"
    elif reasoning.get("status") == "known":
        return f"✔️ Das wusste ich bereits: {reasoning['message']}"
    elif reasoning.get("status") == "new":
        return f"❓ {reasoning['message']}"
    elif reasoning.get("status") == "clarified":
        return f"💡 Danke für die Erklärung: {reasoning['message']}"
    return reasoning.get("message", "🤖 Ich weiß nicht, was ich sagen soll.")