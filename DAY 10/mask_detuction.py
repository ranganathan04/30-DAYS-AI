from tensorflow.keras.models import load_model
import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
model = load_model('mask_detector.model')

labels_dict = {0: '😷 Mask', 1: '❌ No Mask'}
color_dict = {0: (0, 255, 0), 1: (0, 0, 255)}

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for x, y, w, h in faces:
        face = frame[y:y+h, x:x+w]
        resized = cv2.resize(face, (100, 100))
        normalized = resized / 255.0
        reshaped = np.reshape(normalized, (1, 100, 100, 3))

        result = model.predict(reshaped)
        label = np.argmax(result, axis=1)[0]

        color = color_dict[label]
        text = labels_dict[label]

        cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
        cv2.putText(frame, text, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

    cv2.imshow("Mask Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
