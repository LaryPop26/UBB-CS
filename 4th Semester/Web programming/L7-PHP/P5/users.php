<?php
session_start();
require 'db.php';
if (!isset($_SESSION['user_id'])) { header("Location: index.php"); exit; }

$users = $db->query("SELECT id, username FROM users WHERE id != " . $_SESSION['user_id']);
?>
<!DOCTYPE html>
<html><head><title>Utilizatori</title><link rel="stylesheet" href="styles.css"></head>
<body>
<h2>Alți utilizatori</h2>
<a href="profile.php">Înapoi la profil</a>
<ul>
<?php while ($user = $users->fetch_assoc()): ?>
  <li>
    <?= htmlspecialchars($user['username']) ?>
    <div>
    <?php
    $stmt = $db->prepare("SELECT filename FROM photos WHERE user_id = ?");
    $stmt->bind_param("i", $user['id']);
    $stmt->execute();
    $photos = $stmt->get_result();
    while ($p = $photos->fetch_assoc()): ?>
        <img src="uploads/<?= htmlspecialchars($p['filename']) ?>">
    <?php endwhile; ?>
    </div>
  </li>
<?php endwhile; ?>
</ul>
</body></html>