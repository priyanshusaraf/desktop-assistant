import os
import pyaudio
import pyttsx3
import datetime
import wikipedia 
import speech_recognition as sr
from selenium import webdriver

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def take_command():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")

        r.pause_threshold = 1
        r.energy_threshold = 400

        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio, language="en-in")
            print(said)
        
        except Exception as e:
            print(e)
            
    return said

def greet():
    
    hour = int(datetime.datetime.now().hour)

    if hour <= 12:
        speak("Good Morning!")
    if hour > 12 and hour < 17:
        speak("Good afternoon!")
    else:
        speak("Good evening")

if __name__ == "__main__":
    greet()

    #execute tasks 
    on = True
    while on:
        query = take_command().lower()

        if 'wikipedia' in query:
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences = 3)
            speak("According to wikipedia, ")
            print(result)
            speak(result)

        elif "open youtube" in query:
            speak("Opening Youtube")
            chrome = webdriver.Chrome()
            chrome.get("https://www.youtube.com")

        elif "open google" in query:
            speak("Opening google")
            chrome = webdriver.Chrome()
            chrome.get("https://www.google.com")

        elif "open stackoverflow" in query:
            speak("opening stack overflow")
            chrome = webdriver.Chrome()
            chrome.get("https://www.stackoverflow.com")
        
        elif "open instagram" in query:
            speak("Opening instagram")
            chrome = webdriver.Chrome()
            chrome.get("https://www.instagram.com")
        
        elif query == "exit":
            on = False

        elif "hello" in query:
            speak("Welcome")

        elif "open python documentation" in query:
            speak("okay, here is python documentation")
            chrome = webdriver.Chrome()    
            chrome.get("docs.python.org")

        elif "who are you" in query:
            speak("I am priyanshu's desktop assistant, pri")

        elif "the time" in query:
            str_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak("The current time is: " + str_time)
        
        elif "open vs code" or "open visual studio code" or "open code" in query:
            vscode = "C:\\Users\\USER\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vscode)

        elif "open teams" in query:
            msteams = "C:\\Users\\USER\\AppData\\Local\\Microsoft\\Teams"
            os.startfile(msteams)
        else:
            speak("I dont know the answer to that question. Please try something else")

