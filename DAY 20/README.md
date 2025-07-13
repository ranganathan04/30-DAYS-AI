# 🎓 Day 20: Face Recognition-Based Attendance System

A real-time face attendance system using webcam and the `face_recognition` library.

---

## ✅ Features

- Detects and recognizes faces from webcam
- Logs attendance (Name + Timestamp)
- Stores attendance in `attendance.csv`

---

## 🛠️ Requirements

```bash
pip install face_recognition opencv-python numpy

▶️ How to Run
Add known face images to the known_faces/ folder

Name them as yourname.jpg, etc.

Run the script:

python face_attendance.py

Show your face in front of the camera.

Name + Time will be added to attendance.csv

📌 Notes

Use clear, front-facing images for accurate recognition

Attendance will not be duplicated for the same session

