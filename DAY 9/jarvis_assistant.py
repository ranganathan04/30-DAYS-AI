import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    print(f"JARVIS: {text}")
    engine.say(text)
    engine.runAndWait()

def wish_user():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am JARVIS. How can I help you?")

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("🔍 Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"You: {query}\n")
        return query.lower()
    except Exception:
        speak("Sorry, I didn't catch that.")
        return "None"

def run_jarvis():
    wish_user()
    while True:
        query = take_command()

        if 'time' in query:
            time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {time}")
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")
        elif 'open google' in query:
            webbrowser.open("https://www.google.com")
        elif 'play music' in query:
            music_dir = 'C:\\Users\\Public\\Music'
            songs = os.listdir(music_dir)
            if songs:
                os.startfile(os.path.join(music_dir, songs[0]))
            else:
                speak("No music files found.")
        elif 'exit' in query or 'bye' in query:
            speak("Goodbye! Have a great day.")
            break

if __name__ == "__main__":
    run_jarvis()
