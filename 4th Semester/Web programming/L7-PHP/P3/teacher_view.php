<?php
session_start();

if (!isset($_SESSION['id']) || $_SESSION['role'] !== 'teacher') {
    header("Location: index.html");
    exit;
}

$mysqli = new mysqli("localhost", "root", "", "lab-PHP");
if ($mysqli->connect_error) {
    exit('DB connection failed');
}

// Afișare mesaj (succes / eroare)
if (isset($_SESSION['message'])) {
    $color = ($_SESSION['msg_type'] === 'success') ? 'green' : 'red';
    echo '<p style="color:' . $color . ';">' . htmlspecialchars($_SESSION['message']) . '</p>';
    unset($_SESSION['message'], $_SESSION['msg_type']);
}

// Formularul pentru adăugarea notei
echo '<form method="POST" action="add_grade.php" style="margin-bottom:20px;">';

// Select materii
$sql = "SELECT id, name FROM subjects";
$stmt = $mysqli->prepare($sql);
$stmt->execute();
$stmt->bind_result($subject_id, $subject_name);

echo '<label for="subject">Materie:</label>';
echo '<select id="subject" name="subject" required>';
while ($stmt->fetch()) {
    echo '<option value="' . $subject_id . '">' . htmlspecialchars($subject_name) . '</option>';
}
echo '</select>';

// Select studenti
$stmt->close();
$sql = "SELECT id, username FROM students";
$stmt = $mysqli->prepare($sql);
$stmt->execute();
$stmt->bind_result($student_id, $student_username);

echo '<br><label for="student">Student:</label>';
echo '<select id="student" name="student" required>';
while ($stmt->fetch()) {
    echo '<option value="' . $student_id . '">' . htmlspecialchars($student_username) . '</option>';
}
echo '</select>';

// Input nota
echo '<br><label for="grade">Notă (1-10):</label>';
echo '<input type="number" id="grade" name="grade" min="1" max="10" required>';

// Buton submit
echo '<br><input type="submit" value="Adaugă notă">';
echo '</form>';

// Afișarea notelor adăugate (ale tuturor studenților, după materie și student)
echo '<h2>Note existente</h2>';
echo '<table border="1" cellpadding="5" cellspacing="0">';
echo '<tr><th>Materie</th><th>Student</th><th>Notă</th></tr>';

$sql = "SELECT subjects.name AS subject_name, students.username AS student_username, grades.grade 
        FROM grades 
        JOIN subjects ON grades.subject_id = subjects.id
        JOIN students ON grades.student_id = students.id
        ORDER BY subjects.name, students.username";

$result = $mysqli->query($sql);

if ($result && $result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
        echo '<tr>';
        echo '<td>' . htmlspecialchars($row['subject_name']) . '</td>';
        echo '<td>' . htmlspecialchars($row['student_username']) . '</td>';
        echo '<td>' . htmlspecialchars($row['grade']) . '</td>';
        echo '</tr>';
    }
} else {
    echo '<tr><td colspan="3">Nu există note înregistrate.</td></tr>';
}

echo '</table>';
?>
