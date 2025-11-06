<?php
$db = new mysqli("localhost", "root", "", "photo_app");
if ($db->connect_error) {
    die("Conexiune eșuată: " . $db->connect_error);
}