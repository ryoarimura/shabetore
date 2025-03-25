import pyttsx3


def text_to_speech(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 200)
    engine.setProperty("volume", 1.0)

    engine.say(text)
    engine.runAndWait()
