import speech_recognition as sr 
from datetime import *
import wikipedia
import pyttsx3
import webbrowser
import random
import winsound
import os
import time
import pandas as pd

##Read student csv file into python
df = pd.read_csv("C:\\Users\\Akash Shakya\\Desktop\\student.csv")
#print(df)
student = df.student.to_list()     #convert student name column into a list format
#print(student)

"""VOICE"""
engine = pyttsx3.init()
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male

def speak(audio):  
    engine.say(audio)
    engine.runAndWait()
def wish():
    hour = int(datetime.now().hour)
    if hour >= 0 and hour<12:
        speak("Good morning Student, I am virtual assistent,please, Ready for your attendance")
    else:
        speak("Good Afternoon student, I am virtual assistent, please, Ready for your attendance")

wish()

'''Calling Student Name one by one using for loop'''
for x in range(len(student)):
    engine.say(student[x])
    engine.runAndWait()
    time.sleep(2)

