import pyttsx3

engine =pyttsx3.init()
TEXT=input("Enter Text: ")
engine.say(TEXT)
engine.runAndWait()
