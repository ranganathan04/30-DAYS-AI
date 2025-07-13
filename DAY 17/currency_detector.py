import cv2
import numpy as np
import os

def load_templates(folder="templates"):
    templates = {}
    for file in os.listdir(folder):
        path = os.path.join(folder, file)
        img = cv2.imread(path, 0)
        if img is not None:
            templates[file.split('.')[0]] = img
    return templates

def detect_currency(input_img, templates):
    gray = cv2.cvtColor(input_img, cv2.COLOR_BGR2GRAY)
    best_match = None
    max_val = 0
    for label, temp in templates.items():
        res = cv2.matchTemplate(gray, temp, cv2.TM_CCOEFF_NORMED)
        _, match_val, _, _ = cv2.minMaxLoc(res)
        if match_val > max_val and match_val > 0.5:
            max_val = match_val
            best_match = label
    return best_match

cap = cv2.VideoCapture(0)
templates = load_templates()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    detected = detect_currency(frame, templates)
    if detected:
        cv2.putText(frame, f"Currency: ₹{detected}", (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)

    cv2.imshow("Currency Detector", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
