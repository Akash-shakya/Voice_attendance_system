'''student voice attendance system using voice command and store the present and absent student name list into excel file'''
##import required library
import speech_recognition as sr 
from datetime import *
#import wikipedia
import pyttsx3
#import webbrowser
#import random
#import winsound
import os
import time
import pandas as pd
import xlsxwriter

##Read student csv file into python
df = pd.read_csv("C:\\Users\\Akash Shakya\\Desktop\\student.csv")
#print(df)
student = df.student.to_list()     #convert student name column into a list format
#print(student)

## voice command engine
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate+10)  ## Increase/decrease speed of voice
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male

#define function
def speak(audio):  
    engine.say(audio)
    engine.runAndWait()

def takecom():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning....")
        audio = r.listen(source)
    try:
        print("Recognising.") 
        text = r.recognize_google(audio,language='en-in')
        print(text)
    except Exception:                #For Error handling
        speak("error...")
        print("Network connection error") 
        return "none"
    return text

def wish():
    hour = int(datetime.now().hour)
    if hour >= 0 and hour<12:
        speak("Good morning Student, I am virtual assistent,please, Ready for your attendance")
    else:
        speak("Good Afternoon student, I am virtual assistent, please, Ready for your attendance")

wish()
### make a list of present and absent student
present_stu = []
absent_stu = []

##Calling Student Name one by one using for loop

#if __name__ == "__main__":
for x in range(len(student)):
    engine.say(student[x])
    engine.runAndWait()
    print(student[x])
   
   # while True: take answer from the student 
    query = takecom().lower()

    if "present" in query or "yes" in query or "yes mam" in query or "present Mam" in query or "Yes sir" in query or "present sir" in query:
        speak("You are present")
        present_stu.append(student[x])
        print("Present")
        print(present_stu)
        
    elif 'Absent' in query or "Not present" in query or "Nahin aaya" in query:
        speak("You are Absent")
        absent_stu.append(student[x])
        print("Absent")
        print(absent_stu)
        
    else:
        speak("You are Absent")
        absent_stu.append(student[x])
        print("Absent")
        print(absent_stu)

#### List of all present and absent student
print("Present Student : ",present_stu)
print("Absent Student : ",absent_stu)

### upload the data into excel file
workbook = xlsxwriter.Workbook('studentattendance.xlsx')
worksheet = workbook.add_worksheet()

my_data = {'present': present_stu,
           'absent': absent_stu}

col_num = 0

for key, value in my_data.items():
    worksheet.write(0, col_num, key)
    worksheet.write_column(1, col_num, value)
    col_num += 1

workbook.close()

