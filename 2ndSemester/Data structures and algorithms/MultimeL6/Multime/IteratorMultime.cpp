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
	if (curent != nullptr)
		curent = curent->urm;

	while (curent == nullptr && ++indexTabela < multime.capacitate) {
		curent = multime.tabela[indexTabela];
	}
}

// CF: Teta(1)- prima lista nu este vida
// CD: Teta(m) - m este numarul de pozitii in tabela de dispersie
void IteratorMultime::prim() {
	indexTabela = 0;
	while (indexTabela < multime.capacitate && multime.tabela[indexTabela] == nullptr) {
		indexTabela++;
	}
	if (indexTabela < multime.capacitate) {
		curent = multime.tabela[indexTabela];
	} else {
		curent = nullptr;
	}
}

// CF: Θ(1) - urmatorul element este in aceeasi lista
// CD: Θ(m) - trebuie sa parcurga mai multe pozitii din tabela pentru a gasi urmatorul element
// CM: Θ(1)
void IteratorMultime::urmator() {
	if (!valid())
		throw std::exception();
	avanseazaLaUrmator();
}

// Teta(1)
TElem IteratorMultime::element() const {
	if (!valid())
		throw std::exception();
	return curent->valoare;
}

// Teta(1)
bool IteratorMultime::valid() const {
	return curent != nullptr;
}
