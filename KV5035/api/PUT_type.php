<?php
function PUT_type() {

    require_once __DIR__ . '/database/execute_SQL.php';

    $request_body = file_get_contents('php://input');
    $request_body = json_decode($request_body, true);

    if ($request_body === null) { 
        http_response_code(400); 
        echo json_encode("Error: Invalid JSON in request body"); 
        exit(); 
    }

    if (!array_key_exists('type_id', $request_body)) {
        http_response_code(400);
        echo json_encode("Error id required");
        exit();
    }

    if (!array_key_exists('name', $request_body)) {
        http_response_code(400);
        echo json_encode("Error name required");
        exit();
    }

    $type_id = $request_body['type_id'];
    $name = $request_body['name'];

    $sql = "UPDATE type SET name = :name WHERE id = :id";
    $param = [
        ':name' => $name,
        ':id' => $type_id
    ];

    execute_SQL($sql, $param);

    http_response_code(200);
    echo json_encode("Type updated");
}
