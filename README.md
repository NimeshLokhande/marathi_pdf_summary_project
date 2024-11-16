# Marathi PDF Summarizer

This project extracts text, summarizes content, and identifies relevant keywords from Marathi PDF files using a combination of OCR, NLP, and Flask for web application development.

---

## Features
- **Text Extraction**: Converts PDF pages to images and uses Tesseract OCR for Marathi text extraction.
- **Summarization**: Generates a simple summary using NLP tools.
- **Keyword Extraction**: Identifies relevant keywords using the Stanza NLP library.
- **User-Friendly Web Interface**: Allows users to upload PDF files and view results seamlessly.

---

## Installation Guide

### Prerequisites
1. **Python**: Install Python 3.8 or above.
2. **Pip**: Ensure pip is installed for package management.
3. **Tesseract OCR**: For Optical Character Recognition.
4. **Poppler**: For converting PDF pages to images.

---

### Installation Steps

#### 1. Clone the Repository
```bash
git clone <repository-link>
cd marathi-pdf-summarizer

2. Install Python Dependencies

Install the required Python libraries listed in requirements.txt:

pip install -r requirements.txt

3. Install Tesseract OCR

Tesseract OCR is required to extract text from images.
Windows

    Download the Tesseract installer from Tesseract OCR GitHub.
    Install it and note the installation path (e.g., C:\Program Files\Tesseract-OCR\tesseract.exe).
    Add the installation path to the PATH environment variable.

Ubuntu

sudo apt update
sudo apt install tesseract-ocr
sudo apt install libtesseract-dev

macOS

brew install tesseract

4. Install Poppler

Poppler is used to convert PDF pages to images.
Windows

    Download the Poppler binaries from Poppler for Windows.
    Extract the downloaded file and note the bin folder path.
    Add the bin folder to the PATH environment variable.

Ubuntu

sudo apt update
sudo apt install poppler-utils

macOS

brew install poppler

5. Download Stanza Models

Ensure the Marathi Stanza model is downloaded:

python -c "import stanza; stanza.download('mr')"

Running the Project

    Start the Flask application:

python app.py

Open the application in your browser:

    http://127.0.0.1:5000

    Upload a Marathi PDF to extract text, generate a summary, and view keywords.

File Structure

marathi-pdf-summarizer/
│
├── app.py                # Main Flask application
├── requirements.txt      # Python dependencies
├── templates/
│   └── index.html        # Frontend HTML
├── pdf_processing/
│   ├── extract_text.py   # Extracts text from PDFs
│   └── summarize.py      # Summarization and keyword extraction
└── uploads/              # Folder for uploaded PDFs
