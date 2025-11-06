function filtrareProduse() {
  const prod = document.getElementById('producator').value;
  const proc = document.getElementById('procesor').value;
  const mem = document.getElementById('memorie').value;
  const hdd = document.getElementById('capacitateHDD').value;
  const placa = document.getElementById('placavideo').value;

  const xhr = new XMLHttpRequest();
  xhr.open("POST", "filter.php", true);
  xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

  xhr.onload = function () {
    document.getElementById('rezultate').innerHTML = xhr.responseText;
  };

  const data = `producator=${encodeURIComponent(prod)}&procesor=${encodeURIComponent(proc)}&memorie=${encodeURIComponent(mem)}&capacitateHDD=${encodeURIComponent(hdd)}&placavideo=${encodeURIComponent(placa)}`;
  xhr.send(data);
}


/*
function filtrareProduse() {
  const data = {
    producator: $('#producator').val(),
    procesor: $('#procesor').val(),
    memorie: $('#memorie').val(),
    capacitateHDD: $('#capacitateHDD').val(),
    placavideo: $('#placavideo').val()
  };

  $.post('filter.php', data, function(response) {
    $('#rezultate').html(response);
  }).fail(function() {
    $('#rezultate').html('Eroare la filtrare.');
  });
}

*/