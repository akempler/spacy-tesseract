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
These endpoints are available at:
http://localhost:5000

### OCR / Tesseract
Uses tesseract to retrieve the text from an image.

#### `POST` `/api/ocr`

```
{
  "file": A source pdf file
}
```

Name | Type | Description
------------ | ------------- | -------------
file | file resource | The file to process for text.
psm | page segmentation mode | Which psm mode to use. Defaults to 3.
oem | engine mode | Which engine mode to use. Defaults to 3.


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

Detailed example, specifying a different psm:

```
<?php

use GuzzleHttp\Client;
require __DIR__ . '/vendor/autoload.php';

$url = 'http://localhost:5000/api/ocr';
$client = new \GuzzleHttp\Client();

$options = [
    'multipart' => [
        [
            'contents' => fopen('./pdf/H3485-2019-01-09-introduced.pdf', 'r'),
            'filename' => 'H3485-2019-01-09-introduced.pdf',
        ],
        [
            'name' => 'psm',
            'contents' => json_encode('11')
        ]
    ],
];
$response = $client->post($url, $options);

echo $response->getStatusCode(); // 200
echo"<pre>";
echo $response->getBody(); 
echo"</pre>";
```

Response:
```
{
  "lines": [
    "SOUTH CAROLINA REVENUE AND FISCAL AFFAIRS OFFICE",
    "STATEMENT OF ESTIMATED FISCAL IMPACT",
    "(803)734-0640 » RFA.SC.GOV/IMPACTS",
    "Bill Number:",
    "H. 3020",
    "Introduced on January 8, 2019",
    "Author:",
    "MeCravy",
    "Subject:",
    "SC Fetal Heartbeat Protection from Abortion Act",
    "Requestor:",
    "House Judiciary",
    "RFA Analyst(s):",
    "Griffith and Gardner",
    "Impact Date:",
    "April 4, 2019",
    "Fiscal Impact Summary",
    "This bill will have no expenditure impact on the General Fund, Federal Funds, or Other Funds",
  ],
    "text": "SOUTH CAROLINA REVENUE AND FISCAL AFFAIRS OFFICE STATEMENT OF ESTIMATED FISCAL IMPACT (803)734-0640 » RFA.SC.GOV/IMPACTS Bill Number: H. 3020 Introduced on January 8, 2019 Author: MeCravy Subject: SC Fetal Heartbeat Protection from Abortion Act Requestor: House Judiciary RFA Analyst(s): Griffith and Gardner Impact Date: April 4, 2019 Fiscal Impact Summary This bill will have no expenditure impact on the General Fund, Federal Funds, or Other Funds becat any additional expenses relating to the promulgation..."
}
```

---

### Spacy NLP
Uses Spacy nlp to retrieve information about text.  

Can provide an image, pdf or a text string to these endpoints. 
You must provide one or the other of these. If both are present, the pdf will be used as the source.

#### `POST` `/api/annotate/sentences`

```
{
  "file": A source pdf file, <br/>
  "text": Text to process (instead of a file).
}
```

Name | Type | Description
------------ | ------------- | -------------
file | file resource | The file to process for text.
text | Text string | The text to process.

Example response:

```
{
  "sentences": [
    "SOUTH CAROLINA REVENUE AND FISCAL AFFAIRS OFFICE\n\n",
    "STATEMENT OF ESTIMATED FISCAL IMPACT\n",
    "(803)734-0640 » RFA.SC.GOV/IMPACTS,\n\n \n\n \n\n",
    "Bill Number: H. 3020 _",
    "Introduced on January 8, 2019\n\n",
    "Author: MeCravy\n",
    "Subject:",
    "Income Tax Credit, Rehabilitation Expenditures for Historic Structures",
    "Requestor:",
    "House Judiciary\n\nRFA Analyst(s)",
    ": Griffith and Gardner\nImpact Date:___April 4, 2019\n\n \n\n",
    "Fiscal Impact Summary\n\n",
  ]
}
```

See /samples/sample.php for an example using GuzzleHttp.

#### `POST` `/api/annotate/entities`

```
{
  "file": A source pdf file, <br/>
  "text": On July 4th, 1998 a large disc shaped object was seen hovering over New York City. Spotted by David Templer, he assumed it was a UFO. However, it turned out to be a hot air balloon.
}
```
NOTE: provide EITHER a file or text:

Name | Type | Description
------------ | ------------- | -------------
file | file resource | The file to process for text.
text | Text string | The text to process (instead of a file).

Example response:

```
{
  "entities": [
    [
      "July 4th, 1998",
      12,
      26,
      "DATE"
    ],
    [
      "New York City",
      77,
      90,
      "GPE"
    ],
    [
      "David Templer",
      103,
      115,
      "PERSON"
    ]
  ]
}
```

#### `POST` `/api/annotate/pos`

Proivdes PoS (part of speech) tagging using Spacy.

@see https://spacy.io/usage/linguistic-features#pos-tagging  
@see https://spacy.io/api/annotation#pos-tagging

```
{
  "file": A source pdf file, <br/>
  "text": On July 4th, 1998 a large disc shaped object was seen hovering over New York City. Spotted by David Templer, he assumed it was a UFO. However, it turned out to be a hot air balloon.
}
```
NOTE: provide EITHER a file or text:

Name | Type | Description
------------ | ------------- | -------------
file | file resource | The file to process for text.
text | Text string | The text to process (instead of a file).

Example response, with the following data for each item (for the first item below): 
* token text - "Amended"
* token lemma - "ammend"
* token PoS - "VERB" (https://spacy.io/api/annotation#pos-universal)
* token tag - "VBN" (verb, non-3rd person singular present, https://spacy.io/api/annotation#pos-en)
* token dependency - "ROOT" (https://spacy.io/api/annotation#dependency-parsing-english)

```
{
    "tokens": [
        [
            "Amended",
            "amend",
            "VERB",
            "VBN",
            "ROOT"
        ],
        [
            "by",
            "by",
            "ADP",
            "IN",
            "agent"
        ],
        [
            "the",
            "the",
            "DET",
            "DT",
            "det"
        ],
        [
            "House",
            "House",
            "PROPN",
            "NNP",
            "pobj"
        ],
        [
            "of",
            "of",
            "ADP",
            "IN",
            "prep"
        ],
        [
            "Representatives",
            "Representatives",
            "PROPN",
            "NNPS",
            "pobj"
        ],
        [
            "on",
            "on",
            "ADP",
            "IN",
            "prep"
        ],
        [
            "February",
            "February",
            "PROPN",
            "NNP",
            "pobj"
        ],
        [
            "28",
            "28",
            "NUM",
            "CD",
            "nummod"
        ],
        [
            ",",
            ",",
            "PUNCT",
            ",",
            "punct"
        ],
        [
            "2020",
            "2020",
            "NUM",
            "CD",
            "nummod"
        ]
    ]
}
```

#### `POST` `/api/annotate/entities_pos`

Proivdes PoS (part of speech) tagging and Named Entity Recognition using Spacy.

```
{
  "file": A source pdf file, <br/>
  "text": Amended by the House of Representatives on February 28, 2020.
}
```
NOTE: provide EITHER a file or text:

Name | Type | Description
------------ | ------------- | -------------
file | file resource | The file to process for text.
text | Text string | The text to process (instead of a file).

Sample Output:

```
{
    "entities": [
        [
            "the House of Representatives",
            11,
            39,
            "ORG"
        ],
        [
            "February 28, 2020",
            43,
            60,
            "DATE"
        ]
    ],
    "tokens": [
        [
            "Amended",
            "amend",
            "VERB",
            "VBN",
            "ROOT"
        ],
        [
            "by",
            "by",
            "ADP",
            "IN",
            "agent"
        ],
        [
            "the",
            "the",
            "DET",
            "DT",
            "det"
        ],
        [
            "House",
            "House",
            "PROPN",
            "NNP",
            "pobj"
        ],
        [
            "of",
            "of",
            "ADP",
            "IN",
            "prep"
        ],
        [
            "Representatives",
            "Representatives",
            "PROPN",
            "NNPS",
            "pobj"
        ],
        [
            "on",
            "on",
            "ADP",
            "IN",
            "prep"
        ],
        [
            "February",
            "February",
            "PROPN",
            "NNP",
            "pobj"
        ],
        [
            "28",
            "28",
            "NUM",
            "CD",
            "nummod"
        ],
        [
            ",",
            ",",
            "PUNCT",
            ",",
            "punct"
        ],
        [
            "2020",
            "2020",
            "NUM",
            "CD",
            "nummod"
        ]
    ]
}
```