import cv2
import pytesseract

# Configure Tesseract path if needed (especially on Windows)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load image
image = cv2.imread('number_plate.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Load Haar cascade for license plate
plate_cascade = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')

# Detect plates
plates = plate_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in plates:
    plate = image[y:y+h, x:x+w]
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # OCR on cropped plate
    plate_text = pytesseract.image_to_string(plate, config='--psm 8')
    print("Detected Plate Text:", plate_text.strip())

    cv2.putText(image, plate_text.strip(), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)

# Show result
cv2.imshow("License Plate Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
