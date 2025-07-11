#pragma once

#define NULL_TELEM -1
#include <list>
#include <stdlib.h>
#include <vector>
typedef int TElem;

class IteratorMultime;

class Nod {
public:
	TElem valoare;
	Nod* urm;

	Nod(TElem v, Nod* u = nullptr) : valoare(v), urm(u) {}
};

class Multime {
	friend class IteratorMultime;

    private:
		/* aici e reprezentarea */
	Nod** tabela;
	int capacitate;
	int nrElem;

	int dispersie(TElem e) const {
		return abs(e) % capacitate;
	}

    public:
 		//constructorul implicit
		Multime();

		//adauga un element in multime
		//returneaza adevarat daca elementul a fost adaugat (nu exista deja in multime)
		bool adauga(TElem e);

		//sterge un element din multime
		//returneaza adevarat daca elementul a existat si a fost sters
		bool sterge(TElem e);

		//verifica daca un element se afla in multime
		bool cauta(TElem elem) const;

		// returneaza diferenta dintre valoarea maxima si cea minima ( pp valori intregi)
		// daca multimea e vida, se returneaza -1
		int diferentaMaxMin() const;

		//intoarce numarul de elemente din multime;
		int dim() const;

		//verifica daca multimea e vida;
		bool vida() const;

		//returneaza un iterator pe multime
		IteratorMultime iterator() const;

		// destructorul multimii
		~Multime();
};




