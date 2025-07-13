import cv2
import numpy as np
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1)

colors = [(255, 0, 255), (255, 0, 0), (0, 255, 0), (0, 0, 0)]
color_names = ['Purple', 'Blue', 'Green', 'Eraser']
color_index = 0
brush_thickness = 7
eraser_thickness = 50

canvas = None
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    h, w, c = img.shape

    if canvas is None:
        canvas = np.zeros_like(img)

    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_img)

    x1, y1 = 0, 0

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            lm_list = []
            for id, lm in enumerate(hand_landmarks.landmark):
                cx, cy = int(lm.x * w), int(lm.y * h)
                lm_list.append((id, cx, cy))

            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            if lm_list:
                x1, y1 = lm_list[8][1:]  # Index finger
                x2, y2 = lm_list[12][1:]  # Middle finger

                fingers_up = y2 < y1

                if fingers_up:
                    # Selection mode
                    for i, col in enumerate(colors):
                        cv2.rectangle(img, (i*100, 0), ((i+1)*100, 100), col, -1)
                    if y1 < 100:
                        color_index = x1 // 100
                else:
                    # Drawing mode
                    color = colors[color_index]
                    if color == (0, 0, 0):
                        cv2.circle(img, (x1, y1), eraser_thickness, color, -1)
                        cv2.circle(canvas, (x1, y1), eraser_thickness, color, -1)
                    else:
                        cv2.circle(img, (x1, y1), brush_thickness, color, -1)
                        cv2.circle(canvas, (x1, y1), brush_thickness, color, -1)

    img = cv2.addWeighted(img, 0.5, canvas, 0.5, 0)
    cv2.putText(img, color_names[color_index], (10, 460), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 3)
    cv2.imshow("Virtual Painter", img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
