from werkzeug import secure_filename
import os
import sys

UPLOAD_FOLDER = './uploads'

# 10485760 bytes = 10.48576mb
MAX_CONTENT_LENGTH = 10 * 1024 * 1024
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'pdf'])

def upload_file(request):
  """
  This function will handle the upload a file and return of the extracted text via tesseract.
  No spacy or other processing will be done.
  """
  if request.method == 'POST':

    if 'file' not in request.files:
      return jsonify(error='No file provided with key of "file" found')

    file = request.files['file']
    
    if file.filename == '':
      return jsonify(error='No file provided with key of "file" found')

    if file and allowed_file_type(file.filename):
      filename = secure_filename(file.filename)
      # save file to /uploads
      filepath = os.path.join(UPLOAD_FOLDER, filename)
      file.save(filepath)

      return filepath


# function to check the file extension
def allowed_file_type(filename):
  return '.' in filename and \
    filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS