import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
engine = pyttsx3. init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty("voice", voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("good morning!")

    elif hour>=12 and hour<18:
        speak("good afternoon!")

    else:
        speak("good evening!")

    speak(" I am jenoid sir.... how may i help you ")


def takecommand():
    # it takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr. Microphone() as source:
        print("listning...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognizing...")
        query = r. recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print(e)
        print("say that again please...")
        return "none"
    return query


if __name__ == "__main__":
    wishme()
    #while True:
    if 1:
        query = takecommand().lower()
        # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query)
            print('according to wikipedia')
            print(results)
            speak(results)
        elif'jenoid,open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open brave' in query:
            bravepath = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application"
            os.open(bravepath)
        elif 'gogo anime' in query:
            webbrowser.open("gogo anime.com")
        elif'who are you' in query:
            speak("I am jenoid, I am an voice assistent , devlopd by mister jagrav  ")
        elif' who is Narendra modi' in query:
            speak(" Nerandra modi is india's ,honorable prime minister , he is 83 years old , recently his mother died ")

        elif'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir ,the time is{strTime}")
        elif'open pycharm' in query:
            coadpath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2022.3.1\\bin"
            os.open(coadpath)