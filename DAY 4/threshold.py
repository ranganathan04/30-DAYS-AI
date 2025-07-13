import cv2

img = cv2.imread('novitech.png')

grayImg = cv2.cvColor(img, cv2.COLOR_BGR2GRAY)

#dst = cv2.threshold(src, threshold, maxValueFo

thresholdImg = cv2.threshold(grayImg,180,255,cv2.THRESH_BINARY) [1]

cv2.imshow("Original",img)

cv2.imshow("Threshold.jpg",thresholdImg)


#0 - black

#180

#255 - white
