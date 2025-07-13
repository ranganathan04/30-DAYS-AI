# 😴 Day 21 - Drowsiness Detection for Driver Safety (MediaPipe Version)

This project detects drowsiness in real-time using MediaPipe Face Mesh and the Eye Aspect Ratio (EAR).

## 📦 Requirements

```bash
pip install opencv-python mediapipe numpy
```

## ▶️ How to Run

```bash
python drowsiness_detection.py
```

## 💡 How It Works

- Uses MediaPipe Face Mesh to get facial landmarks
- Calculates EAR (Eye Aspect Ratio)
- If EAR < 0.25 for several frames, a drowsiness alert is triggered

## ⚠️ Output

- Green EAR value shown on screen
- "⚠️ DROWSINESS ALERT" text displayed when eyes are closed too long

---
