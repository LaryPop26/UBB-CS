#include "Colectie.h"
#include "IteratorColectie.h"
#include <iostream>

using namespace std;

bool rel(TElem e1, TElem e2) {
	/* de adaugat */
	return e1<=e2;
}

void Colectie::dealoca(int p) {
	drept[p] = primLiber;
	stang[p] = -1;
	primLiber = p;
}

int Colectie::aloca() {
	// alocare un spatiu liber pe prima poz libera
	int p = primLiber;
	primLiber = drept[primLiber];
	return p;
}

void Colectie::resize() {
	// redimensionare pt cele 3 tablouri
	TComparabil* new_elems = new TComparabil[cp * 2];
	int* new_drept = new int[cp * 2];
	int* new_stang = new int[cp * 2];
	for ( int i=0;i<cp;i++) {
		new_elems[i] = elems[i];
		new_stang[i] = stang[i];
		new_drept[i] = drept[i];
	}

	// dealocare spatiu pt tablourile anterioare si initializarea lor
	delete[] elems;
	delete[] stang;
	delete[] drept;
	elems = new_elems;
	stang = new_stang;
	drept = new_drept;
	cp = cp * 2;
	// initializare spatii libere in lista
	for ( int i =0;i<cp*2-1; i++) {
		drept[i] = i+1;
	}
	stang[cp*2-1] = -1;
	primLiber = cp;
	cp = cp*2;
}


int Colectie::creeazaNod(TElem e) {
	if (size >= cp) {
		resize();
	}
	int p = aloca();
	elems[p] = make_pair(e, 1);
	stang[p] = -1;
	drept[p] = -1;
	return p;
}



int Colectie::minim(int p) {
	while (p!= -1) {
		p = stang[p];
	}
	return p;
}


int Colectie::stergeToateElementeleRepetitive() {
}


Colectie::Colectie() {
	/* de adaugat */
	cp = CAPACITY;
	size = 0;
	// alocare spatiu pt cele 3 liste
	elems = new TComparabil[cp];
	stang = new int[cp];
	drept = new int[cp];
	// initializare colectie vida
	radacina = -1;

	// initializare spatii libere in lista
	for ( int i =0;i<cp-1; i++) {
		drept[i] = i+1;
		stang[i+1] = i;
	}
	stang[0] = -1;
	drept[cp-1] = -1;
	// primul spatiu liber e pe index 0
	primLiber = 0;

}

void Colectie::adauga(TElem e) {
	/* de adaugat */
	size++;

	// daaca colectia e vida
	if (radacina == -1) {
		radacina = creeazaNod(e);
		return;
	}
	// parcurgem arborele pana gasim locul de adaugat
	int pos = radacina;
	int parinte = pos;
	while (pos != -1) {
		parinte = pos;
		// daca elem exista - creste frecventa
		if ( e == elems[pos].first) {
			elems[pos].second++;
			return;
		}
		// daca e in relatie cu elementul curent - parcurgem arborele stang , altfel pe cel drept
		if (rel(e, elems[pos].first)) {
			pos = stang[pos];
		} else {
			pos = drept[pos];
		}
	}

	// creem noul nod si subarborii
	int p = creeazaNod(e);
	if (rel(e,elems[parinte].first)) {
		stang[parinte] = p;
	} else {
		drept[parinte] = p;
	}
}

// complexitate: O(n) - capacitatea curenta a arborelui
bool Colectie::sterge_rec(int curent, int anterior, TElem e) {
	// daca am ajuns la un subarbore vid
	if (curent == -1) {
		return false;
	}
	// daca am ajuns la elementul de sters
	if (elems[curent].first == e) {
		size--;
		// daca elementul are mai mult de o singura aparitie, decrementam frecventa
		if (elems[curent].second > 1) {
			elems[curent].second--;
			return true;
		}
		// daca nodul are si subarbore stang si drept
		else if (stang[curent] != -1 && drept[curent] != -1) {
			int min = minim(drept[curent]);
			elems[curent] = elems[min];
			return sterge_rec(drept[curent], curent, elems[min].first);
		}
		// daca nodul este o frunza
		else if (stang[curent] == -1 && drept[curent] == -1) {
			if (curent == radacina) {
				radacina = -1;
			}
			else {
				if (stang[anterior] == curent) {
					stang[anterior] = -1;
				}
				else {
					drept[anterior] = -1;
				}
			}
		}
		// daca nodul are un singur fiu, stang
		else if (stang[curent] == -1) {
			if (anterior == -1) {
				radacina = drept[curent];
			}
			else if (stang[anterior] == curent) {
				stang[anterior] = drept[curent];
			}
			else {
				drept[anterior] = drept[curent];
			}
		}
		// daca nodul are un singur fiu, drept
		else {
			if (anterior == -1) {
				radacina = stang[curent];
			}
			else if (stang[anterior] == curent) {
				stang[anterior] = stang[curent];
			}
			else {
				drept[anterior] = stang[curent];
			}
		}
		dealoca(curent);
		return true;
	}
	// daca este in relatie cu elementul curent parcurgem subarborele stang, altfel pe cel drept
	if (rel(e, elems[curent].first)) {
		return sterge_rec(stang[curent], curent, e);
	}
	else {
		return sterge_rec(drept[curent], curent, e);
	}
}

bool Colectie::sterge(TElem e) {
	/* de adaugat */
	return sterge_rec(radacina, -1, e);
}


bool Colectie::cauta(TElem elem) const {
	// parcurgem arborele pana gasim elementul sau ajungem la capatul arborelui
	int pos = radacina;
	while (pos != -1) {
		if (elem == elems[pos].first) {
			return true;
		}
		// daca este in relatie cu elementul curent parcurgem subarborele stang, altfel pe cel drept
		if (rel(elem, elems[pos].first)) {
			pos = stang[pos];
		}
		else {
			pos = drept[pos];
		}
	}
	return false;
}

// O(n) - capacitatea curenta a arborelui
int Colectie::nrAparitii(TElem elem) const {
	/* de adaugat */
	// parcurgem arborele
	int pos = radacina;
	while (pos != -1) {
		// daca am gasit elem
		if (elem == elems[pos].first) {
			return elems[pos].second;
		}
		// daca e in relatie cu elementul curent - parcurgem arborele stang , altfel pe cel drept
		if (rel(elem, elems[pos].first)) {
			pos = stang[pos];
		} else {
			pos = drept[pos];
		}
	}
	// daca nu s-a gasit
	return 0;
}


// Teta(1)
int Colectie::dim() const {
	/* de adaugat */
	return size;
}

// Teta(1)
bool Colectie::vida() const {
	/* de adaugat */
	return size == 0;
}


IteratorColectie Colectie::iterator() const {
	return  IteratorColectie(*this);
}

// Teta(1)
Colectie::~Colectie() {
	/* de adaugat */
	delete[] elems;
	delete[] stang;
	delete[] drept;
}
