import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import sys


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    elif hour >= 18 and hour < 20:
        speak("Good evening")
    else:
        speak("Good night!")

    speak("I am Jarvis Sir. Please tell me how may i help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio,language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            #print(e)

            print("Say that again please...")
            return "None"
        return query
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('Yourmail@gmail.com','your password')
    server.sendmail('recivermail@gmail.com',to,content)
    server.close()

if __name__ == '__main__':
    speak("RITIK KUMAR SIR ")
    wishMe()
    while True:

        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            speak("opening youtube!")
            chromePath = r"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            webbrowser.register("chrome",None, webbrowser.BackgroundBrowser(chromePath))
            webbrowser.get("chrome").open_new_tab("youtube.com")

        elif 'open google' in query:
            speak("opening google!")
            chromePath = r"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            webbrowser.register("chrome",None, webbrowser.BackgroundBrowser(chromePath))
            webbrowser.get("chrome").open_new_tab("google.com")


        elif 'open facebook' in query:
            speak("opening facebook!")
            chromePath = r"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            webbrowser.register("chrome",None, webbrowser.BackgroundBrowser(chromePath))
            webbrowser.get("chrome").open_new_tab("facebook.com")
        elif 'open instagram' in query:
            speak("opening instagram!")
            chromePath = r"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            webbrowser.register("chrome",None, webbrowser.BackgroundBrowser(chromePath))
            webbrowser.get("chrome").open_new_tab("instagram.com")
        elif 'open stack overflow' in query:
            speak("opening stack overflow!")
            chromePath = r"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            webbrowser.register("chrome",None, webbrowser.BackgroundBrowser(chromePath))
            webbrowser.get("chrome").open_new_tab("stackoverflow.com")
        elif 'play music' in query:
            music_dir = 'D:\\MIUI\\sound_recorder\\call_rec'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is {strTime}")
        elif 'open code' in query:
            codePath = "C:\\Users\\ritik\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'open whatsapp' in query:
            whatsappPath = "C:\\Users\\ritik\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(whatsappPath)
        elif 'java ka compiler khol de' in query:
            intellijPath = "C:\\Program Files\\JetBrains\\jetbrains\\IntelliJ IDEA Community Edition 2020.2\\bin\\idea64.exe"
            os.startfile(intellijPath)


        elif 'email to ritik' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "recivermail@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend ritik bhai. I am not able to send this email")
        elif 'band ho ja' in query:
            exit()



