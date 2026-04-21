<?php
header('Content-Type: application/json');
header('Access-Control-Allow-Origin: *');

$data = [
    "module" => "KV5035 Software Architecture",
    "developer" => "Jonathan"
];

echo json_encode($data);