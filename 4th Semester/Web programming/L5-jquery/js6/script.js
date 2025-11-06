const n = 4;
let grid = [];
let emptyRow = 0, emptyCol = 0;

function generatePuzzle() {
  const numbers = Array.from({ length: n * n }, (_, i) => i);
  shuffleArray(numbers);

  grid = [];
  let idx = 0;
  for (let i = 0; i < n; i++) {
    grid[i] = [];
    for (let j = 0; j < n; j++) {
      grid[i][j] = numbers[idx];
      if (numbers[idx] === 0) {
        emptyRow = i;
        emptyCol = j;
      }
      idx++;
    }
  }
}

function shuffleArray(arr) {
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
}

function drawPuzzle() {
  const $table = $("#puzzle");
  $table.empty();
  for (let i = 0; i < n; i++) {
    const $row = $("<tr></tr>");
    for (let j = 0; j < n; j++) {
      const val = grid[i][j];
      const $cell = $("<td></td>").text(val !== 0 ? val : "").addClass(val === 0 ? "empty" : "");
      $row.append($cell);
    }
    $table.append($row);
  }
}

function move(dx, dy) {
  const newRow = emptyRow + dx;
  const newCol = emptyCol + dy;

  if (newRow >= 0 && newRow < n && newCol >= 0 && newCol < n) {
    [grid[emptyRow][emptyCol], grid[newRow][newCol]] = [grid[newRow][newCol], grid[emptyRow][emptyCol]];
    emptyRow = newRow;
    emptyCol = newCol;
    drawPuzzle();
  }
}

$(document).keydown((e) => {
  switch (e.key) {
    case "ArrowUp": move(1, 0); break;
    case "ArrowDown": move(-1, 0); break;
    case "ArrowLeft": move(0, 1); break;
    case "ArrowRight": move(0, -1); break;
  }
});

generatePuzzle();
drawPuzzle();
