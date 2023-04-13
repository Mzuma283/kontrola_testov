import cv2
import pytesseract

# Load the image
img = cv2.imread('fotky\image_1 - Copy.png')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply thresholding to the image to make it binary
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Find the contours in the image
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Set up the Tesseract OCR engine
pytesseract.pytesseract.tesseract_cmd = r'c:\users\sivyv\appdata\local\programs\python\python310\lib\site-packages.exe'

# Loop through each contour in the image
for contour in contours:
    # Get the bounding rectangle of the contour
    x, y, w, h = cv2.boundingRect(contour)

    # Check if the contour is a square with a certain aspect ratio
    if w > 10 and h > 10 and abs(w - h) < 5:
        aspect_ratio = float(w) / h
        if aspect_ratio >= 0.8 and aspect_ratio <= 1.2:
            # Extract the square from the image
            square = thresh[y:y+h, x:x+w]

            # Apply OCR to the square to check if it has been crossed out
            text = pytesseract.image_to_string(square)

            # Check if the text in the square is a cross-out mark
            if 'X' in text or 'x' in text:
                print(f"Square at ({x}, {y}) has been crossed out.")