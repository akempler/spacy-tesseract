from flask import request, jsonify
from werkzeug.utils import secure_filename
import os
import sys
import pdf2image

UPLOAD_FOLDER = './uploads'

# 10485760 bytes = 10.48576mb
MAX_CONTENT_LENGTH = 10 * 1024 * 1024
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'pdf'])

def upload_file(request):
  """
  Handle the upload a file. Can be an image or pdf.
  """
  if request.method == 'POST':

    # if 'file' not in request.files:
    #   return jsonify(error='No file provided with key of "file" found')

    file = request.files['file']
    
    if file.filename == '':
      return jsonify(error='No file provided with key of "file" found')

    if file and allowed_file_type(file.filename):
      filename = secure_filename(file.filename)
      # save file to /uploads
      filepath = os.path.join(UPLOAD_FOLDER, filename)
      file.save(filepath)

      file_name, file_extension = os.path.splitext(filename)

      if file_extension == '.pdf':
        pages = pdf2image.convert_from_path(pdf_path=filepath, dpi=200, size=(1654,2340))
        for i in range(len(pages)):
          filename = file_name + str(i) + '.jpg'
          filepath = os.path.join(UPLOAD_FOLDER, filename)
          print(filename, flush=True)
          print(filepath, flush=True)
          pages[i].save(filepath)
          # for now returning first page until TODO below.
          return filepath

      # TODO need to return an array of paths.
      return filepath


# function to check the file extension
def allowed_file_type(filename):
  return '.' in filename and \
    filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def request_data_type(request):
  """
  Check if either a file or text was provided to be proccessed.
  """

  req_data = request.get_json()

  if 'file' in request.files:
    return 'file'
  elif 'text' in req_data:
    return 'text'
  else:
    return 'false'