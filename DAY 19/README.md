# 👁️ Day 19: AI-Based Eye Blink Detection

This project detects eye blinks using the Eye Aspect Ratio (EAR) technique with Dlib and OpenCV.

---

## ✅ Features

- Real-time blink detection
- Tracks total number of blinks
- Can be extended for drowsiness alerts, etc.

---

## 🛠️ Requirements

```bash
pip install opencv-python dlib imutils scipy
```

---

## 📁 Files Needed

- `eye_blink_detector.py`
- `shape_predictor_68_face_landmarks.dat`  
  👉 Download from: https://github.com/davisking/dlib-models

---

## ▶️ How to Run

```bash
python eye_blink_detector.py
```

- Look at the webcam and blink naturally
- Press `q` to quit

---

## 📌 Tip

You can trigger alerts or log data if blinks exceed or fall below a range.

👀 Real-time blink awareness, powered by AI.
