<?php
$file = $_GET['file'] ?? '';

// Securitate: normalizează calea și verifică că e într-un director permis
$baseDir = realpath(__DIR__ . '/../'); // rădăcina permisă, de exemplu
$realFile = realpath($file);

if ($realFile === false || strpos($realFile, $baseDir) !== 0 || !is_file($realFile)) {
    http_response_code(400);
    echo "Fișierul nu există sau accesul este interzis.";
    exit;
}

$content = file_get_contents($realFile);

header('Content-Type: text/plain; charset=utf-8');
echo $content;
