<?php
session_start();
require 'db.php';
require 'csrf.php';
if ($_SERVER['REQUEST_METHOD'] === 'POST' && verify_csrf_token($_POST['csrf_token'])) {
    $stmt = $db->prepare("SELECT filename FROM photos WHERE id = ? AND user_id = ?");
    $stmt->bind_param("ii", $_POST['photo_id'], $_SESSION['user_id']);
    $stmt->execute();
    $stmt->bind_result($filename);
    if ($stmt->fetch()) {
        unlink("uploads/" . $filename);
        $db->query("DELETE FROM photos WHERE id = " . intval($_POST['photo_id']));
    }
}
header("Location: profile.php");