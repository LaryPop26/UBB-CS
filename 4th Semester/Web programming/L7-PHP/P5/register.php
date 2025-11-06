<?php
session_start();
require 'db.php';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $username = $_POST['username'];
    $password = password_hash($_POST['password'], PASSWORD_DEFAULT);

    $stmt = $db->prepare("INSERT INTO users (username, password) VALUES (?, ?)");
    $stmt->bind_param("ss", $username, $password);
    if ($stmt->execute()) {
        header("Location: index.php");
        exit;
    } else {
        $error = "Utilizator deja existent.";
    }
}
?>
<!DOCTYPE html>
<html><head><title>Înregistrare</title><link rel="stylesheet" href="styles.css"></head>
<body>
<h2>Înregistrare</h2>
<?php if (isset($error)) echo "<p>$error</p>"; ?>
<form method="POST">
  <label>Utilizator: <input type="text" name="username" required></label><br>
  <label>Parola: <input type="password" name="password" required></label><br>
  <button type="submit">Înregistrare</button>
</form>
</body></html>