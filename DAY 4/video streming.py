import cv2

vs = cv2.VideoCapture(0)  #initializing camera id if it is web cam instude 0 give 1

while True:
    _,img = vs.read()

    cv2.imshow("VideoStream", img)

    key = cv2.waitKey(1)

    print(key)
    if key == ord("q"): #or 113
        break

vs.release()
cv2.destroyAllWindows()
    
