import cv2

# Initialize video capture
cap = cv2.VideoCapture(0)

# Read first two frames
ret, frame1 = cap.read()
ret, frame2 = cap.read()

if not ret:
    print("❌ Unable to access the webcam.")
    cap.release()
else:
    print("📹 Press 'q' to quit.")
    while cap.isOpened():
        # Difference between two frames
        diff = cv2.absdiff(frame1, frame2)

        # Convert to grayscale
        gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

        # Blur the image
        blur = cv2.GaussianBlur(gray, (5, 5), 0)

        # Threshold the image
        _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)

        # Dilate to fill in holes
        dilated = cv2.dilate(thresh, None, iterations=3)

        # Find contours
        contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            if cv2.contourArea(contour) < 500:
                continue
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame1, "Movement Detected", (10, 20),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

        cv2.imshow("Live Feed", frame1)

        frame1 = frame2
        ret, frame2 = cap.read()

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
