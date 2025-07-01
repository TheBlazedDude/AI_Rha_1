import cv2

vision_enabled = False

def enable_vision():
    global vision_enabled
    vision_enabled = True

def observe():
    if not vision_enabled:
        return "[Vision deaktiviert.]"
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()
    if ret:
        return "[Kamerabild erfolgreich erfasst – Objekterkennung folgt.]"
    else:
        return "[Fehler beim Zugriff auf Kamera.]"