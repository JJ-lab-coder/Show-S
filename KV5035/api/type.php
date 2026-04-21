<?php
header('Content-Type: application/json');
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: GET, POST, PUT, PATCH, DELETE');

$request_method = $_SERVER['REQUEST_METHOD'];

switch ($request_method) {
    case 'GET':
        require_once 'GET_type.php';
        GET_type();
        break;

    case 'POST':
        require_once 'POST_type.php';
        POST_type();
        break;
    
    case 'PUT':
    case 'PATCH':
        require_once 'PUT_type.php';
        PUT_type();
        break;
    
    case 'DELETE':
        require_once 'DELETE_type.php';
        DELETE_type();
        break;
    
    case 'OPTIONS':
        http_response_code(200);
        break;

    default:
        http_response_code(405);
        echo json_encode("METHOD NOT Allowed");
        break;
}