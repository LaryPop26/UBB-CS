<?php
include 'config.php';

$id = isset($_GET['id']) ? intval($_GET['id']) : 0;

$sql = "SELECT * FROM people WHERE id = $id LIMIT 1";
$result = mysqli_query($conn, $sql);

if ($row = mysqli_fetch_assoc($result)) {
    header('Content-Type: application/json');
    echo json_encode($row);
} else {
    echo json_encode([]);
}
?>
