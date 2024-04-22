import cv2
import pytesseract
from gtts import gTTS
import os

# Path to Tesseract executable (change this according to your system)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Read the image
image_path = 'words.jpeg'  # Change this to the path of your image
image = cv2.imread(image_path)

# Convert image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Perform OCR to extract text
extracted_text = pytesseract.image_to_string(gray_image)

# Print extracted text
print("Extracted Text:")
print(extracted_text)

# Convert extracted text to speech
tts = gTTS(text=extracted_text, lang='en')  # Language code (e.g., 'en' for English)
tts.save("output.mp3")

# Play the speech
os.system("start output.mp3")
