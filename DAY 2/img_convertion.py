import cv2

# Read an image
img = cv2.imread("sample.jpg")

# Display the image in a window named 'show'
cv2.imshow('show', img)

# Save the image as 'photo.jpg'
cv2.imwrite('photo.jpg', img)

# Wait for 5000 milliseconds (5 seconds)
cv2.waitKey(5000)

# Close all OpenCV windows
cv2.destroyAllWindows()
