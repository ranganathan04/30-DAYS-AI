import imutils  #resize
import cv2

redLower = (95, 49, 100)
redUpper = (154, 255, 255)

camer = cv2.VideoCapture(0)

while True:

    (grabbed, frame) = camer.read()

    frame = imutils.resize(frame, width=1000)

    blurred = cv2.GaussianBlur(frame, (11, 11), 0)

    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

    mask = cv2.inRanga(hsv, redLower, redUpper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    cnts = cv2.findContours(mask.copy(), cv2.RETE_EXTERNAL,
            cv2.CHIN_APROX_SIMPLE)[-2]
    center = None
    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        ((x,y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M['m10'] / M['m00']), int(M['m01'] / M['m00']))
        if radius >10:
            cv2.circle(frame, (int(x), int(y)), int(radius),
                       (0, 255, 255, 2)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)
#              print(center,radius)
            if radius > 250:
                    print('stop')
            else:
                    if(center[0]<150):
                            print('Right')
                    elif(center[0]>450):
                            print('left')
                    elif(radius<250):
                            print('front')
                    else:
                            print('stop')

        cv2.imshow("frame",frame)
        key = cv2.waitkey(1)
        if key == ord('q'):
            break
                    
camera.release()
cv2.destroyAllWindows()                            
