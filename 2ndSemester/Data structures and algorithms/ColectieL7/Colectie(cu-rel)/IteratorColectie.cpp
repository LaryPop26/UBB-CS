#include "IteratorColectie.h"
#include "Colectie.h"
using namespace std;

// O(n) - capacitatea curenta a colectiei
IteratorColectie::IteratorColectie(const Colectie& c): col(c) {
	/* de adaugat */
	curent = col.radacina;
	int anterior = -1;

	// se adauga in stiva ramura stanga a elem curent
	while (curent != -1) {
		s.push(curent);
		anterior = curent;
		curent = col.stang[curent];
	}

	// se sterge frunza din varful stivei
	if (!s.empty()) {
		s.pop();
		curent = anterior;
	}
}

// Teta(1)
TElem IteratorColectie::element() const{
	/* de adaugat */
	if (!valid()) {
		throw exception();
	}
	return col.elems[curent].first;
}

// Teta(1)
bool IteratorColectie::valid() const {
	/* de adaugat */
	return curent != -1;
}

// O(n) - capacitatea curenta a colectiei
void IteratorColectie::urmator() {
	/* de adaugat */
	if (!valid()) {
		throw exception();
	}
	// se sterge nodul din varful stivei
	if (!s.empty()) {
		curent = s.top();
		s.pop();
	}
	if (col.drept[curent] != -1) {
		curent = col.drept[curent];
		// se adauga in stiva ramura stanga a elem curent
		while (curent != -1) {
			s.push(curent);
			curent = col.stang[curent];
		}
	}

	// se sterge nodul din varful stivei
	if (!s.empty()) {
		curent = s.top();
	} else { curent = -1;}
}

// O(n) - capacitatea curenta a colectiei
void IteratorColectie::prim() {
	/* de adaugat */
	// se sterg toate elem adaugate in stiva
	while (!s.empty()) {
		s.pop();
	}
	curent = col.radacina;

	// se adauga in stiva ramura stanga a elem curent
	while (curent != -1) {
		s.push(curent);
		curent = col.stang[curent];
	}
	// se sterge frunza din varful stivei
	if (!s.empty()) {
		curent = s.top();
	}
}
