let ordineClasic = [true, true, true];

function sorteazaClasic(colIndex) {
  const $tabel = $("#tabelClasic");
  const $tbody = $tabel.find("tbody");
  const $randuri = $tbody.find("tr").toArray();
  const sens = ordineClasic[colIndex] = !ordineClasic[colIndex];

  $randuri.sort((a, b) => {
    const valA = $(a).find("td").eq(colIndex).text();
    const valB = $(b).find("td").eq(colIndex).text();

    if (colIndex === 0) {
      return sens ? valA.localeCompare(valB) : valB.localeCompare(valA);
    } else {
      return sens ? valA - valB : valB - valA;
    }
  });

  $tbody.empty().append($randuri);
}

let ordineVertical = {
  fructe: true,
  1: true,
  2: true
};

function getColoane() {
  const $tabel = $("#tabelVertical");
  const $randuri = $tabel.find("tr");
  const $capFructe = $randuri.eq(0).find("th");

  const coloane = [];
  for (let col = 1; col < $capFructe.length; col++) {
    coloane.push({
      fruct: $capFructe.eq(col).text(),
      pret: $randuri.eq(1).find("td").eq(col - 1).text(),
      cant: $randuri.eq(2).find("td").eq(col - 1).text(),
      colIndex: col
    });
  }

  return { coloane, $capFructe, $randuri };
}

function sorteazaDupaRand(indexRand) {
  const { coloane, $capFructe, $randuri } = getColoane();
  const sens = ordineVertical[indexRand] = !ordineVertical[indexRand];

  coloane.sort((a, b) => {
    const valA = parseFloat($randuri.eq(indexRand).find("td").eq(a.colIndex - 1).text());
    const valB = parseFloat($randuri.eq(indexRand).find("td").eq(b.colIndex - 1).text());
    return sens ? valA - valB : valB - valA;
  });

  actualizeazaTabel(coloane, $capFructe, $randuri);
}

function sorteazaDupaNumeFruct() {
  const { coloane, $capFructe, $randuri } = getColoane();
  const sens = ordineVertical['fructe'] = !ordineVertical['fructe'];

  coloane.sort((a, b) => {
    return sens
      ? a.fruct.localeCompare(b.fruct)
      : b.fruct.localeCompare(a.fruct);
  });

  actualizeazaTabel(coloane, $capFructe, $randuri);
}

function actualizeazaTabel(coloane, $capFructe, $randuri) {
  for (let i = 0; i < coloane.length; i++) {
    $capFructe.eq(i + 1).text(coloane[i].fruct);
    $randuri.eq(1).find("td").eq(i).text(coloane[i].pret);
    $randuri.eq(2).find("td").eq(i).text(coloane[i].cant);
  }
}
