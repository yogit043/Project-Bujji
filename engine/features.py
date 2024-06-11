import os
from pipes import quote
import re
import sqlite3
import struct
import subprocess
import time
import webbrowser
from playsound import playsound
import eel
import pyaudio
import pyautogui
from engine.command import speak
from engine.config import ASSISTANT_NAME
# Playing assiatnt sound function
import pywhatkit as kit
import smtplib
import pvporcupine
from engine.helper import extract_yt_term
from hugchat import hugchat
import cv2
from requests import get
from engine.helper import remove_words
from hugchat import hugchat

con = sqlite3.connect("bujji.db")
cursor = con.cursor()


@eel.expose
def playAssistantSound():
    music_dir = "D:/vit/Project Bujji/www/assets/audio/start_sound.mp3"
    playsound(music_dir)
        
def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query = query.lower().strip()

    app_name = query.strip()
    if app_name != "":
        # try:
        #     cursor.execute('SELECT path FROM sys_command WHERE name = ?', (app_name,))
        #     results = cursor.fetchall()
            
        #     if len(results) != 0:  # Corrected here
        #         speak("Opening " + query)
        #         os.startfile(results[0][0])
                
        #     else:
        #         cursor.execute('SELECT url FROM web_command WHERE name = ?', (app_name,))
        #         results = cursor.fetchall()
                
        #         if len(results) != 0:  # Corrected here
        #             speak("Opening " + query)
        #             webbrowser.open(results[0][0])
        if app_name == "command prompt":
            speak("Opening "+query)
            os.system("start cmd")
        elif app_name == "camera":
            speak("Opening "+query)
            cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
            while True:
                ret, img = cap.read()
                if ret:
                    cv2.imshow('webcam', img)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
            cap.release()
            cv2.destroyAllWindows()
        else:
            try:
                cursor.execute(
                    'SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
                results = cursor.fetchall()

                if len(results) != 0:
                    speak("Opening "+query)
                    os.startfile(results[0][0])

                elif len(results) == 0: 
                    cursor.execute(
                    'SELECT url FROM web_command WHERE name IN (?)', (app_name,))
                    results = cursor.fetchall()
                    
                    if len(results) != 0:
                        speak("Opening "+query)
                        webbrowser.open(results[0][0])
                    else:
                        speak("Opening " + query)
                        try:
                            os.system('start ' + query)
                        except Exception as e:  # More specific error handling
                            speak("Not Found")
                            print(f"Error: {e}")
            except Exception as e:  # More specific error handling
                speak("Something went wrong")
                print(f"Error: {e}")
    else:
        speak("Sorry, I didn't understand what you want me to open")
    # if query!="":
    #     speak("Opening "+query)
    #     os.system('start '+query)
    # else :
    #     speak("Sorry, I didn't understand what you want me to open")
        

def PlayYoutube(query):
    search_term = extract_yt_term(query)
    speak("Playing "+search_term+" on YouTube")
    kit.playonyt(search_term)

def hotword():
    porcupine=None
    paud=None
    audio_stream=None
    try:
       
        # pre trained keywords    
        porcupine=pvporcupine.create(keywords=["jarvis","alexa"]) 
        paud=pyaudio.PyAudio()
        audio_stream=paud.open(rate=porcupine.sample_rate,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=porcupine.frame_length)
        
        print("Listening for hotwords")
        
        #loop for streaming
        while True :
            keyword = audio_stream.read(porcupine.frame_length)
            keyword = struct.unpack_from("h" * porcupine.frame_length, keyword)
            #processing keyword comes from mic
            keyword_index = porcupine.process(keyword)
            #checking first keyword detected for not
            if keyword_index>=0:
                print("hotword detected")
                #processing shortcut key win+b
                import pyautogui as autogui
                autogui.keyDown("alt")
                autogui.press("b")
                time.sleep(2)
                autogui.keyUp("alt")
    except Exception as e:
        print(f"Error in hotword detection: {e}")
    finally:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()
            
def clean_phone_number(phone_number):
    # Remove all spaces from the phone number
    cleaned_number = phone_number.replace(" ", "")
    # Add +91 prefix if it's not present
    if not cleaned_number.startswith('+91'):
        cleaned_number = '+91' + cleaned_number
    return cleaned_number

def findContact(query):
    words_to_remove = [ASSISTANT_NAME , 'make' , 'bujji' , 'a','to','phone' , 'call', 'send','message','please','can','whatsapp','video','start']
    query = remove_words(query,words_to_remove)
    
    
    try:
        query = query.lower().strip()
        cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ?", ('%' + query + '%',))
        results = cursor.fetchall()
        print(results[0][0])
        if results:
            mobile_number_str = str(results[0][0])
            mobile_number_str = clean_phone_number(mobile_number_str)
            return mobile_number_str, query
        else:
            return 0, 0
    except Exception as e :
        print(f"Error in finding contact: {e}")
        return 0,0
    
def whatsApp(mobile_no , message , flag , name):
    if flag == "message":
        target_tab = 12
        bujji_message = "message sent successfully to "+name
        
    elif flag == "call":
        target_tab = 7
        message = ''
        bujji_message = "calling to "+name
    else:
        target_tab = 6
        message = ''
        bujji_message = "starting video call with "+name
        
    encoded_message = quote(message)
    
    #constructimg the url
    whatsapp_url = f"whatsapp://send?phone={mobile_no}&text={encoded_message}"
    #constructimg full command
    full_command = f'start "" "{whatsapp_url}"'
    
    #open whatsapp with the constructed url using cmd.exe
    subprocess.run(full_command,shell=True)
    time.sleep(5)
    subprocess.run(full_command,shell=True)
    pyautogui.hotkey('ctrl','f')
    for i in range(1,target_tab):
        pyautogui.hotkey('tab')
    pyautogui.press('enter')
    speak(bujji_message)
       
#chat application
def chatBot(query):
    user_input = query.lower()
    chatbot = hugchat.ChatBot(cookie_path="engine\cookies.json")
    id = chatbot.new_conversation()
    chatbot.change_conversation(id)
    response = chatbot.chat(user_input)
    print(response)
    speak(response)
    return response