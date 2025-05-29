#include "Multime.h"
#include "IteratorMultime.h"

#include <iostream>
//Teta(1)
Multime::Multime() {
	capacitate = 13;
	nrElem = 0;
	tabela = new Nod*[capacitate];
	for (int i = 0; i < capacitate; ++i) {
		tabela[i] = nullptr;
	}
}

// CF: Teta(1) - lista de pe pozitia hash-ului e goala
// CD: Teta(n) - toate elem sunt in aceeasi lista
// CM: Teta(1) - presupune o fct de dispersie buna
bool Multime::adauga(TElem e) {
	int poz = dispersie(e);
	Nod* curent = tabela[poz];
	while (curent != nullptr) {
		if (curent->valoare == e)
			return false;
		curent = curent->urm;
	}
	tabela[poz] = new Nod(e, tabela[poz]);
	nrElem++;
	return true;
}

// CF: Θ(1) - elementul este primul în lista de la poziția hash-ului
// CD: Θ(n) - când toate elementele sunt in aceeasi lista
// CM: Θ(1) - presupunand o functie de dispersie buna

bool Multime::sterge(TElem e) {
	int poz = dispersie(e);
	Nod* curent = tabela[poz];
	Nod* anterior = nullptr;

	while (curent != nullptr) {
		if (curent->valoare == e) {
			if (anterior == nullptr)
				tabela[poz] = curent->urm;
			else
				anterior->urm = curent->urm;
			delete curent;
			nrElem--;
			return true;
		}
		anterior = curent;
		curent = curent->urm;
	}
	return false;
}


// CF: Θ(1) - elementul este primul în lista de la poziția hash-ului
// CD: Θ(n) - când toate elementele sunt în aceeași listă
// CM: Θ(1) - presupunând o funcție de dispersie bună

bool Multime::cauta(TElem e) const {
	int poz = dispersie(e);
	Nod* curent = tabela[poz];
	while (curent != nullptr) {
		if (curent->valoare == e)
			return true;
		curent = curent->urm;
	}
	return false;
}

// CF = Θ(1) - multimea e vida
// CM = CD: Θ(n) - se parcurg toate elementele in orice caz
int Multime::diferentaMaxMin() const {
	if (vida())
		return -1;

	int minVal = NULL_TELEM;
	int maxVal = NULL_TELEM;

	for (int i = 0; i < capacitate; ++i) {
		Nod* curent = tabela[i];
		while (curent != nullptr) {
			if (curent->valoare < minVal)
				minVal = curent->valoare;
			if (curent->valoare > maxVal)
				maxVal = curent->valoare;
			curent = curent->urm;
		}
	}
	return maxVal - minVal;
}


/*
	Subalgoritm diferentaMaxMin(int rez)
		// pre: Multime M

		daca M.vida() atunci
			rez <- -1

		minVal <- NULL
		maxVal <- NULL
		prim <- true

		Pentru fiecare lista L din M.tabela executa
			Pentru fiecare e in L executa
				Daca prim atunci
					minVal <- e
					maxVal <- e
					prim <- false
				altfel
					Daca e < minVal atunci
						minVal <- e
					SfDaca
					Daca e > maxVal atunci
					SfDaca
				SfDaca
			SfPentru
		SfPentru

		rez <- maxVal - minVal
 */

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
	for (int i = 0; i < capacitate; ++i) {
		Nod* curent = tabela[i];
		while (curent != nullptr) {
			Nod* deSters = curent;
			curent = curent->urm;
			delete deSters;
		}
	}
	delete[] tabela;
}


IteratorMultime Multime::iterator() const {
	return IteratorMultime(*this);
}

