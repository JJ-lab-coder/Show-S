<?php
function execute_SQL($sql = "", $param = []) {

    require_once __DIR__."/database_connection.php";
    
    try {
        $conn = database_connection();
        $result = $conn->prepare($sql);
        $result->execute($param); 

        return $result->fetchAll(PDO::FETCH_ASSOC);
 
    } catch( PDOException $e ) {
        $error = "SQL Error: " . $e->getMessage();
        echo json_encode($error);
        exit();
    }
}