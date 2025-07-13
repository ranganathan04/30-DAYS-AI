import cv2
import os

face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def face_extractor(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    
    if faces is ():
        return None
    
    for (x, y, w, h) in faces:
        cropped_face = img[y:y + h, x:x + w]
        return cropped_face

def main():
    name = input("Enter the name of the person: ")
    path = os.path.join('datasets', name)
    os.makedirs(path, exist_ok=True)

    cap = cv2.VideoCapture(0)
    count = 0

    print("📸 Capturing images. Press 'q' to stop early.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        face = face_extractor(frame)
        if face is not None:
            count += 1
            face = cv2.resize(face, (200, 200))
            file_name_path = os.path.join(path, f'{count}.jpg')
            cv2.imwrite(file_name_path, face)

            cv2.putText(face, str(count), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow('Face Cropper', face)
        else:
            print("Face not found")

        if cv2.waitKey(1) == ord('q') or count >= 50:
            break

    cap.release()
    cv2.destroyAllWindows()
    print("✅ Dataset collection complete!")

if __name__ == "__main__":
    main()
