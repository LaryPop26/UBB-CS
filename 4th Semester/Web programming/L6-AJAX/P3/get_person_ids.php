<?php
include 'config.php';

$sql = "SELECT id FROM people ORDER BY id ASC";
$result = mysqli_query($conn, $sql);

$ids = [];
while ($row = mysqli_fetch_assoc($result)) {
    $ids[] = $row;
}

header('Content-Type: application/json');
echo json_encode($ids);
?>
