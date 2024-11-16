import pytesseract
from pdf2image import convert_from_path
from PIL import Image

# Tesseract executable path (update with your Tesseract OCR installation path)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_text_from_pdf(pdf_path, lang='mar'):

    # path to the Poppler binaries (update with your Poppler installation path)
    poppler_path = r'C:\Users\HP\Downloads\Release-24.08.0-0\poppler-24.08.0\Library\bin'  # Update this path with your Poppler binary path

    try:
        # Convert PDF pages to images using the specified Poppler path
        images = convert_from_path(pdf_path, poppler_path=poppler_path)

        extracted_text = ""
        for image in images:
            # Perform OCR on each image
            text = pytesseract.image_to_string(image, lang=lang)
            extracted_text += text + "\n"

        return extracted_text.strip()

    except Exception as e:
        return f"An error occurred: {str(e)}"