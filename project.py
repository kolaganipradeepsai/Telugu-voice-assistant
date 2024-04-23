from logging import exception
import speech_recognition as sr
import translators as ts
#import pyttsx3
import datetime
import os
from gtts import gTTS
import playsound
import wikipedia
import webbrowser
import os
import random
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
def rishiSpeak(text):
    file_name="audio.mp3"
    tts=gTTS(text=text,lang='te',tld='com')
    tts.save(file_name)
    playsound.playsound(file_name)
    os.remove(file_name)
def rishiSpeechInput():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold=1
        print('రింకీ వింటుంది......')
        audio=r.listen(source)
    try:
        print('మీరూ అన్నధానిని గుర్తించడానికీ ప్రయాత్నిస్తోంది......')
        text=r.recognize_google(audio,language='te-IN')
        text=ts.google(text,'te','en')
    except Exception as e:
       rishiSpeak("రింకీ మీరు ఏమి చెప్పారో గుర్తించలేకపోయింది, దయచేసి మళ్లీ పునరావృతం చేయండి")
       return "none"
    return text
def welcome():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        wish="good morning "
    elif hour>=12 and hour<16:
        wish="good afternoon "
    else:
        wish="good evening "
    rishiSpeak(ts.google("namaste nenu rinky what is your name?",'en','te'))
    name="none"
    while name=="none":
        name=rishiSpeechInput()
    rishiSpeak(ts.google(wish+name+" how can i help you",'en','te'))
if __name__ =="__main__":
    welcome()
    while True:
        query="none"
        while query=="none":
            query=rishiSpeechInput()
        query=query.lower()
        if 'search' in query or "browse" in query:
            query=query.replace('search','')
            query=query.replace("browse","")
            query=query.replace("rinky","")
            query=query.replace("","+")
            browser=webdriver.Chrome(ChromeDriverManager().install())
            elements=browser.get("https://www.google.com/search?q="+query+"&start"+str(0))
        elif 'wikipedia' in query:
            rishiSpeak(ts.google("rinky is searching for which you asked",'en','te'))
            query=query.replace("wikipedia","")
            try:
                result=wikipedia.summary(query,sentences=3)
                result="according to wikipedia"+result
                result=ts.google(result,'en','te')
                rishiSpeak(result)
            except Exception as e:
                print(e)
        elif 'open youtube' in query:
            rishiSpeak(ts.google("rinky is opening youtube",'en','te'))
            webbrowser.open("youtube.com")
        elif "open twitter" in query:
            rishiSpeak(ts.google("rinky is opening twitter",'en','te'))
            webbrowser.open("twitter.com")
        elif "open instagram" in query:
            rishiSpeak(ts.google("rinky is opening instagram",'en','te'))
            webbrowser.open("instagram.com")
        elif "chrome" in query:
            file_directory="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome.lnk"
            rishiSpeak(ts.google("rinky is opening chrome browser",'en','te'))
            os.startfile(file_directory)
        elif "photo" in query:
            file_directory="C:\\Users\\rishi\\OneDrive\\Pictures\\photos"
            photos=os.listdir(file_directory)
            l=len(photos)
            k=random.randint(0,l-1)
            file_directory=file_directory+f"\\{photos[k]}"
            rishiSpeak(ts.google("rinky is opening photos",'en','te'))
            os.startfile(file_directory)
        elif 'music' in query:
            music_dir="C:\\Users\\rishi\\Music\\patal"
            songs=os.listdir(music_dir)
            l=len(songs)
            k=random.randint(0,l-1)
            #print(songs)
            os.startfile(os.path.join(music_dir,songs[k]))
        elif 'time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            file_name="audio.mp3"
            tts=gTTS(text=strTime,lang='en',tld='com')
            tts.save(file_name)
            playsound.playsound(file_name)
            os.remove(file_name)
        elif 'date' in query:
            rishiSpeak(ts.google("today date is",'en','te'))
            date=datetime.date.today().strftime("%m/%d/%Y")
            file_name="audio.mp3"
            tts=gTTS(text=date,lang='en',tld='com')
            tts.save(file_name)
            playsound.playsound(file_name)
            os.remove(file_name)
        elif 'meaning' in query:
            query=query.replace("meaning","")
            query=query.replace("rinky","")
            rishiSpeak(ts.google(query,'en','te')) 
        elif 'code blocks' in query:
            path="C:\\Users\\rishi\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\CodeBlocks\\CodeBlocks.lnk"
            rishiSpeak(ts.google("rinky is opening codeblocks",'en','te'))
            os.startfile(path)
        elif "name" in query:
            rishiSpeak(ts.google("my name is rinky",'en','te'))
        if query=='stop':
            rishiSpeak(ts.google("thankyou for using me ",'en','te'))
            break
        print(ts.google("say stop to stop rinky",'en','te'))
   


        
