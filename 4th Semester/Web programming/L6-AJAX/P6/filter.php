<?php
include 'config.php';

$producator = $_POST['producator'] ?? '';
$procesor = $_POST['procesor'] ?? '';
$memorie = $_POST['memorie'] ?? '';
$capacitateHDD = $_POST['capacitateHDD'] ?? '';
$placavideo = $_POST['placavideo'] ?? '';

$sql = "SELECT * FROM products WHERE 1=1";

if ($producator !== '') {
    $sql .= " AND producator = '" . mysqli_real_escape_string($conn, $producator) . "'";
}
if ($procesor !== '') {
    $sql .= " AND procesor = '" . mysqli_real_escape_string($conn, $procesor) . "'";
}
if ($memorie !== '') {
    $sql .= " AND memorie = '" . mysqli_real_escape_string($conn, $memorie) . "'";
}
if ($capacitateHDD !== '') {
    $sql .= " AND capacitateHDD = '" . mysqli_real_escape_string($conn, $capacitateHDD) . "'";
}
if ($placavideo !== '') {
    $sql .= " AND placavideo = '" . mysqli_real_escape_string($conn, $placavideo) . "'";
}

$result = mysqli_query($conn, $sql);

if (mysqli_num_rows($result) > 0) {
    while ($row = mysqli_fetch_assoc($result)) {
        echo "<tr>
                <td>{$row['producator']}</td>
                <td>{$row['procesor']}</td>
                <td>{$row['memorie']}</td>
                <td>{$row['capacitateHDD']}</td>
                <td>{$row['placavideo']}</td>
              </tr>";
    }
} else {
    echo "<tr><td colspan='5'>Niciun rezultat găsit.</td></tr>";
}

mysqli_close($conn);
?>
