<?php

use thiagoalessio\TesseractOCR\TesseractOCR;
use GuzzleHttp\Client;

require __DIR__ . '/vendor/autoload.php';

// echo (new TesseractOCR('../fiscalimpact1.png'))
//     ->run();

//use this..
// $ocr = new TesseractOCR();
// $ocr->image('../fiscalimpact1.png');
// $ocr->psm(6);
// $ocr->setOutputFile('./impact2.text');
// $ocr->run();

// $ocr = new TesseractOCR();
// $ocr->image('../fiscalimpact1.png');
// $ocr->tsv();
// $ocr->setOutputFile('./impact.tsv');
// $ocr->run();

//echo"<h4>Completed!!!</h4>";


//$url = 'http://localhost:8000/dep';
// returns null.
// $data = [
//     'text' => 'They ate the pizza with anchovies',
//     "model" => "en",
//     "collapse_punctuation" => 0,
//     "collapse_phrases" => 1
// ];
// $response = httpPost($url, $data);
// var_dump(json_decode($response));
// //using php curl (sudo apt-get install php-curl) 
// function httpPost($url, $data){
//     $curl = curl_init($url);
//     curl_setopt($curl, CURLOPT_POST, true);
//     curl_setopt($curl, CURLOPT_POSTFIELDS, http_build_query($data));
//     curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
//     $response = curl_exec($curl);
//     curl_close($curl);
//     return $response;
// }
//curl -s localhost:8000/dep -d '{"text":"Pastafarians are smarter than people with Coca Cola bottles.", "model":"en"}'


// {
//     "text": "They ate the pizza with anchovies",
//     "model": "en",
//     "collapse_punctuation": 0,
//     "collapse_phrases": 1
//   }

// $client = new \GuzzleHttp\Client();
// $response = $client->request('GET', 'https://api.github.com/repos/guzzle/guzzle');

// echo $response->getStatusCode(); // 200
// echo $response->getHeaderLine('content-type'); // 'application/json; charset=utf8'
// echo $response->getBody(); // '{"id": 1420053, "name": "guzzle", ...}'

// url = "http://localhost:8000/dep"
// message_text = "They ate the pizza with anchovies"
// headers = {'content-type': 'application/json'}
// d = {'text': message_text, 'model': 'en'}

// response = requests.post(url, data=json.dumps(d), headers=headers)
// r = response.json()
// Dependencies
///$url = 'http://localhost:8000/dep';
// Entities
//$url = 'http://localhost:8000/ent';
 // Sentences
//$url = 'http://localhost:8000/sents';
// sentences and depencies
//$url = 'http://localhost:8000/sents_dep';

$url = 'http://localhost:8000/dep';


//$text = 'They ate the pizza with anchovies';
//$text = 'When Sebastian Thrun started working on self-driving cars at Google in 2007, few people outside of the company took him seriously.';
// /ent: { "end": 14, "start": 5, "text": "Sebastian", "type": "NORP" }, { "end": 67, "start": 61, "text": "Google", "type": "ORG" }, { "end": 75, "start": 71, "text": "2007", "type": "DATE" }
// /sents: [ "When Sebastian Thrun started working on self-driving cars at Google in 2007, few people outside of the company took him seriously." ]

//$text = file_get_contents('./impactsimple.text');
//$text = 'Bill Number: H. 3020';
//$text = 'Author: MeCravy';
$text = 'Subject: SC Fetal Heartbeat Protection from Abortion Act';
$text = 'Summary: The large disc shaped object was seen hovering over New York City. Many assumed it was a UFO.';

$data = [
    'text' => $text,
    'model' => 'en',
    'collapse_punctuation' => 1,
    "collapse_phrases" => 1
];

//echo "<h4>guzzling</h4>";
//http://docs.guzzlephp.org/en/stable/
$client = new \GuzzleHttp\Client();
$headers = [
    'Content-type' => 'application/json; charset=utf-8',
    'Accept' => 'application/json',
    //'Authorization' => 'Basic ' . base64_encode($username . ':' . $password),
];

$response = $client->request('POST', $url, [
    'body' => json_encode($data)
]);
//echo $response->getStatusCode(); // 200
//echo $response->getHeaderLine('content-type'); // 'application/json; charset=utf8'
echo"<pre>";
echo $response->getBody(); 
echo"</pre>";