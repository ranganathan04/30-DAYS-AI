import cv2

# Load pre-trained car Haar cascade classifier
car_cascade = cv2.CascadeClassifier('cars.xml')

# Load a sample video or use webcam
cap = cv2.VideoCapture('vehicles.avi')  # or use 0 for webcam

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to grayscale for Haar cascade
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect cars
    cars = car_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

    # Draw rectangles around detected cars
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display result
    cv2.imshow('Vehicle Detection', frame)

    if cv2.waitKey(30) & 0xFF == 27:  # Press Esc to exit
        break

cap.release()
cv2.destroyAllWindows()
