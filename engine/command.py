import pyttsx3
import speech_recognition as sr
import eel
import time
import datetime
import wikipedia
import smtplib
import pyjokes
from requests import get
import os
import requests
from bs4 import BeautifulSoup
import webbrowser
import re
import mixer
from gtts import gTTS
import googletrans
from googletrans import Translator
import json
from plyer import notification

# import alarm

current_time = datetime.datetime.now()

def parse_time_query(query):
    # Patterns to identify different time intervals
    patterns = {
        "half an hour": 30,
        "one hour": 60,
        "two hours": 120,
        "three hours": 180,
        "one minute": 1,
        "five minutes": 5,
        "ten minutes": 10,
        "fifteen minutes": 15,
        "thirty minutes": 30,
    }
    
    for pattern, minutes in patterns.items():
        if re.search(pattern, query, re.IGNORECASE):
            return minutes
    return None

def latestnews():
    api_dict = {"business" : "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=#here paste your api key",
            "entertainment" : "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=#here paste your api key",
            "health" : "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=#here paste your api key",
            "science" :"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=#here paste your api key",
            "sports" :"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=#here paste your api key",
            "technology" :"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=#here paste your api key"
        }

    content = None
    url = None
    speak("Which field news do you want, [business] , [health] , [technology], [sports] , [entertainment] , [science]")
    field = takecommand()
    for key ,value in api_dict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print("url was found")
            break
        else:
            url = True
    if url is True:
        print("url not found")

    news = requests.get(url).text
    news = json.loads(news)
    speak("Here is the first news.")

    arts = news["articles"]
    for articles in arts :
        article = articles["title"]
        print(article)
        speak(article)
        news_url = articles["url"]
        print(f"for more info visit: {news_url}")

        a = input("[press 1 to cont] and [press 2 to stop]")
        if str(a) == "1":
            pass
        elif str(a) == "2":
            break
        
    speak("thats all")

def speak(text):
    eel.DisplayMessage("")
    text = str(text)
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.setProperty('rate',174)
    # print(voices)
    eel.DisplayMessage(text)
    engine.say(text)
    eel.receiverText(text)
    engine.runAndWait()
    
def speak1(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.setProperty('rate',174)
    # print(voices)
    eel.DisplayMessage("Hey Bujji here, For Your Service")
    engine.say(text)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        eel.DisplayMessage("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source,15,3)
    try:
        print("Recognizing...")
        eel.DisplayMessage("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        eel.DisplayMessage(query)
        time.sleep(2)
        # speak(query)
        # eel.ShowHome()
    except Exception as e:
        return ""
    return query.lower()

@eel.expose
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12 :
        speak("Good Morning Dear")
    elif hour > 12 and hour<18:
        speak("Good Afternoon Dear")
    else:
        speak("Good Evening Dear")
    speak1("Hey Buji here, For Your Service")
    
@eel.expose
def wish1():
    speak1("What can I do for you?")
    
    
@eel.expose
def allCommands(message = 1):
    
    if message==1:
        query = takecommand()
        # print(query)
        query = query.lower().strip()
        eel.DisplayMessage(query)
        eel.senderText(query)
    else:
        query = message
        query = query.lower().strip()
        eel.DisplayMessage(query)
        eel.senderText(query)
    try:
        # query = takecommand()
        
        q1 = query.lower().strip()
        print("query",query)
        print("q1",q1)
        
        if "open google" in q1:
            speak("Hey , what to search on google")
            cm = takecommand().lower().strip()
            webbrowser.open(f"https://www.google.com/search?q={cm}")
            
        # elif "set alarm" in q1 or "set an alarm" in q1:
        #     speak("What time do you want to set alarm")
        #     tm = takecommand().lower().strip()
        #     tm = tm.replace("set alarm for ","")
        #     tm = tm.replace("set an alarm for ","")
        #     tm = tm.replace("set alarm at ","")
        #     tm = tm.replace("set an alarm at ","")
        #     tm = tm.replace("o clock","")
        #     tm = tm.replace("o'clock","")
        #     tm = tm.replace(" ","")
        #     alarm(tm)
        #     speak("Done")
            
            
        # elif "temperature" or "weather" in q1:
        #     # search = takecommand()
        #     url = f"https://www.google.com/search?q={q1}"
        #     r = requests.get(url)
        #     data = BeautifulSoup(r.text,"html.parser")
        #     temp = data.find("div",class_ = "BNeawe").text
        #     speak(f"currently it is {temp}")
                
        elif "open" in query:
            from engine.features import openCommand
            openCommand(query)
        
        # elif "email to amma" or "email to nanna" in q1:
        #     try :
        #         speak("What should I say?")
        #         content = takecommand().lower().strip()
        #         to = "ab.grsyg@gmail.com"
        #         from engine.helper import sendEmail
        #         sendEmail(to,content)
        #         speak("Email has been sent!")
        #     except Exception as e:
        #         print(e)
        
        # elif "temperature" or "weather" in q1:
        #     # search = takecommand()
        #     url = f"https://www.google.com/search?q={q1}"
        #     r = requests.get(url)
        #     data = BeautifulSoup(r.text,"html.parser")
        #     temp = data.find("div",class_ = "BNeawe").text
        #     speak(f"currently it is {temp}")
        
        elif "temperature" in query:
            k = query
            url = f"https://www.google.com/search?q={k}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_ = "BNeawe").text
            speak(f"currently it is {temp}")
            
        elif "weather" in query:
            k = query
            url = f"https://www.google.com/search?q={k}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_ = "BNeawe").text
            speak(f"currently it is {temp}")
            
        elif "hello" in query:
            speak("Hello , how are you?")
            
        elif "thank you" in query:
            speak("You're welcome")
            
        elif "news" in query:
            # from NewsRead import latestnews
            latestnews()
            
        elif "schedule my day" in query:
            tasks = [] # Empty list 
            speak("Do you want to clear old tasks? Please say YES or NO.")
            query = takecommand().lower()
            if "yes" in query:
                with open("tasks.txt", "w") as file:
                    file.write("")  # Clearing old tasks
                speak("How many tasks do you want to schedule?")
                no_tasks = int(takecommand())
                for i in range(no_tasks):
                    speak(f"Please tell me task number {i + 1}.")
                    task = takecommand()
                    tasks.append(task)
                    with open("tasks.txt", "a") as file:
                        file.write(f"{i}. {task}\n")
            elif "no" in query:
                speak("How many tasks do you want to schedule?")
                no_tasks = int(takecommand())
                for i in range(no_tasks):
                    speak(f"Please tell me task number {i + 1}.")
                    task = takecommand()
                    tasks.append(task)
                    with open("tasks.txt", "a") as file:
                        file.write(f"{i}. {task}\n")

          
        elif "show my schedule" in query:
            file = open("tasks.txt","r")
            content = file.read()
            file.close()
            mixer.init()
            mixer.music.load("start_sound.mp3")
            mixer.music.play()
            notification.notify(
                title = "My schedule :-",
                message = content,
                timeout = 15
                )  
            
        elif "wikipedia" in q1:
            try:
                speak("searching wikipedia.....")
                search_query = query.replace("wikipedia", "").strip()
                print("search_query:", search_query)
                results = wikipedia.summary(search_query, sentences=4)
                speak("according to wikipedia")
                speak(results)
                print(results)
            except wikipedia.exceptions.DisambiguationError as e:
                speak("The query is too ambiguous, please be more specific.")
                print(f"DisambiguationError: {e}")
            except wikipedia.exceptions.PageError as e:
                speak("The page does not exist on Wikipedia.")
                print(f"PageError: {e}")
            except Exception as e:
                speak("An error occurred while searching Wikipedia.")
                print(f"Exception: {e}")
                
        elif "my ip address" in q1:
            ip = get("https://api.ipify.org").text
            speak(f"Your IP address is {ip}")
            
        elif "screenshot" in query:
            import pyautogui 
            im = pyautogui.screenshot()
            im.save("ss.jpg")    
        
        elif "translate" in query:
                from googletrans.Translator import translategl
                query = query.replace("jarvis","")
                query = query.replace("alexa","")
                query = query.replace("bujji","")
                query = query.replace("translate","")
                translategl(query)
        
        elif "on youtube" in query:
            from engine.features import PlayYoutube
            PlayYoutube(query)
            
        elif "in youtube" in query:
            from engine.features import PlayYoutube
            PlayYoutube(query)
            
        elif "present time" in query or "current time" in query:
            strTime = current_time.strftime("%H:%M")
            speak(f"The present time is {strTime}")
            
        elif "send message" in query or "phone call" in query or "video call" in query :
            from engine.features import findContact , whatsApp
            message = ""
            contact_no , name = findContact(query)
            if(contact_no!=0):
                if "send message" in query :
                    message = 'message'
                    speak("what message to send")
                    query = takecommand().strip()
                
                elif "phone call" in query:
                    message = 'call'
                else:
                    message = 'video call'
                whatsApp(contact_no , query , message , name)       
            else:
                print("not run")
                speak("Sorry at this point of time")  
                
        elif "close notepad" in query:
            speak("Okay , Closing notepad")
            os.system("taskkill /f /im notepad.exe")
            

            
        # elif "set alarm" in query:
        #     nn = int(datetime.datetime.now().hour)
        #     if nn==22:
        #         music_dir = 'C:\\Users\\HP\\Music'
        #         songs = os.listdir(music_dir)
        #         os.startfile(os.path.join(music_dir, songs[0]))
        
        elif "tell me a joke" in query:
            joke = pyjokes.get_joke(language="en", category="all")
            speak(joke)
        else:
            from engine.features import chatBot
            chatBot(query)
            
    except:
        speak("Sorry for you at this point of time")
        print("error")
    eel.ShowHome()
# text = takecommand()
# speak(text)

