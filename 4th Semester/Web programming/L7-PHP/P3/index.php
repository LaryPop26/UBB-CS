<?php session_start(); ?>
<!DOCTYPE html>
<html>
<head><title>Login</title></head>
<body>
  <?php
  if (isset($_SESSION['error'])) {
      echo '<p style="color:red;">' . htmlspecialchars($_SESSION['error']) . '</p>';
      unset($_SESSION['error']);
  }
  ?>
  <form method="POST" action="login.php" style="display:flex; flex-direction:column; max-width:200px;">
    <input type="text" name="username" placeholder="username" required />
    <input type="password" name="password" placeholder="password" required />
    <input type="submit" value="Log in" />
  </form>
</body>
</html>
