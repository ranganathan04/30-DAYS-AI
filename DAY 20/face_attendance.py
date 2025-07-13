import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

# Load known faces
path = 'known_faces'
images = []
names = []

for file in os.listdir(path):
    img = cv2.imread(f'{path}/{file}')
    images.append(img)
    names.append(os.path.splitext(file)[0])

# Encode faces
def find_encodings(images):
    encodings = []
    for img in images:
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encodings.append(face_recognition.face_encodings(img_rgb)[0])
    return encodings

known_encodings = find_encodings(images)

# Mark attendance
def mark_attendance(name):
    with open('attendance.csv', 'a+') as f:
        f.seek(0)
        lines = f.readlines()
        recorded = [line.split(',')[0] for line in lines]
        if name not in recorded:
            now = datetime.now()
            timestamp = now.strftime('%H:%M:%S')
            f.write(f'{name},{timestamp}\n')

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()
    small = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb = cv2.cvtColor(small, cv2.COLOR_BGR2RGB)

    faces = face_recognition.face_locations(rgb)
    encodes = face_recognition.face_encodings(rgb, faces)

    for encode, loc in zip(encodes, faces):
        matches = face_recognition.compare_faces(known_encodings, encode)
        face_dist = face_recognition.face_distance(known_encodings, encode)
        match_index = np.argmin(face_dist)

        if matches[match_index]:
            name = names[match_index].upper()
            y1, x2, y2, x1 = [v*4 for v in loc]
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
            cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
            mark_attendance(name)

    cv2.imshow('Attendance System', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
