import os
from flask import Flask, render_template, request, redirect, url_for, send_file
from werkzeug.utils import secure_filename
import pytesseract
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app.config['UPLOAD_FOLDER'] = os.path.join(BASE_DIR, 'uploads')
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(image_path)

        # Convert the image to PDF
        pdf_path = convert_image_to_pdf(image_path)

        # Send the PDF file back to the user
        return send_file(pdf_path, as_attachment=True)

    return redirect(url_for('index'))

def convert_image_to_pdf(image_path):
    # Extract the filename without extension and set PDF path
    pdf_filename = os.path.splitext(os.path.basename(image_path))[0] + '.pdf'
    pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], pdf_filename)

    # OCR extraction
    text = pytesseract.image_to_string(Image.open(image_path))

    # Generate the PDF
    c = canvas.Canvas(pdf_path, pagesize=letter)
    width, height = letter
    y = height - 40  # Start position for text

    # Write each line of text to the PDF
    for line in text.split('\n'):
        c.drawString(40, y, line)
        y -= 12  # Move down the page for the next line

    c.save()
    return pdf_path

if __name__ == "__main__":
    # Ensure the uploads folder exists
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(host='0.0.0.0', port=5000)

