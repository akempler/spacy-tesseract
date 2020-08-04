from flask import Flask, render_template, request, jsonify
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import os
import sys
import re
from utils import upload_file
import json

import spacy
from spacy import displacy
from spacy.matcher import PhraseMatcher

app = Flask(__name__)
app.debug = True

def ocr_core(filepath):
    """
    This function will handle the core OCR processing of images.
    """
    text = pytesseract.image_to_string(Image.open(filepath)) 
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

@app.route('/api/ocr', methods = ['POST'])
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

def set_custom_boundaries(doc):
  for token in doc[:-1]:
    if token.text == ":" and doc[token.i-1].text in app.phrases:
      doc[token.i+1].is_sent_start = False
      doc[token.i].is_sent_start = False
      # TODO can also check if prev is a match for the phrase_list.
      prev = doc[token.i-1]
  return doc

@app.route('/api/annotate/sentences', methods = ['POST'])
def annotate_file():
  """
  This function will handle the upload a file and return the spacy sentences.
  """

  filepath = upload_file(request)

  extracted_text = ocr_core(filepath)

  nlp = spacy.load("en_core_web_md")

  phrase_list = request.form.get("phrase_list")
  if phrase_list is not None:
    phrases = json.loads(phrase_list)
    app.phrases = phrases
    matcher = PhraseMatcher(nlp.vocab)
    phrase_patterns = [nlp(text) for text in phrases]
    matcher.add('InfoItems', None, *phrase_patterns)
    nlp.add_pipe(set_custom_boundaries, before="parser")

  doc = nlp(extracted_text)
  sentences = []
  sents = list(doc.sents)
  for s in sents:
    sentences.append(s.text)

  return jsonify(sentences=sentences)

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=5000, debug=True)
