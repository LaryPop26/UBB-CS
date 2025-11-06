<?php
include 'config.php';

$id = isset($_POST['id']) ? intval($_POST['id']) : 0;
$nume = mysqli_real_escape_string($conn, $_POST['nume']);
$prenume = mysqli_real_escape_string($conn, $_POST['prenume']);
$telefon = mysqli_real_escape_string($conn, $_POST['telefon']);
$email = mysqli_real_escape_string($conn, $_POST['email']);

$sql = "UPDATE people SET nume='$nume', prenume='$prenume', telefon='$telefon', email='$email' WHERE id=$id";

if (mysqli_query($conn, $sql)) {
    echo "OK";
} else {
    http_response_code(500);
    echo "Error: " . mysqli_error($conn);
}
?>
