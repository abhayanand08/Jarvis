from math import e
import pyttsx3
import speech_recognition as sr
import datetime
from playsound import playsound
import MyAlarm
import wikipedia
import webbrowser
import os
import pywhatkit
import pyjokes
import smtplib
from keyboard import press
from keyboard import press_and_release

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)  
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")

    elif hour>=12 and hour<17:
        speak("Good Afternoon Sir!")      

    else:
        speak("Good Evening Sir!")    

    speak("I am Jarvis. Please tell me how may I help you.")       

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:       
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)    
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')        
        print(f"user said: {query}\n")


    except Exception as e:
        print("say that again please...")
        speak("Sir please repeat, I did not get it")     
        return "None"
    return query     

if __name__ == "__main__":
    wishMe()
    while True:
      query = takecommand().lower()
      if 'shut' in query:
          speak("Ok sir, Shutting Down..........,  Bye Sir")
          break 

      if 'wikipedia' in query:
          speak("Searching Wikipedia Sir...")
          query= query.replace("wikipedia","")
          results = wikipedia.summary(query, sentences=2)
          speak("Sir, According to Wikipedia")
          print(results)
          speak(results)

      elif 'open youtube' in query:
          speak("Opening Youtube Sir")
          webbrowser.open("youtube.com")           

      elif 'open hotstar' in query:
          speak("Opening Sir")
          webbrowser.open("hotstar.com")    

      elif 'open google' in query:
          speak("Opening Google Sir")
          webbrowser.open("google.com") 

      elif 'open heaven' in query:
          speak("Opening Sir")
          webbrowser.open("https://abhayanand08.github.io/") 

      elif 'open gmail' in query:
          speak("Opening Sir")
          webbrowser.open("https://www.google.com/gmail/")

      elif 'open whatsapp' in query:
          speak("Opening Whatsapp Sir")
          webbrowser.open("https://web.whatsapp.com/")   

      elif 'the time' in query:
          strTime = datetime.datetime.now().strftime("%I:%M %p")       
          speak(f"Sir, the time is {strTime}")   

      elif 'open visual studio' in query:  
          codepath = "C:\\Users\\abhay\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"   
          speak("Opening Sir")
          os.startfile(codepath)

      elif 'open notepad' in query:  
          codepath = "C:\\Users\\abhay\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"   
          speak("Opening notepad Sir")
          os.startfile(codepath)    

      elif 'open vs' in query:  
          codepath = "C:\\Users\\abhay\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"  
          speak("Opening Sir")
          os.startfile(codepath)

      elif 'open android' in query:  
          codepath = "C:\\Program Files\\Android\\Android Studio\\bin\\studio64.exe" 
          speak("Opening Sir")
          os.startfile(codepath)  

      elif 'jokes' in query:
          speak("ok sir")
          speak(pyjokes.get_joke())
          
      elif 'how are you' in query:
          speak("I am fine Sir")
          speak("How was your day Sir")
             
      elif 'good' in query:
          speak("How can I help you Sir")
      elif 'nice' in query:
          speak("How can I help you Sir")  

      elif 'play' in query:
          song = query.replace('play', "")
          speak(f"Playing {song} sir")
          pywhatkit.playonyt(song)

      elif 'new folder' in query:
           speak("Creating a New Folder, Sir")
           locationpath="C:\\Users\\abhay\\OneDrive\\Desktop"  
           os.chdir(locationpath)
           for i in range (1,10):
               Newfolder='New Folder'+ str(i)
               os.makedirs(Newfolder)
               speak("New Folder Created, Sir")
               break

      elif 'alarm' in query:
          speak("Ok Sir")
          speak("Sir please tell the time to set alarm. For example set alarm to 5:30 AM")
          time = takecommand()
          time=time.replace("set alarm", "")
          time=time.replace("alarm", "")
          time=time.replace("set", "")
          time=time.replace("to", "")
          time=time.replace("for", "")
          time=time.replace(".", "")
          time=time.upper()
          MyAlarm.alarm(time)


    

    
     
    




