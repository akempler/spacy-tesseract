<?php
# run locally with:
# php -S localhost:8000

use GuzzleHttp\Client;

require __DIR__ . '/vendor/autoload.php';

$url = 'http://localhost:5000/api/annotate/sentences';

//http://docs.guzzlephp.org/en/stable/
$client = new \GuzzleHttp\Client();

$options = [
    'multipart' => [
        [
            'name' => 'file',
            'contents' => fopen('./images/fiscalimpact1.png', 'r'),
            'filename' => 'eurotext.png',
        ],
        [
            'name' => 'phrase_list',
            'contents' => json_encode(['Subject', 'Author', 'Bill Number', 'Requestor'])
        ]
    ],
];
$response = $client->post($url, $options);

//echo $response->getStatusCode(); // 200
//echo $response->getHeaderLine('content-type'); // 'application/json; charset=utf8'
echo"<pre>";
echo $response->getBody(); 
echo"</pre>";