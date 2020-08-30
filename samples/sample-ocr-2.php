<?php
# Example of sending a pdf file and running ocr with custom settings on it.
# run locally with:
# php -S localhost:8080
# Then access at http://localhost:8080/sample-ocr-2.php

use GuzzleHttp\Client;

require __DIR__ . '/vendor/autoload.php';

$url = 'http://localhost:5000/api/ocr';

//http://docs.guzzlephp.org/en/stable/
$client = new \GuzzleHttp\Client();

$options = [
    'multipart' => [
        [
            'name' => 'file',
            'contents' => fopen('./pdf/H3601-2019-02-28-amended.pdf', 'r'),
            'filename' => 'H3601-2019-02-28-amended.pdf',
        ],
        [
            'name' => 'psm',
            'contents' => json_encode('11')
        ]
    ],
];
$response = $client->post($url, $options);

echo"<pre>";
echo $response->getBody(); 
echo"</pre>";