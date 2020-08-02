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

#### `POST` `/api/ocr`

```
{
  "file": The source file
}
```

Name | Type | Description
------------ | ------------- | -------------
file | file resource | The file to process for text.


Example request using [GuzzleHttp](http://docs.guzzlephp.org/en/stable/):

```
$body = fopen('/path/to/file', 'r');
$r = $client->request('POST', 'http://localhost:5000/api/ocr', ['file' => $body]);
```

Example response:

```
{
  "lines": [
    "The (quick) [brown] {fox} jumps!",
    "Over the $43,456.78 <lazy> #90 dog",
    "& duck/goose, as 12.5% of E-mail",
    "from aspammer@website.com is spam.",
    "Der ,.schnelle” braune Fuchs springt",
    "iiber den faulen Hund. Le renard brun",
    "«rapide» saute par-dessus le chien",
    "paresseux. La volpe marrone rapida",
    "salta sopra il cane pigro. El zorro",
    "marron rapido salta sobre el perro",
    "perezoso. A raposa marrom rapida",
    "salta sobre o céo preguicoso."
  ],
  "text": "The (quick) [brown] {fox} jumps!\nOver the $43,456.78 <lazy> #90 dog\n& duck/goose, as 12.5% of E-mail\nfrom aspammer@website.com is spam.\nDer ,.schnelle” braune Fuchs springt\niiber den faulen Hund. Le renard brun\n«rapide» saute par-dessus le chien\nparesseux. La volpe marrone rapida\nsalta sopra il cane pigro. El zorro\nmarron rapido salta sobre el perro\nperezoso. A raposa marrom rapida\nsalta sobre o céo preguicoso."
}
```

