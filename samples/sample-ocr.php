<?php
# Example of sending an image or pdf file.
# run locally with:
# php -S localhost:8080
# Then access at http://localhost:8080/sample-ocr.php

use GuzzleHttp\Client;

require __DIR__ . '/vendor/autoload.php';

$url = 'http://localhost:5000/api/ocr';

//http://docs.guzzlephp.org/en/stable/
$client = new \GuzzleHttp\Client();

$options = [
    'multipart' => [
        [
            'name' => 'file',
            //'contents' => fopen('./images/fiscalimpact1.png', 'r'),
            'contents' => fopen('./pdf/H3485-2019-01-09-introduced.pdf', 'r'),
            'filename' => 'H3485-2019-01-09-introduced.pdf',
        ]
    ],
];
$response = $client->post($url, $options);

//echo $response->getStatusCode(); // 200
//echo $response->getHeaderLine('content-type'); // 'application/json; charset=utf8'
echo"<pre>";
echo $response->getBody(); 
echo"</pre>";