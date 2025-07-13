import cv2

# Load image
image = cv2.imread('sample.jpg')

if image is None:
    print("❌ Error: sample.jpg not found. Please add an image file.")
else:
    # Show original image
    cv2.imshow("Original Image", image)

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Grayscale Image", gray)

    # Apply Canny Edge Detection
    edges = cv2.Canny(gray, 100, 200)
    cv2.imshow("Edge Detection", edges)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
