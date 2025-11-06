<?php
include 'config.php';

// preluare pagina din GET, cu fallback
$page = isset($_GET['page']) ? (int)$_GET['page'] : 1;
$limit = 3;
$offset = ($page - 1) * $limit;

// query pentru tabelă people și coloane corecte
$sql = "SELECT nume, prenume, telefon, email FROM people LIMIT $limit OFFSET $offset";
$result = mysqli_query($conn, $sql);

$records = [];
while ($row = mysqli_fetch_assoc($result)) {
    $records[] = $row;
}

// verifică câte înregistrări sunt în total pentru paginare
$sql_count = "SELECT COUNT(*) as total FROM people";
$res_count = mysqli_query($conn, $sql_count);
$total = mysqli_fetch_assoc($res_count)['total'];

$hasPrevious = $page > 1;
$hasNext = $offset + $limit < $total;

// trimitem JSON
header('Content-Type: application/json');
echo json_encode([
    'records' => $records,
    'currentPage' => $page,
    'hasPrevious' => $hasPrevious,
    'hasNext' => $hasNext
]);
?>
