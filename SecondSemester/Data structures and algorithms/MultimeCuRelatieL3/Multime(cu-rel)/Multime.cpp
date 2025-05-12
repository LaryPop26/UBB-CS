#include "Multime.h"
#include "IteratorMultime.h"
#include <iostream>

using namespace std;

// O(1)
bool rel(TElem e1, TElem e2) {
	if (e1 <= e2) {
		return true;
	}
	else {
		return false;
	}
}

// O(1)
Nod::Nod(TElem el, PNod urmator) {
	this->el=el;
	this->urmator=urmator;
}

//O(1)
TElem Nod::getEl() {
	return el;
}

//O(1)
PNod Nod::getUrmator() {
	return urmator;
}

//O(1)
Multime::Multime() {
	prim = nullptr;
}

/* Complexitate:
 * CF: Teta(1) : el se adauga la inceput
 * CD Teta(n)
 * = CM O(n) se adauga la sfarsit
*/
bool Multime::adauga(TElem elem) {
	// daca lista e goala => creeaza nod
	if (prim == nullptr) {
		prim = new Nod(elem, nullptr);
		return true;
	}
	// elem = primul din lista => fals
	if (elem == prim->el) return false;

	// daca elem e mai mic decat primul din lista se adauga la inceput
	if (!rel(prim->el, elem)) {
		prim = new Nod(elem, prim);
		return true;
	}

	PNod anterior = prim;
	PNod curent = prim->urmator;

	// parcurge lista pana gaseste poz corecta
	while (curent != nullptr && rel(curent->el, elem)) {
		if (curent->el == elem)
			return false; // deja există
		anterior = curent;
		curent = curent->urmator;
	}

	// Inserare între anterior și curent
	anterior->urmator = new Nod(elem, curent);
	return true;
}

/* Complexitate:
 * CF: Teta(1) : el se sterge de  la inceput
 * CD = CM O(n) se sterge de la sfarsit
*/
bool Multime::sterge(TElem elem) {
	// lista goala => fals
	if (prim == nullptr)
		return false;

	// elem e primul => salveaza nodul de sters , actualizeaza primul nod, sterge nodul salvat
	if (prim->el == elem) {
		PNod deSters = prim;
		prim = prim->urmator;
		delete deSters;
		return true;
	}

	PNod anterior = prim;
	PNod curent = prim->urmator;

	// cauta elem in lista , daca e gasit il sterge
	while (curent != nullptr && rel(curent->el, elem)) {
		if (curent->el == elem) {
			anterior->urmator = curent->urmator;
			delete curent;
			return true;
		}
		anterior = curent;
		curent = curent->urmator;
	}
	return false;
}

/* Complexitate:
 * CF: Teta(1) : el se gaseste la inceput
 * CD = CM O(n) se gaseste la sfarsit
*/
bool Multime::cauta(TElem elem) const {
	PNod aux = prim;
	if (aux != nullptr) {
		if (elem < aux->getEl())
			return false;
	}
	while (aux != nullptr) {
		if (aux->getEl() == elem)
			return true;
		aux = aux->getUrmator();
	}
	return false;
}

// Complexitate:Teta(1) CF=CM=CD=CT
int Multime::dim() const {
	PNod aux = prim;
	int cnt=0;
	while (aux != nullptr) {
		aux = aux->getUrmator();
		cnt++;
	}
	return cnt;
}

// Complexitate:Teta(1) CF=CM=CD=CT
bool Multime::vida() const {
	if (prim != nullptr)
		return false;
	return true;
}

/* Complexitate:
 * CF: Θ(n) (dacă toate elementele se regăsesc în ambele liste / prima multime e vida)
 * CD = CM = CT: Θ(n x m) - se cauta toate el din prima in a doua
*/
void Multime::intersectie(const Multime &b) {
	if (vida() || b.vida()) {
		while (!vida()) {
			sterge(prim->el);
		}
		return;
	}

	PNod curent = prim;
	while (curent != nullptr) {
		TElem elementCurent = curent->el;
		curent = curent->urmator;

		if (!b.cauta(elementCurent)) {
			sterge(elementCurent);
		}
	}

}

//O(1)
IteratorMultime Multime::iterator() const {
	return IteratorMultime(*this);
}

//O(1)
Multime::~Multime() {
	while (prim != nullptr) {
		PNod p = prim;
		prim = prim->urmator;
		delete p;
	}
}
