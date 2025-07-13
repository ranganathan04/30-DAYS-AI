# 😷 Real-Time Face Mask Detection Using Pre-Trained Model

This project detects whether a person is wearing a mask in real-time using OpenCV and a pre-trained deep learning model.

---

## ✅ Features

- Detects faces in real-time using webcam
- Classifies each face as:
  - ✅ "Mask"
  - ❌ "No Mask"
- Uses a pre-trained `.h5` model — **no training or dataset required**

---

## 📂 Project Files

project-folder/
├── mask_detection.py
├── mask_detector.model # Downloaded pre-trained model
├── haarcascade_frontalface_default.xml
└── README.md


---

## ▶️ How to Run

### 1. 📦 Install Dependencies

```bash
pip install tensorflow opencv-python numpy

2. 📥 Download Pre-trained Model
Download the mask detector model and save it as:

📁 Download mask_detector.model

Make sure it’s in the same folder as your script.

3. 🧠 Run the Detection Script
bash
Copy
Edit
python mask_detection.py
Press q to quit the webcam feed.

🛠 Requirements
Python 3.x

TensorFlow / Keras

OpenCV

Webcam

Pre-trained .h5 model

