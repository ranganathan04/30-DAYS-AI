import cv2  # OpenCV
import time  # Delay
import imutils  # Resize

cam = cv2.VideoCapture(0)  # Use 0 for default webcam; change if needed
time.sleep(1)  # Let the camera warm up

firstFrame = None
area = 500  # Minimum area size for motion detection

while True:
    ret, img = cam.read()
    if not ret:
        break

    text = 'Normal'
    img = imutils.resize(img, width=1000)

    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gaussianImg = cv2.GaussianBlur(grayImg, (21, 21), 0)

    if firstFrame is None:
        firstFrame = gaussianImg
        continue

    imgDiff = cv2.absdiff(firstFrame, gaussianImg)
    threshImg = cv2.threshold(imgDiff, 25, 255, cv2.THRESH_BINARY)[1]
    threshImg = cv2.dilate(threshImg, None, iterations=2)

    contours, _ = cv2.findContours(threshImg.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:
        if cv2.contourArea(c) < area:
            continue

        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        text = "Moving Object Detected"

    cv2.putText(img, f"Room Status: {text}", (10, 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    cv2.imshow("Live Camera", img)
    cv2.imshow("Threshold Image", threshImg)
    cv2.imshow("Difference Image", imgDiff)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
