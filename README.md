# OCR and Document Search Web Application

This project is a web-based application that allows users to upload images or documents, extract text from them using Optical Character Recognition (OCR), and perform searches across the extracted text. Built with `Gradio` for a user-friendly interface and leveraging `Pytesseract` for OCR functionality, this app is ideal for managing and searching text from scanned documents, images, and PDFs.

## Features

- **OCR Processing**: Extract text from images or documents in multiple languages using Tesseract.
- **Document Search**: Perform a keyword search across the extracted text to find relevant information quickly.
- **Gradio Interface**: User-friendly web interface for uploading documents and displaying results.
- **Multiple Language Support**: The application can handle multiple languages, including English and Hindi.

## Tech Stack

- **Gradio**: For building the web-based interface.
- **Pytesseract**: To perform OCR on uploaded images and documents.
- **Python**: Backend processing.
- **Tesseract-OCR**: The underlying OCR engine used for text extraction.
  
## Requirements

Before running the application, ensure you have the following installed:

- Python 3.x
- Tesseract-OCR
  - For Linux:
    ```bash
    sudo apt-get install tesseract-ocr
    ```
  - For Windows, download from [here](https://github.com/tesseract-ocr/tesseract/wiki).

- Required Python packages:
  ```bash
  pip install -r requirements.txt
  ```

  Your `requirements.txt` should include:
  - gradio
  - pytesseract
  - pillow (for image handling)
  - numpy

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ajaynair710/OCR-and-Document-Search-Web-Application.git
   cd OCR-and-Document-Search-Web-Application
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Tesseract**:
   - For Linux:
     ```bash
     sudo apt-get install tesseract-ocr
     ```
   - For Windows:
     [Download and install Tesseract](https://github.com/tesseract-ocr/tesseract/wiki).

   Make sure Tesseract is added to your system's PATH.

4. **Run the Application**:
   ```bash
   python app.py
   ```

   The app will run on a local server, and you can access it by navigating to the local URL provided in the console, typically `http://0.0.0.0:7860`.

## Usage

1. **Upload a Document or Image**:
   - Open the app in your browser, and upload an image or document that contains text you want to extract.

2. **Text Extraction**:
   - Once the document is uploaded, the app will process it using the Tesseract OCR engine and display the extracted text on the screen.

3. **Search**:
   - Use the search bar to find specific keywords within the extracted text.

## Troubleshooting

- **TesseractNotFoundError**: If you encounter the `TesseractNotFoundError`, ensure Tesseract is installed correctly and added to your system's PATH.
  
  For Linux:
  ```bash
  sudo apt-get install tesseract-ocr
  ```

  For Windows:
  Add Tesseract's installation directory (e.g., `C:\Program Files\Tesseract-OCR\`) to your system's PATH.

- **OCR Accuracy**: OCR accuracy depends on the quality of the uploaded images. Higher resolution images tend to yield better results.

## Future Enhancements

- **PDF Support**: Add the ability to process and extract text from multi-page PDF documents.
- **Text Export**: Allow users to download the extracted text as a `.txt` or `.docx` file.
- **Advanced Search**: Implement advanced search filters such as case sensitivity, regex matching, and proximity searches.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.
