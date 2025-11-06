let currentPlayer = "";
let computerSymbol = "";
let occupiedPositions = ['-', '-', '-', '-', '-', '-', '-', '-', '-'];

function initializeGame() {
    currentPlayer = Math.random() < 0.5 ? "X" : "O";
    if (currentPlayer === "O") {
        computerSymbol = 'X';
        setTimeout(function () {
            makeComputerMove();
        }, 1000);
    } else computerSymbol = 'O';
}

function makePlayerMove(cell) {
    if ($(cell).text() === "") {
        $(cell).text(currentPlayer);
        occupiedPositions[$(cell).attr("id")] = currentPlayer;
        setTimeout(function () {
            makeComputerMove();
        }, 1000);
    }
}

function makeComputerMove() {
    let request = new XMLHttpRequest();
    request.onreadystatechange = function () {
        if (request.readyState === 4) {
            if (request.status === 200) {
                let response = JSON.parse(request.responseText);
                if ('chosenPosition' in response) {
                    document.getElementById(response.chosenPosition).textContent = computerSymbol;
                    occupiedPositions[response.chosenPosition] = computerSymbol;
                }
                if (response.gameResult) {
                    alert("Winner is: " + response.gameResult);
                }
            }
        }
    };

    let requestData = {
        occupiedPositions: occupiedPositions,
        symbol: computerSymbol
    };

    request.open('POST', 'makeMove.php', true);
    request.setRequestHeader('Content-Type', 'application/json');
    request.send(JSON.stringify(requestData));
}


window.onload = initializeGame;


/*
let currentPlayer = "";
let computerSymbol = "";
let occupiedPositions = ['-', '-', '-', '-', '-', '-', '-', '-', '-'];

function initializeGame() {
    currentPlayer = Math.random() < 0.5 ? "X" : "O";

    if (currentPlayer === "O") {
        computerSymbol = 'X';
        setTimeout(makeComputerMove, 1000);
    } else {
        computerSymbol = 'O';
    }
}

function makePlayerMove(cell) {
    if ($(cell).text() === "") {
        $(cell).text(currentPlayer);
        occupiedPositions[$(cell).attr("id")] = currentPlayer;

        setTimeout(makeComputerMove, 1000);
    }
}

function makeComputerMove() {
    const requestData = {
        occupiedPositions: occupiedPositions,
        symbol: computerSymbol
    };

    $.ajax({
        url: 'makeMove.php',
        method: 'POST',
        contentType: 'application/json',
        data: JSON.stringify(requestData),
        dataType: 'json',
        success: function(response) {
            if ('chosenPosition' in response) {
                $('#' + response.chosenPosition).text(computerSymbol);
                occupiedPositions[response.chosenPosition] = computerSymbol;
            }

            if (response.gameResult) {
                alert("Winner is: " + response.gameResult);
            }
        },
        error: function() {
            alert('Eroare la obținerea mutării calculatorului.');
        }
    });
}

$(document).ready(function () {
    initializeGame();

    // Atașează evenimentul de click la fiecare celulă
    $('.cell').on('click', function () {
        makePlayerMove(this);
    });
});



*/