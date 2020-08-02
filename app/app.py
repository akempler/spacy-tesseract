
from flask import Flask, render_template, request, jsonify
from werkzeug import secure_filename
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import os
import sys
import re
from utils import upload_file


app = Flask(__name__)


def ocr_core(filepath):
    """
    This function will handle the core OCR processing of images.
    """
    text = pytesseract.image_to_string(Image.open(filepath))  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text

@app.route("/")
def root():
  return jsonify(msg='success')

@app.route("/ui")
def home():
  return render_template('index.html')

@app.route("/ui/about")
def about():
  return render_template('about.html')

@app.route('/api/ocr', methods = ['GET', 'POST'])
def ocr():
  """
  This function will handle the upload a file and return of the extracted text via tesseract.
  No spacy or other processing will be done.
  """
  if request.method == 'POST':

    filepath = upload_file(request)

    extracted_text = ocr_core(filepath)
    lines = re.split('\n\n|\n',extracted_text)
    return jsonify(text=extracted_text, lines=lines)

@app.route('/api/annotate/sentences', methods = ['GET', 'POST'])
def annotate_file():
  """
  This function will handle the upload a file and return the spacy sentences.
  """

  return jsonify(msg='test')

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=5000, debug=True)
