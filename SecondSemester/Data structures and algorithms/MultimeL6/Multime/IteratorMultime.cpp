#include "IteratorMultime.h"
#include "Multime.h"

// CF: Teta(1)- prima lista nu este vida
// CD: Teta(m) - m este numarul de pozitii in tabela de dispersie
IteratorMultime::IteratorMultime(const Multime &m) : multime(m){
	/* de adaugat */
	prim();
}

// CF: Θ(1) - urmatorul element este in aceeasi lista
// CD: Θ(m) - trebuie sa parcurga mai multe pozitii din tabela pentru a gasi urmatorul element
// CM: Θ(1)

void IteratorMultime::avanseazaLaUrmator() {
	++itLista;
	while (indexTabela < multime.capacitate && itLista == multime.tabela[indexTabela].end()) {
		indexTabela++;
		if (indexTabela < multime.capacitate) {
			itLista = multime.tabela[indexTabela].begin();
		}
	}
}

// CF: Teta(1)- prima lista nu este vida
// CD: Teta(m) - m este numarul de pozitii in tabela de dispersie
void IteratorMultime::prim() {
	/* de adaugat */
	indexTabela = 0;
	while (indexTabela < multime.capacitate && multime.tabela[indexTabela].empty()) {
		indexTabela++;
	}

	if (indexTabela < multime.capacitate) {
		itLista = multime.tabela[indexTabela].begin();
	}
}

// CF: Θ(1) - urmatorul element este in aceeasi lista
// CD: Θ(m) - trebuie sa parcurga mai multe pozitii din tabela pentru a gasi urmatorul element
// CM: Θ(1)
void IteratorMultime::urmator() {
	/* de adaugat */
	if (!valid())
		throw std::exception();
	avanseazaLaUrmator();
}

// Teta(1)
TElem IteratorMultime::element() const {
	/* de adaugat */
	if (!valid())
		throw std::exception();
	return *itLista;
}

// Teta(1)
bool IteratorMultime::valid() const {
	/* de adaugat */
	return indexTabela < multime.capacitate && itLista != multime.tabela[indexTabela].end();
}
