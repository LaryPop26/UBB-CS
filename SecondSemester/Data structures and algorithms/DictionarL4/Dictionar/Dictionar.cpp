#include "Dictionar.h"
#include <iostream>
#include "IteratorDictionar.h"
// Teta(n)
Dictionar::Dictionar() {
	/* de adaugat */
	capacitate = 10;
	prim = -1;
	urm = new int[capacitate];
	prec = new int[capacitate];
	e = new TElem[capacitate];
	for (int i = 0; i < capacitate; i++) {
		urm[i] = -1;
	}
	urm[capacitate - 1] = -1;
	primLiber = 0;
	ultim = -1;
}
//Teta(1)
Dictionar::~Dictionar() {
	/* de adaugat */
	delete[] urm;
	delete[] prec;
	delete[] e;
}
//O(1)
int Dictionar::aloca() {
	if ( primLiber == -1 ) {
		redimensionare();
	}

	int i = primLiber;
	primLiber = urm[primLiber];
	return i;
}

// O(1)
void Dictionar::dealoca(int i) {
	urm[i] = primLiber;
	primLiber = i;
}
// Teta(n)
void Dictionar::redimensionare() {
	int capacitateNoua = capacitate * 2;
	TElem* eNou = new TElem[capacitateNoua];
	int* urmNou = new int[capacitateNoua];
	int* precNou = new int[capacitateNoua];

	// Copy existing elements
	for (int i = 0; i < capacitate; i++) {
		eNou[i] = e[i];
		urmNou[i] = urm[i];
		precNou[i] = prec[i];
	}

	// Initialize the new free space
	for (int i = capacitate; i < capacitateNoua - 1; i++) {
		urmNou[i] = i + 1;
		precNou[i] = -1;
	}
	urmNou[capacitateNoua - 1] = -1;
	precNou[capacitateNoua - 1] = -1;

	delete[] e;
	delete[] urm;
	delete[] prec;

	e = eNou;
	urm = urmNou;
	prec = precNou;
	primLiber = capacitate;  // Start of new free space
	capacitate = capacitateNoua;

}

// CF: O(1) - el e adaugat la inceput / pe prima poz
// CD = CT: O(n) - se adauga la final / + redimensionare
TValoare Dictionar::adauga(TCheie c, TValoare v){
	/* de adaugat */
	// Cauta cheia si actualizeaza val + returneaza val veche
	int p = prim;
	while (p != -1) {
		if (e[p].first == c) {
			TValoare veche = e[p].second;
			e[p].second = v;
			return veche;
		}
		p = urm[p];
	}

	// Se aloca un nod nou
	int i = aloca();
	if (i == -1) {
		return NULL_TVALOARE; // Handle allocation failure
	}

	// Se adauga perechea + actualizare legaturi
	e[i] = std::make_pair(c, v);
	urm[i] = -1;
	prec[i] = ultim;

	// Update links
	if (ultim != -1) {
		urm[ultim] = i;
	}
	else {
		prim = i;
	}
	ultim = i;

	return NULL_TVALOARE;

}

//cauta o cheie si returneaza valoarea asociata
// CF: O(1) - elem cautat e primul
// CD=CT: O(n) - elem e ultimul / nu exista
TValoare Dictionar::cauta(TCheie c) const{
	/* de adaugat */
	int p = prim;
	while (p != -1) {
		if (e[p].first == c) {
			return e[p].second;
		}
		p = urm[p];
	}

	return NULL_TVALOARE;
}

// CF: O(1) - elem de sters e primul
// CD=CT: O(n) - se parcurge pana se gaseste
TValoare Dictionar::sterge(TCheie c){
	/* de adaugat */
	int p = prim;
	while (p != -1) {
		if (e[p].first == c) {
			TValoare val = e[p].second;
			int pre = prec[p];
			int next = urm[p];

			if (pre != -1) {
				urm[pre] = next;
			}
			else {
				prim = next;
			}

			if (next != -1) {
				prec[next] = pre;
			}
			else {
				ultim = pre;
			}
			dealoca(p);
			return val;
		}
		p = urm[p];
	}
	return NULL_TVALOARE;
}

// CF=CD=CT: O(n)
void Dictionar::filtreaza(Conditie cond) {
	int p = prim;
	while (p != -1) {
		int next = urm[p];  // Salvăm următoarea poziție înainte de o posibilă ștergere
		if (cond(e[p].first)) {
			sterge(e[p].first);
		}
		p = next;
	}
}

// Teta(n)
int Dictionar::dim() const {
	/* de adaugat */
	int cnt = 0;
	int p = prim;
	while (p != -1) {
		cnt++;
		p = urm[p];
	}
	return cnt;
}
// Teta(1)
bool Dictionar::vid() const{
	/* de adaugat */
	return prim == -1;
}

// Teta(1)
IteratorDictionar Dictionar::iterator() const {
	return  IteratorDictionar(*this);
}


