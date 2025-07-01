import pyttsx3

tts_enabled = False
engine = pyttsx3.init()

def enable_tts():
    global tts_enabled
    tts_enabled = True

def speak(text):
    if not tts_enabled:
        return
    engine.say(text)
    engine.runAndWait()