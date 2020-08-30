import functools
from flask import Flask, Blueprint, render_template, request, jsonify
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import os
import sys
import re
from utils import upload_file, request_data_type
import json

import spacy
from spacy import displacy
from spacy.matcher import PhraseMatcher
import numpy as np
from tesseract import ocr_core

bp = Blueprint('spacynlp', __name__, url_prefix='/api')

def set_custom_boundaries(doc):
  for token in doc[:-1]:
    if token.text == ":" and doc[token.i-1].text in bp.phrases:
      doc[token.i+1].is_sent_start = False
      doc[token.i].is_sent_start = False
      # TODO can also check if prev is a match for the phrase_list.
      prev = doc[token.i-1]
  return doc

@bp.route('/annotate/sentences', methods = ['POST'])
def annotate_sentences():
  """
  This function will handle the upload a file and return the spacy sentences.
  """

  datatype = request_data_type(request)

  if datatype == 'file':
    filepath = upload_file(request)
    text = ocr_core(filepath)
  elif datatype == 'text':
    req_data = request.get_json()
    text = req_data['text']
  else:
    return jsonify(msg='No valid file or text found.')

  nlp = spacy.load("en_core_web_md")

  phrase_list = request.form.get("phrase_list")
  if phrase_list is not None:
    phrases = json.loads(phrase_list)
    bp.phrases = phrases
    matcher = PhraseMatcher(nlp.vocab)
    phrase_patterns = [nlp(text) for text in phrases]
    matcher.add('InfoItems', None, *phrase_patterns)
    nlp.add_pipe(set_custom_boundaries, before="parser")

  doc = nlp(text)
  sentences = []
  sents = list(doc.sents)
  for s in sents:
    sentences.append(s.text)

  return jsonify(sentences=sentences)

@bp.route('/annotate/entities', methods = ['POST'])
def annotate_entities():
  """
  This function will handle the upload a file and return spacy entities.
  """

  datatype = request_data_type(request)

  if datatype == 'file':
    filepath = upload_file(request)
    text = ocr_core(filepath)
  elif datatype == 'text':
    req_data = request.get_json()
    text = req_data['text']
  else:
    return jsonify(msg='No valid file or text found.')

  entities = []
  nlp = spacy.load("en_core_web_md")
  doc = nlp(text)
  for ent in doc.ents:
    info = [ent.text, ent.start_char, ent.end_char, ent.label_]
    entities.append(info)

  return jsonify(entities=entities)