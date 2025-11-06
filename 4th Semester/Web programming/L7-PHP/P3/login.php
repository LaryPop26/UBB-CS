<?php
session_start();

$mysqli = new mysqli("localhost", "root", "", "lab-PHP");
if ($mysqli->connect_error) {
    exit('Could not connect to DB');
}

function test_input($data) {
    return htmlspecialchars(stripslashes(trim($data)));
}

if (!isset($_POST['username'], $_POST['password'])) {
    $_SESSION['error'] = "Completați toate câmpurile.";
    header("Location: index.php");
    exit;
}

$username = test_input($_POST['username']);
$password = test_input($_POST['password']);

$sql = "SELECT id, password FROM teachers WHERE username = ?";
$stmt = $mysqli->prepare($sql);
$stmt->bind_param('s', $username);
$stmt->execute();
$result = $stmt->get_result()->fetch_assoc();

if ($result && $result['password'] === $password) {
    $_SESSION['id'] = $result['id'];
    $_SESSION['username'] = $username;
    $_SESSION['role'] = 'teacher';
    header("Location: teacher_view.php");
    exit;
}

$sql = "SELECT id, password FROM students WHERE username = ?";
$stmt = $mysqli->prepare($sql);
$stmt->bind_param('s', $username);
$stmt->execute();
$result = $stmt->get_result()->fetch_assoc();

if ($result && $result['password'] === $password) {
    $_SESSION['id'] = $result['id'];
    $_SESSION['username'] = $username;
    $_SESSION['role'] = 'student';
    header("Location: student_view.php");
    exit;
}

$_SESSION['error'] = "Username sau parolă incorecte.";
header("Location: index.php");
exit;
