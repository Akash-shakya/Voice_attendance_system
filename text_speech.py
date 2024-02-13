# import library
import speech_recognition as sr 
from datetime import *
import wikipedia
import pyttsx3
import webbrowser
import random
import winsound
import os
import time
"""VOICE"""
engine = pyttsx3.init()
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[1].id)  #changing index, changes voices. o for male

#text to speech
r = sr.Recognizer()
 
# Function to convert text to
# speech
def SpeakText(command):
     
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

#students name
engine.say("Akash shakya")
engine.runAndWait()

while():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning....")
        audio = r.listen(source)
    try:
        print("Recognising....") 
        text = r.recognize_google(audio,language='en-in')
        print(text)
    except Exception:                
        speak("sir please connect me with internet ")
        print("Network connection error") 
        return "none"
    return text
             
'''time.sleep(3)
engine.say("Muskan gupta")
engine.runAndWait()
time.sleep(3)
engine.say("Saurabh tiwari")
engine.runAndWait()
time.sleep(3)
engine.say("kartik bansal")
engine.runAndWait()
time.sleep(3)
engine.say("Amit ghosh")
engine.runAndWait()
time.sleep(3)
