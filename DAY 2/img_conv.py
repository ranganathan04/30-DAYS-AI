import cv2

image = cv2.imread(r"sample.jpg")

grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('original', image)

cv2.imshow('gray', image)

print(image.shape)

print(image.size)
