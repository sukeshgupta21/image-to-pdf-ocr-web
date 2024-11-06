# Base image with Python
FROM python:3.8-slim

# Install necessary system packages for OCR
RUN apt-get update && \
    apt-get install -y tesseract-ocr && \
    apt-get clean

# Set up the working directory
WORKDIR /app

# Copy app code to container
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port for Flask
EXPOSE 5000

# Run the application
CMD ["python", "app/main.py"]

