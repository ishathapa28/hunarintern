import webbrowser
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()

device_index = 0

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def speak(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone(device_index=device_index) as source:
            speak('Hello I am alexa')
            speak('how can i help you today?')
            # 0.8 is default pause_threshold anyway
            # listener.pause_threshold = 1
            print("Adjusting for ambient noise...")
            listener.adjust_for_ambient_noise(source, duration=3)
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language='en-in')
            print("You said: " + command)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        speak("I didn't catch that. Can you say it again?")
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service")
        speak("I'm having trouble connecting to the speech recognition service.")
    except Exception as e:
        print("An error occurred: " + str(e))
        speak("An unexpected error occurred.")
    return command

def run_alexa():
    command = take_command()
    if not command:
        speak("I didn't hear anything. Please try again.")
        return

    if 'play' in command:
        song = command.replace('play', '')
        speak('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time =  datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        speak('Current time is ' + time)
    elif 'search for' in command:
        person = command.replace('search for', '')
        try:
            info = wikipedia.summary(person, 1)
            print(info)
            speak(info)
        except wikipedia.exceptions.DisambiguationError as e:
            speak("There are multiple results. Can you be more specific?")
        except wikipedia.exceptions.PageError:
            speak("Sorry, I couldn't find information on that topic.")
    elif 'joke' in command:
        speak(pyjokes.get_joke())


    else:
        speak('Please say the command again.')

    sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],
             ["google", "https://www.google.com"]]
    for site in sites:
        if f"Open {site[0]}".lower() in command.lower():
            speak(f"Opening {site[0]} sir..")
            webbrowser.open(site[1])

while True:
    run_alexa()





