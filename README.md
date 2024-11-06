# OCR to PDF Web Application

This project is a Dockerized web application that converts images into PDFs after performing OCR (Optical Character Recognition) to extract text.

## Features

- **Upload**: Users can upload JPG or PNG images.
- **OCR Processing**: Extracts text from the uploaded image.
- **PDF Conversion**: Creates a PDF file with the image and extracted text.

## Technologies Used

- **Python** (Flask web framework)
- **Docker**
- **pytesseract** (OCR library)
- **reportlab** (PDF generation library)
- **Tesseract OCR Engine**

## Prerequisites

- **Docker** installed
- **Git** installed (for GitHub repository management)

## Installation and Usage

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ocr-to-pdf-app.git
cd ocr-to-pdf-app

