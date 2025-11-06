<?php
session_start();
require 'db.php';
require 'csrf.php';
if (!isset($_SESSION['user_id'])) { header("Location: index.php"); exit; }
$id = $_SESSION['user_id'];
$stmt = $db->prepare("SELECT id, filename FROM photos WHERE user_id = ?");
$stmt->bind_param("i", $id);
$stmt->execute();
$result = $stmt->get_result();
?>
<!DOCTYPE html>
<html><head><title>Profilul Meu</title><link rel="stylesheet" href="styles.css"></head>
<body>
<h2>Profilul lui <?= htmlspecialchars($_SESSION['username']) ?></h2>
<a href="users.php">Vezi utilizatori</a> | <a href="logout.php">Logout</a>
<form method="POST" enctype="multipart/form-data" action="upload.php">
  <input type="hidden" name="csrf_token" value="<?= generate_csrf_token() ?>">
  <input type="file" name="photo" required><button type="submit">Încarcă</button>
</form>
<div class="gallery">
<?php while ($row = $result->fetch_assoc()): ?>
  <div><img src="uploads/<?= htmlspecialchars($row['filename']) ?>">
    <form method="POST" action="delete.php">
      <input type="hidden" name="csrf_token" value="<?= generate_csrf_token() ?>">
      <input type="hidden" name="photo_id" value="<?= $row['id'] ?>">
      <button type="submit">Șterge</button>
    </form>
  </div>
<?php endwhile; ?>
</div>
</body></html>