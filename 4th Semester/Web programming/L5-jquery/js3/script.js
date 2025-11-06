const useImages = true; // `true` pentru imagini, `false` pentru numere

const imageUrls = [
    'https://picsum.photos/100/100?random=1',
    'https://picsum.photos/100/100?random=2',
    'https://picsum.photos/100/100?random=3',
    'https://picsum.photos/100/100?random=4',
    'https://picsum.photos/100/100?random=5',
    'https://picsum.photos/100/100?random=6',
    'https://picsum.photos/100/100?random=7',
    'https://picsum.photos/100/100?random=8',
    'https://picsum.photos/100/100?random=9',
    'https://picsum.photos/100/100?random=10',
];

let values = [];
let clicked = [];
let idS = [];
let noFlipped = 0;

Array.prototype.shuffle = function () {
    for (let i = this.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [this[i], this[j]] = [this[j], this[i]];
    }
};

function startNewGame() {
    noFlipped = 0;
    clicked = [];
    idS = [];

    if (useImages) {
        values = imageUrls.concat(imageUrls);
    } else {
        values = [];
        for (let i = 0; i < 10; i++) {
            values.push(i.toString(), i.toString());
        }
    }

    values.shuffle();

    let output = '';
    for (let i = 0; i < values.length; i++) {
        if (useImages) {
            output += `
                <div id="card_${i}" class="card" data-value="${values[i]}">
                    <img src="${values[i]}" alt="img${i}">
                </div>
            `;
        } else {
            output += `
                <div id="card_${i}" class="card text" data-value="${values[i]}">
                    <span class="hidden">${values[i]}</span>
                </div>
            `;
        }
    }

    $('#board').html(output);
    $('#winMessage').text('');

    // Adaugă handlerul după generarea cărților
    $('.card').on('click', function () {
        flip($(this), $(this).data('value'));
    });
}

function flip($card, value) {
    if (clicked.length < 2 && !$card.hasClass('revealed')) {
        if (useImages) {
            $card.addClass('revealed');
        } else {
            $card.find('.hidden').show();
            $card.addClass('revealed text');
        }

        clicked.push(value);
        idS.push($card.attr('id'));

        if (clicked.length === 2) {
            if (clicked[0] === clicked[1]) {
                clicked = [];
                idS = [];
                noFlipped += 2;
                if (noFlipped === values.length) {
                    $('#winMessage').text('Ai câștigat!');
                }
            } else {
                setTimeout(() => {
                    for (let i = 0; i < idS.length; i++) {
                        const $cardToHide = $('#' + idS[i]);
                        if (useImages) {
                            $cardToHide.removeClass('revealed');
                        } else {
                            $cardToHide.find('.hidden').hide();
                            $cardToHide.removeClass('revealed text');
                        }
                    }
                    clicked = [];
                    idS = [];
                }, 2000);
            }
        }
    }
}

$(document).ready(startNewGame);
