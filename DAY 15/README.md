# 🎵 Day 15: AI Music Genre Classification

This project uses a pre-trained model to classify audio files into genres based on their MFCC features.

---

## ✅ Features

- Extracts MFCCs using `librosa`
- Predicts genre using a trained Keras model
- Supports multiple genres: classical, pop, rock, jazz, hiphop

---

## ▶️ How to Run

### 1. Install Dependencies

```bash
pip install librosa tensorflow numpy

2. Add Audio + Model

Place test_audio.wav in the folder

Ensure genre_model.h5 is your trained model

3. Run

python genre_predictor.py

🧠 How it Works
Extract MFCC features

Feed into neural network

Output predicted genre

📌 Tips
You can train your model using GTZAN dataset (10 genres, 100 clips each)

Use librosa to extract audio features from training files