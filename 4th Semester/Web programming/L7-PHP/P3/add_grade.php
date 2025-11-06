<?php
session_start();
if (!isset($_SESSION['id']) || $_SESSION['role'] !== 'teacher') {
    header("Location: index.html");
    exit;
}

$mysqli = new mysqli("localhost", "root", "", "lab-PHP");
if ($mysqli->connect_error) {
    exit('DB connection failed');
}

if (!isset($_POST['subject'], $_POST['student'], $_POST['grade']) ||
    !is_numeric($_POST['grade']) || $_POST['grade'] < 1 || $_POST['grade'] > 10) {
    $_SESSION['message'] = "Valoare notă invalidă!";
    $_SESSION['msg_type'] = "error";
    header("Location: teacher_view.php");
    exit;
}

$subject = intval($_POST['subject']);
$student = intval($_POST['student']);
$grade = intval($_POST['grade']);

$sql = "INSERT INTO grades (subject_id, student_id, grade) VALUES (?, ?, ?)";
$stmt = $mysqli->prepare($sql);
$stmt->bind_param("iii", $subject, $student, $grade);

if ($stmt->execute()) {
    $_SESSION['message'] = "Notă adăugată cu succes!";
    $_SESSION['msg_type'] = "success";
} else {
    $_SESSION['message'] = "Eroare la adăugarea notei.";
    $_SESSION['msg_type'] = "error";
}

header("Location: teacher_view.php");
exit;
?>
