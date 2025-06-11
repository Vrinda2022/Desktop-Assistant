import pyttsx3 # pip install pyttsx3
import speech_recognition as sr # pip install speechRecognition
import datetime
import wikipedia # pip install wikipedia
import webbrowser
import os
from pywikihow import search_wikihow
import requests
from bs4 import BeautifulSoup
import pyautogui
import MyAlarm

engine = pyttsx3.init('sapi5') # Microsoft Speech API (SAPI5) is the technology for voice recognition and synthesis provided by Microsoft.
voices = engine.getProperty('voices') # print(voices[1].id) #female voice - 1 male voice - 0
engine.setProperty('voice', voices[2].id) # Sets the voice of the ai
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis. Please tell me how may I help you")

def takeCommand():
    '''It takes microphone input from the user and returns string as output
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"    
    return query   


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print("According to Wikipedia...\n")
            print(results)
            speak(results)

        elif 'open youtube' in query :
            speak("Opening youtube.com")
            webbrowser.open("youtube.com")

        elif 'open google' in query :
            speak("What would you like to search")
            cm = takeCommand()
            print(cm)
            webbrowser.open(f"{cm}")
        
        elif 'open stackoverflow' in query :
            speak("Opening stackoverflow.com")
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query :
            music_dir = 'D:\\SONGS'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query :
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"The time is {strTime}")

        elif 'open vs code' in query :
            speak("Opening visual studio")
            codePath = "C:\\Users\\saksh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"  
            os.startfile(codePath)

        elif 'activate how to do mode' in query : 
            speak("Activated how to do mode, please tell me what would you like to learn")
            query = takeCommand()
            try:
                if 'exit' in query or 'close' in query:
                    speak("Deactivating how to do mode")
                else:
                    max_result = 1
                    how_to = search_wikihow(query, max_result)
                    assert len(how_to) == 1
                    how_to[0].print()
                    speak(how_to[0].summary)
            except Exception as e:
                speak("Sorry, I was not able to find any result for your query")
        
        elif 'weather forecast' in query :
            url = f"https://www.google.com/search?q={query}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"its currently{temp} in your area")

        elif 'alarm' in query :
            speak("Alright what should be the time for the alarm. for example, set alarm to 6:00 a.m.")
            alarm_time = takeCommand()
            alarm_time = alarm_time.replace("set alarm to ", "")
            alarm_time = alarm_time.replace(".", "")
            MyAlarm.alarm(alarm_time)

        elif 'volume up' in query :
            pyautogui.press("volumeup")

        elif 'volume down' in query :
            pyautogui.press("volumedown")

        elif 'mute' in query :
            pyautogui.press("volumemute")

        elif 'stop' in query:
            break
print("Have a good day\nClosing system...")
speak("Have a good day, closing system")