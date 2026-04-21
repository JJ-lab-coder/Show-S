<?php
header('Content-Type: application/json');
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: GET');

require_once __DIR__. '/database/execute_SQL.php';

$sql = "SELECT 
            a.id AS author_id,
            a.name
        FROM author a 
        LEFT JOIN presentation_has_author pha ON a.id = pha.author_id
        WHERE 1=1";

$param = [];

if (!empty($_GET['author-id'])) {
    $sql .= " AND a.id = :aid";
    $param[':aid'] = $_GET['author-id'];
}
if (!empty($_GET['presentation-id'])) {
    $sql .= " AND pha.presentation_id = :pid";
    $param[':pid'] = $_GET['presentation-id'];
}

$page = $_GET['page'] ?? '';
$size = $_GET['size'] ?? '';

if (!empty($size) && $page === '') {
    $page = 1;
}

if (!empty($page) || $page === '0') {

    if (!is_numeric($page)) {
        http_response_code(400);
        echo json_encode("page must be an integer");
        exit();

    }

    if ($page <= 0) {
        http_response_code(400);
        echo json_encode("page must be greater that 0");
        exit();
    }

if (!empty($size) || $size === '0') {

    if (!is_numeric($size)) {
        http_response_code(400);
        echo json_encode("size must be an integer");
        exit();

    }

    if ($page <= 0) {
        http_response_code(400);
        echo json_encode("page must be greater that 0");
        exit();
    }
    
} else {
    $size = 10;
}

    $offset = ($page - 1) * $size;
    $sql .= " ORDER BY presentation_id LIMIT $size OFFSET $offset";
}

$data = execute_SQL($sql, $param);

echo json_encode($data);