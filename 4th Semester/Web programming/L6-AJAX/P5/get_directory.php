<?php
$path = $_GET['path'] ?? '.';

// Pentru securitate, poți normaliza și valida path-ul:
$realBase = realpath(__DIR__ . '/../'); // un folder superior ca bază (exemplu)
$realUserPath = realpath($path);

if ($realUserPath === false || strpos($realUserPath, $realBase) !== 0) {
    // Dacă path-ul nu există sau e în afara bazei permise, returnează eroare:
    echo json_encode([]);
    exit;
}

// Citește conținutul directorului
$files = scandir($realUserPath);
$result = [];

foreach ($files as $file) {
    if ($file === '.' || $file === '..') continue;
    $fullPath = $realUserPath . DIRECTORY_SEPARATOR . $file;
    $result[] = [
        'name' => $file,
        'path' => $fullPath,
        'type' => is_dir($fullPath) ? 'dir' : 'file'
    ];
}

header('Content-Type: application/json');
echo json_encode($result);
?>
