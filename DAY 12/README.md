# 🖐️ Day 12: Hand Gesture Controlled Virtual Mouse

This project lets you control your computer mouse using hand gestures via webcam.

---

## ✅ Features

- Move mouse with your index finger
- Click by pinching (thumb + index)
- Real-time hand tracking using Mediapipe

---

## 📦 Requirements

```bash
pip install opencv-python mediapipe pyautogui numpy
```

---

## ▶️ How to Run

1. Run the script:

```bash
python virtual_mouse.py
```

2. Make sure your hand is visible in the webcam
3. Use your **index finger** to move the mouse
4. **Pinch (thumb + index)** to perform a click

---

## 🧠 Tips

- Works best in good lighting
- Adjust `np.interp()` values to fine-tune screen mapping
- Press `ESC` to exit
