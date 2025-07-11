#pragma once

class Nod;
typedef int TElem;

typedef Nod* PNod;

typedef bool(*Relatie)(TElem, TElem);

// in implementarea operatiilor se va folosi functia (relatia) rel (de ex, pentru <=)
// va fi declarata in .h si implementata in .cpp ca functie externa colectiei
bool rel(TElem, TElem);

class IteratorMultime;

class Nod {
	friend class Multime;

private:
	TElem el;
	PNod urmator;

public:
	Nod(TElem el, PNod urmator);

	TElem getEl();

	PNod getUrmator();
};

class Multime {

	friend class IteratorMultime;

private:
	/* aici e reprezentarea */
	PNod prim;

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

		//intoarce numarul de elemente din multime;
		int dim() const;

		//verifica daca multimea e vida;
		bool vida() const;

		// pastreaza doar elementele care exista si in multimea b
		void intersectie(const Multime& b);

		//returneaza un iterator pe multime
		IteratorMultime iterator() const;

		// destructorul multimii
		~Multime();

};

