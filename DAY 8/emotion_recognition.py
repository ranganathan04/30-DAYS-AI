from facial_emotion_recognition import EmotionRecognition
import cv2

# Load model
er = EmotionRecognition(device='cpu')

# Open webcam
cam = cv2.VideoCapture(0)

while True:
    success, frame = cam.read()
    if not success:
        break

    # Detect emotion
    frame = er.recognise_emotion(frame, return_type='BGR')

    # Show the frame
    cv2.imshow('Emotion Recognition', frame)

    key = cv2.waitKey(1)
    if key == 27:  # ESC key to exit
        break

cam.release()
cv2.destroyAllWindows()
