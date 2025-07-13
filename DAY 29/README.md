# 🎙️ Day 29 - Analyzing Speech and Emotions using CNN and NLP

This project performs emotion analysis from speech by transcribing spoken text and classifying its sentiment/emotion.

## 🎯 Features
- 🎧 Speech-to-Text
- 💬 NLP Text Cleaning
- 😃 Emotion Classification using a pre-trained ML or CNN model

## 🧰 Requirements

```bash
pip install speechrecognition scikit-learn nltk joblib
```

Optional (for audio support):
```bash
pip install pyaudio
```

## ▶️ Run

Place an audio file named `audio_sample.wav` in the same folder and run:

```bash
python emotion_analyzer.py
```

## 📦 Files Needed
- `audio_sample.wav` - recorded speech
- `emotion_model.pkl` - pre-trained model (Naive Bayes / CNN)
- `vectorizer.pkl` - TF-IDF vectorizer for the text

---
