import pyautogui
import time
from PIL import ImageGrab

def is_obstacle_ahead(data):
    for x in range(300, 350):
        for y in range(410, 440):
            if data.getpixel((x, y))[0] < 100:  # Dark pixel = obstacle
                return True
    return False

def jump():
    pyautogui.keyDown("space")
    time.sleep(0.1)
    pyautogui.keyUp("space")

print("🦖 Dino bot will start in 3 seconds... Go to the game window.")
time.sleep(3)

while True:
    screenshot = ImageGrab.grab()
    if is_obstacle_ahead(screenshot):
        print("⛔ Obstacle detected! Jumping...")
        jump()
