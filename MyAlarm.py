import datetime
from playsound import playsound
import pyttsx3


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def alarm(Timing):
    altime = str(datetime.datetime.now().strptime(Timing," %I:%M %p"))

    altime = altime[11:-3]
    print(altime)
    Horeal = altime[:2]
    Horeal = int(Horeal)
    Mireal = altime[3:5]
    Mireal = int(Mireal)
    speak(f"Sir! Alarm is set for {Timing}")

    while True:
        if Horeal==datetime.datetime.now().hour:
            if Mireal==datetime.datetime.now().minute:
                print("alarm is running")
                speak(f"Wake up sir its {Timing}")
                audio="C:\\Users\\abhay\\OneDrive\\Desktop\\Jarvis\\iron.mp3"
                playsound(audio)
                break
   
    
if __name__ == '__main__':
    alarm(' 5:10 PM')    