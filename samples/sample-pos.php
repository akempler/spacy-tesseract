<?php
# Example of sending text and having spacy return pos tagging.
# run locally with:
# php -S localhost:8080
# Then access at http://localhost:8080/sample.php

use GuzzleHttp\Client;

require __DIR__ . '/vendor/autoload.php';

// https://spacy.io/usage/linguistic-features#pos-tagging
// https://spacy.io/api/annotation#pos-tagging 
$url = 'http://localhost:5000/api/annotate/pos_entities';

// http://docs.guzzlephp.org/en/stable/
$client = new \GuzzleHttp\Client();

$text = 'Amended by the House of Representatives on February 28, 2020';

$data = [
  'text' => $text,
  'model' => 'en',
  'collapse_punctuation' => 1,
  "collapse_phrases" => 1
];

$client = new \GuzzleHttp\Client();
$headers = [
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
];

$response = $client->request('POST', $url, [
  'headers' => $headers,
  'body' => json_encode($data)
]);

echo"<pre>";
echo $response->getBody(); 
echo"</pre>";
