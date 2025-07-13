import cv2

import imutils

img = cv2.imread('sample.jpg')

resizedImg = imutils.resize(img, width=100)

cv2.imshow('OriginalImage2.jpg', img)
cv2.imshow('ResizedImage1.jpg', resizedImg)
