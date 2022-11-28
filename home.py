# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 18:52:44 2020

@author: user
"""

import pyttsx3
import datetime
import speech_recognition as sr
import pywhatkit
import wikipedia
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def time():
    time=datetime.datetime.now().strftime('%I:%M:%S')
    speak(time)
#speak('this is jarvis')

def date():
    year=int(datetime.datetime.now().year)
    month=int(datetime.datetime.now().month)
    date=int(datetime.datetime.now().day)
    speak(date)
    speak(month)
    speak(year)
def wishme():
    speak('hello shifna maji ')
   
    
    speak('majii at you service please tell me how can i help you')
    hour=datetime.datetime.now().hour
    if hour>=6 and hour<12:
        speak('good morning')
    elif hour>=12 and hour<18:
        speak('good afternoon')
    elif hour>=18 and hour<24:
        speak('good evening')
    else:
        speak('good night')
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('listening')
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        
        command=r.recognize_google(audio)
        print(command)
        
    except:
        pass
    return command
wishme()
def run_alexa():
    command = takecommand()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        speak('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
         speak('shifna maji the current time is')
         time()
    elif 'date' in command:
        speak(' current date is')
        date()
    elif 'are you single' in command:
        speak('I am in a relationship with shefu')
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        speak(info)
    else:
        speak('Please say the command again.')

while True:
    run_alexa()

        

    
        
        
    
