import cv2
import numpy as np
import pyautogui
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)
screen_width, screen_height = pyautogui.size()
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils
prev_click_time = 0

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_img)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            lm_list = []
            for id, lm in enumerate(hand_landmarks.landmark):
                h, w, _ = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lm_list.append((id, cx, cy))

            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            if lm_list:
                x_index, y_index = lm_list[8][1], lm_list[8][2]
                screen_x = np.interp(x_index, (100, 500), (0, screen_width))
                screen_y = np.interp(y_index, (100, 400), (0, screen_height))
                pyautogui.moveTo(screen_x, screen_y)

                x_thumb, y_thumb = lm_list[4][1], lm_list[4][2]
                distance = np.hypot(x_thumb - x_index, y_thumb - y_index)

                if distance < 40:
                    current_time = time.time()
                    if current_time - prev_click_time > 1:
                        pyautogui.click()
                        prev_click_time = current_time
                        cv2.putText(img, "CLICK", (x_index, y_index - 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 3)

    cv2.imshow("Virtual Mouse", img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
