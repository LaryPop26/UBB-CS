function getStations() {
    let source = $('#source').get(0);
    let sourceCity = source.options[source.selectedIndex].value;

    let destinationList = $('#destinationList');
    destinationList.empty();

    if (!sourceCity) {
        destinationList.append('<li>Alege o plecare</li>');
        return;
    }

    let request = new XMLHttpRequest();
    request.onreadystatechange = function () {
        if (request.readyState === 4) {
            if (request.status === 200) {
                let array = JSON.parse(request.responseText);

                if (array.length === 0) {
                    destinationList.append('<li>Nu există sosiri disponibile</li>');
                    return;
                }

                array.forEach(function(item) {
                    destinationList.append(`<li>${item}</li>`);
                });
            } else {
                destinationList.append('<li>Eroare la încărcarea datelor</li>');
            }
        }
    }
    request.open('GET','getDestinations.php?source=' + encodeURIComponent(sourceCity));
    request.send();
}

/*
function getStations() {
    let sourceCity = $('#source').val();
    let destinationList = $('#destinationList');
    destinationList.empty();

    if (!sourceCity) {
        destinationList.append('<li>Alege o plecare</li>');
        return;
    }

    $.ajax({
        url: 'getDestinations.php',
        method: 'GET',
        data: { source: sourceCity },
        dataType: 'json',
        success: function(array) {
            if (array.length === 0) {
                destinationList.append('<li>Nu există sosiri disponibile</li>');
                return;
            }

            array.forEach(function(item) {
                destinationList.append(`<li>${item}</li>`);
            });
        },
        error: function() {
            destinationList.append('<li>Eroare la încărcarea datelor</li>');
        }
    });
}*/