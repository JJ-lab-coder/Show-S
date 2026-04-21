<?php
function POST_type() {

    require_once __DIR__ . '/database/execute_SQL.php';

    $request_body = file_get_contents('php://input');
    $request_body = json_decode($request_body, true);
 
    if ($request_body === null) { 
        http_response_code(400); 
        echo json_encode("Error: Invalid JSON in request body"); 
        exit(); 
    }

    if (!array_key_exists('name', $request_body)) {
        http_response_code(400);
        echo json_encode("Error: name required");
        exit();
    }

    $name = $request_body['name'];

    $sql = "INSERT INTO type (name) VALUES (:name)";
    $param = ['name' => $name];

    execute_SQL($sql, $param);

    http_response_code(201);
    echo json_encode("TYPE  created");
}