import librosa
import numpy as np
from keras.models import load_model

# Load model
model = load_model("genre_model.h5")
genres = ['classical', 'pop', 'rock', 'jazz', 'hiphop']

def extract_features(file_path):
    audio, sr = librosa.load(file_path, duration=30)
    mfccs = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=40)
    mfccs_scaled = np.mean(mfccs.T, axis=0)
    return mfccs_scaled.reshape(1, -1)

# Test prediction
file = "test_audio.wav"
features = extract_features(file)
prediction = model.predict(features)
predicted_genre = genres[np.argmax(prediction)]

print(f"🎵 Predicted Genre: {predicted_genre}")
