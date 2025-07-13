# 🚗 Day 16: AI Number Plate Detection and Recognition

This project detects number plates using OpenCV and recognizes text using Tesseract OCR.

---

## ✅ Features

- Real-time number plate detection using Haar cascade
- Text recognition using `pytesseract`
- Draws bounding box + text on the frame

---

## 🛠️ Requirements

```bash

pip install opencv-python pytesseract

Windows users: install Tesseract OCR and set the path in your code.

▶️ How to Run

Download Haarcascade XML:

👉 Click to get XML : https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_russian_plate_number.xml

Save the file as:

haarcascade_russian_plate_number.xml

Run the script:

python number_plate_detector.py

Press q to quit.

⚠️ Notes

OCR accuracy depends on camera resolution and lighting.

You can save detected plates to a file for logging.