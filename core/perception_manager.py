def sense_environment(modules):
    results = []
    for mod in modules:
        try:
            data = mod.observe()
            results.append(data)
        except Exception as e:
            results.append(f"Error sensing from {mod.__name__}: {e}")
    return results