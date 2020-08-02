
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
from utils import test, upload_file


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

@app.route("/test")
def teststuff():
  return test()

# @app.route("/api/ocr")
# def image_ocr():
#   """
#   This function will handle the core OCR processing of images.
#   """
#   text = pytesseract.image_to_string(Image.open('./images/fiscalimpact1.png'))
#   return text

@app.route('/api/ocr', methods = ['GET', 'POST'])
def ocr():
  """
  This function will handle the upload a file and return of the extracted text via tesseract.
  No spacy or other processing will be done.
  """
  if request.method == 'POST':
    # if 'file' not in request.files:
    #   return jsonify(error='No file provided with key of "file" found')

    # file = request.files['file']
    
    # if file.filename == '':
    #   return jsonify(error='No file provided with key of "file" found')

    # if file and allowed_file_type(file.filename):

    #   filename = secure_filename(file.filename)
    #   # save file to /uploads
    #   filepath = os.path.join(app.config['UPLOAD_FOLDER'],filename)
    #   file.save(filepath)
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



#print("working!!!!!")
# from flask import Flask, render_template, request
# from werkzeug import secure_filename
# import os
# import sys
# from PIL import Image
# import pytesseract
# import argparse
# import cv2

# __author__ = 'Rick Torzynski <ricktorzynski@gmail.com>'
# __source__ = ''

# app = Flask(__name__)
# UPLOAD_FOLDER = './static/uploads'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 
# app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024

# @app.route("/")
# def index():
#   return render_template("index.html")

# @app.route("/about")
# def about():
#   return render_template("about.html")

# @app.route('/uploader', methods = ['GET', 'POST'])
# def upload_file():
#    if request.method == 'POST':
#       f = request.files['file']

#       # create a secure filename
#       filename = secure_filename(f.filename)

#       # save file to /static/uploads
#       filepath = os.path.join(app.config['UPLOAD_FOLDER'],filename)
#       f.save(filepath)
      
#       # load the example image and convert it to grayscale
#       image = cv2.imread(filepath)
#       gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
      
#       # apply thresholding to preprocess the image
#       gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

#       # apply median blurring to remove any blurring
#       gray = cv2.medianBlur(gray, 3)

#       # save the processed image in the /static/uploads directory
#       ofilename = os.path.join(app.config['UPLOAD_FOLDER'],"{}.png".format(os.getpid()))
#       cv2.imwrite(ofilename, gray)
      
#       # perform OCR on the processed image
#       text = pytesseract.image_to_string(Image.open(ofilename))
      
#       # remove the processed image
#       os.remove(ofilename)

#       return render_template("uploaded.html", displaytext=text, fname=filename)

# if __name__ == '__main__':
#    app.run(host="0.0.0.0", port=5000, debug=True)