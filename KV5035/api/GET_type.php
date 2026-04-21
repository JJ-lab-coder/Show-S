<?php
function GET_type() {

    require_once __DIR__ . '/database/execute_SQL.php';

    $sql = "SELECT id, name FROM type";
    $param = [];

    $data = execute_SQL($sql, $param);
    echo json_encode($data);
}