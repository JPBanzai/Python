import pytesseract
from PIL import Image

# Path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Path to the image file
image_path = 'D:\Proyectos PY\OCR\Codigo\imagetoread.png'

# Open the image using PIL (Python Imaging Library)
image = Image.open(image_path)

# Use pytesseract to get the OCR data and bounding box information
ocr_data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT, lang='jpn')

# Iterate over each detected text block
for i, (text, left, top, width, height) in enumerate(
        zip(ocr_data['text'], ocr_data['left'], ocr_data['top'], ocr_data['width'], ocr_data['height'])):
    # Skip empty text blocks
    if text.strip() != '':
        print(f"Text {i+1}: {text}")
        print(f"Coordinates: Left={left}, Top={top}, Width={width}, Height={height}")
        print()
