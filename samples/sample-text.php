<?php
# Example of sending text.
# run locally with:
# php -S localhost:8080
# Then access at http://localhost:8080/sample.php

use GuzzleHttp\Client;

require __DIR__ . '/vendor/autoload.php';

$url = 'http://localhost:5000/api/annotate/sentences';

//http://docs.guzzlephp.org/en/stable/
$client = new \GuzzleHttp\Client();

$text = 'Summary: On July 4th, 1998 a large disc shaped object was seen hovering over New York City. Many assumed it was a UFO. However, it turned out to be a hot air balloon';

$data = [
  'text' => $text,
  'model' => 'en',
  'collapse_punctuation' => 1,
  "collapse_phrases" => 1
];

//http://docs.guzzlephp.org/en/stable/
$client = new \GuzzleHttp\Client();
$headers = [
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
];

$response = $client->request('POST', $url, [
  'headers' => $headers,
  'body' => json_encode($data)
]);

//echo $response->getStatusCode(); // 200
//echo $response->getHeaderLine('content-type'); // 'application/json; charset=utf8'
echo"<pre>";
echo $response->getBody(); 
echo"</pre>";
