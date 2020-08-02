# A Docker environment for working with Tesseract (Pytesseract) and Spacy.

## Overview
Provides dockerized access to:
* Tesseract (via pytesseract)
* Spacy

NOTE: this is built for local development, and not really suited to production environments yet.

## Installation and Setup
Clone this repo.

```docker-compose build```
```docker-compose up```

## Usage / API

#### OCR
Uses tesseract to retrieve the text from an image.
These endpoints are available at:
http://localhost:5000

```/api/ocr [POST]```

Make a post request to this endpoint with an image file.

Returns json with:
'lines': An array of each line of text in the image.
'text': The entire text of the image.

