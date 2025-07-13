import cv2
import numpy as np
from os import listdir
from os.path import isfile, join
import os

data_path = 'datasets/'
only_dirs = [d for d in listdir(data_path) if os.path.isdir(join(data_path, d))]

Training_Data, Labels = [], []

label_map = {}
current_label = 0

for person in only_dirs:
    person_path = join(data_path, person)
    onlyfiles = [f for f in listdir(person_path) if isfile(join(person_path, f))]
    for i, file in enumerate(onlyfiles):
        image_path = join(person_path, file)
        images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        if images is None:
            continue
        Training_Data.append(np.asarray(images, dtype=np.uint8))
        Labels.append(current_label)
    label_map[current_label] = person
    current_label += 1

Labels = np.asarray(Labels, dtype=np.int32)

model = cv2.face.LBPHFaceRecognizer_create()
model.train(np.asarray(Training_Data), np.asarray(Labels))

print("✅ Model trained successfully!")

face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def face_detector(img, size=0.5):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    if faces is ():
        return img, []

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
        roi = img[y:y + h, x:x + w]
        roi = cv2.resize(roi, (200, 200))
        return img, roi

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    image, face = face_detector(frame)

    try:
        gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        result = model.predict(gray)

        confidence = int(100 * (1 - result[1] / 300))
        display_text = f"{label_map[result[0]]} - {confidence}%"

        if confidence > 70:
            cv2.putText(image, display_text, (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
        else:
            cv2.putText(image, "Unknown", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)

        cv2.imshow('Face Recognition', image)

    except Exception as e:
        cv2.putText(image, "Face not found", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
        cv2.imshow('Face Recognition', image)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
