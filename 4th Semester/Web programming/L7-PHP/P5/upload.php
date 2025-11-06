<?php
session_start();
require 'db.php';
require 'csrf.php';
if (!isset($_SESSION['user_id'])) { header("Location: index.php"); exit; }
if ($_SERVER['REQUEST_METHOD'] === 'POST' && verify_csrf_token($_POST['csrf_token'])) {
    if (isset($_FILES['photo']) && $_FILES['photo']['error'] === UPLOAD_ERR_OK) {
        $type = mime_content_type($_FILES['photo']['tmp_name']);
        if (in_array($type, ['image/jpeg', 'image/png']) && $_FILES['photo']['size'] <= 2*1024*1024) {
            $ext = pathinfo($_FILES['photo']['name'], PATHINFO_EXTENSION);
            $name = uniqid() . "." . $ext;
            move_uploaded_file($_FILES['photo']['tmp_name'], "uploads/" . $name);
            $stmt = $db->prepare("INSERT INTO photos (user_id, filename) VALUES (?, ?)");
            $stmt->bind_param("is", $_SESSION['user_id'], $name);
            $stmt->execute();
        }
    }
}
header("Location: profile.php");