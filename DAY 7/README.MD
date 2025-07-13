# 🧠 Face Recognition with Custom Dataset (Day 7)

This project captures face images, trains a face recognition model, and recognizes faces in real-time using OpenCV.

## 📂 Folder Structure

project-folder/
├── data_creation.py
├── face_detection.py
├── haarcascade_frontalface_default.xml
└── datasets/
└── [YourName]/[1.jpg, 2.jpg, ..., 50.jpg]


## ✅ How to Use

1. Install dependencies:

```bash
pip install opencv-python opencv-contrib-python numpy

2. Run to capture 50 face samples:

python data_creation.py

3. Then run the recognizer:

python face_detection.py

    Press q to quit the webcam.

⚙️ Requirements
Python 3.x

OpenCV with contrib modules (opencv-contrib-python)

Webcam