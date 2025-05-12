#include "Multime.h"
#include "IteratorMultime.h"

#include <iostream>
//Teta(1)
Multime::Multime() {
	/* de adaugat */
	capacitate = 13;
	tabela = std::vector<std::list<TElem>>(capacitate);
	nrElem = 0;
}

// CF: Teta(1) - lista de pe pozitia hash-ului e goala
// CD: Teta(n) - toate elem sunt in aceeasi lista
// CM: Teta(1) - presupune o fct de dispersie buna
bool Multime::adauga(TElem elem) {
	/* de adaugat */
	int pozitie = dispersie(elem);
	for (TElem e : tabela[pozitie]) {
		if (e == elem) {
			return false;
		}
	}

	tabela[pozitie].push_back(elem);
	nrElem++;
	return true;
}

// CF: Θ(1) - elementul este primul în lista de la poziția hash-ului
// CD: Θ(n) - când toate elementele sunt in aceeasi lista
// CM: Θ(1) - presupunand o functie de dispersie buna

bool Multime::sterge(TElem elem) {
	/* de adaugat */
	int pozitie = dispersie(elem);
	auto &lista = tabela[pozitie];
	for (auto it = lista.begin(); it != lista.end(); ++it) {
		if (*it == elem) {
			lista.erase(it);
			nrElem--;
			return true;
		}
	}
	return false;
}


// CF: Θ(1) - elementul este primul în lista de la poziția hash-ului
// CD: Θ(n) - când toate elementele sunt în aceeași listă
// CM: Θ(1) - presupunând o funcție de dispersie bună

bool Multime::cauta(TElem elem) const {
	/* de adaugat */
	int pozitie = dispersie(elem);
	for (TElem e : tabela[pozitie]) {
		if (e == elem) {
			return true;
		}
	}
	return false;
}

// Teta(1)
int Multime::dim() const {
	/* de adaugat */
	return nrElem;
}

// Teta(1)
bool Multime::vida() const {
	/* de adaugat */
	return nrElem == 0;
}


Multime::~Multime() {
	/* de adaugat */
}



IteratorMultime Multime::iterator() const {
	return IteratorMultime(*this);
}

