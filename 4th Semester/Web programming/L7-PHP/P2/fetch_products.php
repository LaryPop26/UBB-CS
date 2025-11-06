<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "lab-PHP";

$conn = new mysqli($servername, $username, $password, $dbname);
if ($conn->connect_error) {
    die("DB connection failed: " . $conn->connect_error);
}

$number = isset($_GET['noProducts']) ? intval($_GET['noProducts']) : 10;
$page = isset($_GET['page']) ? intval($_GET['page']) : 1;
$offset = ($page - 1) * $number;

$totalResult = $conn->query("SELECT COUNT(*) as total FROM products");
$totalRow = $totalResult->fetch_assoc();
$totalProducts = $totalRow['total'];

$sql = "SELECT * FROM products LIMIT $number OFFSET $offset";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    echo "<table border='1' cellpadding='8' cellspacing='0' style='border-collapse: collapse; width: 80%; margin: 20px 0;'>";
    echo "<tr style='background-color: #f2f2f2;'>
            <th>Nume</th>
            <th>Descriere</th>
            <th>Preț</th>
            <th>Cantitate</th>
          </tr>";

    while ($row = $result->fetch_assoc()) {
        echo "<tr>";
        echo "<td>" . htmlspecialchars($row['nume']) . "</td>";
        echo "<td>" . htmlspecialchars($row['descriere']) . "</td>";
        echo "<td style='text-align:right;'>" . intval($row['pret']) . "</td>";
        echo "<td style='text-align:center;'>" . intval($row['cantitate']) . "</td>";
        echo "</tr>";
    }

    echo "</table>";

    echo "<div style='margin-top:10px;'>";

    if ($page > 1) {
        $previousPage = $page - 1;
        echo "<button><a href='fetch_products.php?noProducts=$number&page=$previousPage' style='text-decoration:none;'>Pagina anterioară</a></button> ";
    }

    if ($page * $number < $totalProducts) {
        $nextPage = $page + 1;
        echo "<button><a href='fetch_products.php?noProducts=$number&page=$nextPage' style='text-decoration:none;'>Pagina următoare</a></button>";
    }

    echo "</div>";
} else {
    echo "Nu există produse de afișat.";
}

$conn->close();
?>
