import cv2
img = cv2.imread('sample.jpg')

gaussianImg = cv2.GaussianBlur(img, (41, 41), 50)
gaussianImg1 = cv2.GaussianBlur(img, (21, 42), 0)

cv2.imshow("Original", img)
cv2.imshow("GaussianBlur", gaussianImg)
cv2.imshow("GaussianBlur", gaussianImg1)



