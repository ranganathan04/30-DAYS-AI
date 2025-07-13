# 🕹️ Day 11: Chrome Dino Game Bot with Python

This project automates the Chrome Dino Game using Python.

---

## ✅ Features

- Captures screen in real-time
- Detects obstacles using pixel values
- Simulates spacebar to make the dino jump

---

## 📂 Files

- `dino_bot.py`: Main bot script
- `README.md`: Project instructions

---

## ▶️ How to Use

### 1. Install dependencies:

```bash
pip install pillow pyautogui
```

> For faster capture (optional):
```bash
pip install mss
```

### 2. Open the Dino game in Chrome:

Type this in Chrome:

```
chrome://dino
```

Press `Space` to begin the game.

### 3. Run the bot:

```bash
python dino_bot.py
```

Then quickly switch to the game window.

---

## 🛠 Requirements

- Python 3.x
- pyautogui
- pillow (PIL)
- Works on Windows with a standard 1366x768 or similar screen

---

## ⚠️ Note

- You may need to adjust pixel coordinates for different screen sizes.
- Works best on light background with dark obstacles.

Enjoy your auto-playing AI Dino! 🦖
