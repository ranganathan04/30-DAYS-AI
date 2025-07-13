import urllib.request
import cv2
import numpy as np
import imutils

# Replace with your actual IP from IP Webcam app
url = 'http://192.168.x.x:8080/shot.jpg'

while True:
    try:
        # Get image from mobile camera
        imgResp = urllib.request.urlopen(url)
        imgNp = np.array(bytearray(imgResp.read()), dtype=np.uint8)
        frame = cv2.imdecode(imgNp, -1)

        # Resize and show
        frame = imutils.resize(frame, width=450)
        cv2.imshow('Mobile Camera Feed', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    except:
        print("❌ Failed to connect. Check IP address and network.")

cv2.destroyAllWindows()
