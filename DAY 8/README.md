
# 😊 Day 8: Emotion Recognition from Faces

This project performs real-time facial emotion recognition using a webcam or a mobile IP camera.

---

## ✅ Features

- Detects emotions like Happy, Sad, Angry, etc.
- Two modes:
  - Webcam-based (`emotion_recognition.py`)
  - Mobile IP camera (`emotion_recognition_using_mobile_cam.py`)

---

## 🛠 Install Requirements

```bash
pip install torch torchvision
pip install facial-emotion-recognition
pip install imutils

1. Web Cam Mode

python emotion_recognition.py

Press ESC to quit.

🔹 Mobile IP Camera Mode
1. Download IP Webcam on your Android phone

2. Start the server and copy the IP address (e.g., http://192.168.1.5:8080/shot.jpg)

3. Replace the url in the script

4. Run:

python emotion_recognition_using_mobile_cam.py

Press q to quit.

🎯 Use Cases
AI teacher-student interaction

Emotion-aware robotics

Human-computer interaction

🔧 Requirements
Python 3.x

OpenCV

PyTorch

Webcam or IP camera
