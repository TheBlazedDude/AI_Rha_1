def reflect_on_last_cycles(log_path="logs/cognitive_trace.log"):
    try:
        with open(log_path, "r") as f:
            lines = f.readlines()[-10:]
        return "Ich habe nachgedacht über:\n" + "".join(lines)
    except:
        return "Ich erinnere mich an nichts."