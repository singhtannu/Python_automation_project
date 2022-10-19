# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 21:20:34 2022

@author: Lenovo
"""

import pyttsx3
import speechRecognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
    
def wishme():
    hour = int(datetime.datetime.now().hour)
    """
    12:00 - noon
    1:00 pm- morning/ 13:00 - afternoon
    18:00 - evening
    """
    
    if hour >=0 and hour <=12:
        speak("Good Morning my dear friend")
    elif hour >=12 and hour <18:
        speak("Good Afternoon my dear friend")
    else:
        speak("Good Evening my dear friend")
    speak("Let me know how can I help you ? What are you looking for ?")
    
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening to you Tannu ......")
        r.pause_threshold = 1
        audio = r.listen(source)
        
        
    try:
        print("Recognizing your voice ......")
        query = r.recognize.google(audio, language='en-in')
        print(f"My dear friend you said: {query}\n")
        
        
    except Exception as e:
        print("Tannu say that again please ......")
        return query
    
    
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('tanmaysingh282@gmail.com','Singh@0033')
    server.sendmail('tanmaysingh282@gmail.com', to, content)
    server.close()
    


if __name__ == '__main__':
    wishme()
    
    while True:
        query = takecommand().lowwer()
        
        if'open wikipedia' in query:
            speak('Searching wikipedia .....')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
            
