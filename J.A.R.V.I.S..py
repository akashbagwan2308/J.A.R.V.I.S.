# --------------------------------------------------J.A.R.V.I.S.--------------------------------------------------------
# -------------------------------------------------Import Modules-------------------------------------------------------
import datetime
import random
import pyttsx3
import pyaudio
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

# ----------------------------------------------------------------------------------------------------------------------
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty('voice',voices[0].id)
# -----------------------------------------------------Functions--------------------------------------------------------
def speak(audio):
    """This function is used to speak the text"""
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    """This function is used to wish me     """
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        # print('Good Morning!')
        speak('Good Morning!')
    elif hour>=12 and hour<18:
        # print('Good Afternoon!')
        speak('Good Afternoon!')
    else:
        # print('Good Evening!')
        speak('Good Evening!')
    # print("I am JARVIS Sir. Please tell me how may I help you.")
    speak("I am JARVIS Sir. Please tell me how may I help you")
def takeCommand():
    """This function in used to take microphone input fron the user and return string"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("sendereEmail@gmail.com",'your_password')
    server.sendmail('senderEmail@gmail.com',to,content)
    server.close()


# -----------------------------------------------------Main Code--------------------------------------------------------
if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
#-----------------------------------------------------Wikipedia---------------------------------------------------------
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia',"")
            results = wikipedia.summary(query,sentences = 2)
            speak("According to wikipedia")
            print(results)
            speak(results)
#-----------------------------------------------------Websearch---------------------------------------------------------
        elif 'open youtube' in query:
            speak("Opening youtube")
            webbrowser.open("youtube.com")
        elif 'open tarak mehta' in query:
            speak("Opening tarak mehta")
            webbrowser.open("youtube.com/results?search_query=tarak+mehta+ka+ooltaah+chashma")
        elif 'open google' in query:
            speak("Opening google")
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            speak("Opening stackoverflow")
            webbrowser.open("stackoverflow.com")
        elif 'open gmail' in query:
            speak("Opening gmail")
            webbrowser.open("mail.google.com")
        elif 'open linkedin' in query:
            speak("Opening linkedin")
            webbrowser.open("linkedin.com/in/akashbagwan01")
        elif 'open github' in query:
            speak("Opening github")
            webbrowser.open("github.com/akashbagwan2308")
# ----------------------------------------------------Play Music--------------------------------------------------------
        elif 'play music' in query:
            music_dir = "C:\\Users\\Lenovo\\Music"
            songs = os.listdir(music_dir)
            k = random.randint(0,len(songs))
            speak("Playing music")
            os.startfile(os.path.join(music_dir,songs[k]))
# --------------------------------------------------Time Enquiry--------------------------------------------------------
        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Sir, the time is {strtime}")
            speak(f"Sir, the time is {strtime}")
# ------------------------------------------------Open Softwares--------------------------------------------------------
        elif 'open vs code' in query:
            codePath = "C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'open pycharm' in query:
            codePath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.3.2\\bin\\pycharm64.exe"
            os.startfile(codePath)
        elif 'open whatsapp' in query:
            codePath = "C:\\Users\\Lenovo\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(codePath)
# -----------------------------------------------Email send-------------------------------------------------------------
        elif 'email to akash' in query:
            try:
                speak("What should I say??")
                content = takeCommand()
                print(content)
                to = "receiverE mail@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry akash I am not able to send this email")
# ----------------------------------------------------------------------------------------------------------------------