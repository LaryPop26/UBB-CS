<?php
session_start();
require 'db.php';
require 'csrf.php';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $username = $_POST['username'];
    $password = $_POST['password'];

    $stmt = $db->prepare("SELECT id, password FROM users WHERE username = ?");
    $stmt->bind_param("s", $username);
    $stmt->execute();
    $stmt->store_result();
    if ($stmt->num_rows === 1) {
        $stmt->bind_result($id, $hashed_password);
        $stmt->fetch();
        if (password_verify($password, $hashed_password)) {
            $_SESSION['user_id'] = $id;
            $_SESSION['username'] = $username;
            header("Location: profile.php");
            exit;
        }
    }
    $error = "Date invalide.";
}
?>
<!DOCTYPE html>
<html><head><title>Login</title><link rel="stylesheet" href="styles.css"></head>
<body>
<h2>Autentificare</h2>
<?php if (isset($error)) echo "<p>$error</p>"; ?>
<form method="POST">
  <label>Utilizator: <input type="text" name="username" required></label><br>
  <label>Parola: <input type="password" name="password" required></label><br>
  <button type="submit">Login</button>
</form>
<a href="register.php">Înregistrare</a>
</body></html>