import speech_recognition as sr
import joblib
import re
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download('stopwords')

# Load ML model and vectorizer
model = joblib.load('emotion_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

# Function to clean text
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    tokens = text.split()
    tokens = [word for word in tokens if word not in stopwords.words('english')]
    return " ".join(tokens)

# Speech to text
recognizer = sr.Recognizer()
with sr.AudioFile("audio_sample.wav") as source:
    audio_data = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio_data)
        print("🎧 Transcribed Text:", text)

        cleaned = clean_text(text)
        X = vectorizer.transform([cleaned])
        prediction = model.predict(X)[0]
        print("💬 Detected Emotion:", prediction)

    except sr.UnknownValueError:
        print("Speech Recognition could not understand audio.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
