user_profile = {
    "name": None,
    "preferred_style": "neutral"
}

def set_user_name(name):
    user_profile["name"] = name

def get_user_name():
    return user_profile["name"] or "Freund"