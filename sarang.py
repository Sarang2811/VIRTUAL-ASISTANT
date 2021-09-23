import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import pyjokes

listener = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say('Hey I am Alexa')
engine.say('What can I do for you')
engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()

    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)

    elif 'search' in command:
        person = command.replace('search', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'joke' in command:
        print(pyjokes.get_joke())
        talk(pyjokes.get_joke())

    elif 'bye' or 'exit' in command:
        talk('Bye Have a nice day')
        exit()


while True:
    run_alexa()
