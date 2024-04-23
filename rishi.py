import datetime
from logging import exception
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import translators as ts
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
'''for i in range(3):
    print(voices[i].id)'''
engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def takecommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("recognizing.....")
        query=r.recognize_google(audio,language='te-IN')
        print(f"user said:{query}\n")
        text=ts.google(query,'te','en')
        print(text)
    except exception as e:
        print(e)
        print("say that again please....")
        return "None"
    return text
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("iam rishi how can i help you")
def sendEmail(to,content):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login('rishithreddy432@gmail.com','rinky akka')
    server.sendmail('rishithreddy432@gmail.com',to,content)
    server.close()
if __name__ =="__main__":
    wishme()
    while True:
        query=takecommand().lower()
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query=query.replace('wikipedia',"")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(results)
        elif 'youtube thervu' in query:
            webbrowser.open("youtube.com")
        elif 'open twitter' in query:
            webbrowser.open("twitter.com")
        elif 'play music' in query:
            music_dir="C:\\Users\\rishi\\Music\\patal"
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(strTime)
        elif "open code" in query:
            path="C:\\Users\\rishi\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)
        elif "email to" in query:
            try:
                speak("what should i say?")
                content=takecommand()
                to="rishithreddy432@gmail.com"
                sendEmail(to,content)
                speak("email has been sent")
            except exception as e:
                print(e)
                speak("sorry my friend hari bhai,iam not able to send")
        else:
            webbrowser.open(query)









    

