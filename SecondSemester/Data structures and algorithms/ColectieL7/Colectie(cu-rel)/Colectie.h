#pragma once
#include <utility>
using namespace std;

#define CAPACITY 100; //capacitatea colectiei

typedef int TElem;
typedef pair<TElem, int> TComparabil;
typedef bool(*Relatie)(TElem, TElem);

//in implementarea operatiilor se va folosi functia (relatia) rel (de ex, pentru <=)
// va fi declarata in .h si implementata in .cpp ca functie externa colectiei
bool rel(TElem, TElem);

class IteratorColectie;

class Colectie {

	friend class IteratorColectie;

private:
	/* aici e reprezentarea */
	int cp, size; // capacitate liste si nr elem
	TComparabil* elems; // sir de elems
	int* stang; // sir de fii stangi
	int* drept; // sir de fii drepti
	int radacina, primLiber; // referinte catre indexul radacinii si al primului spatiu liber

	// dealoca spatiu pt un elem
	void dealoca(int p);

	// aloca spatiu pt un nou elem si returneaza pozitia spatiului alocat
	int aloca();

	// redimensionare liste
	void resize();

	// fct de creare a unui nou nod in arbore cu redimensionare
	// returneaza pozitia pe care e inserat elem
	int creeazaNod(TElem e);

	// sterge o aparitie a unui elem din colectie recursiv
	bool sterge_rec(int curent, int anterior, TElem e);

	int minim(int p);

public:
		//constructorul implicit
		Colectie();

		//adauga un element in colectie
		void adauga(TElem e);

		//sterge o aparitie a unui element din colectie
		//returneaza adevarat daca s-a putut sterge
		bool sterge(TElem e);

		//
		int stergeToateElementeleRepetitive();

		//verifica daca un element se afla in colectie
		bool cauta(TElem elem) const;

		//returneaza numar de aparitii ale unui element in colectie
		int nrAparitii(TElem elem) const;

		//intoarce numarul de elemente din colectie;
		int dim() const;

		//verifica daca colectia e vida;
		bool vida() const;

		//returneaza un iterator pe colectie
		IteratorColectie iterator() const;

		// destructorul colectiei
		~Colectie();


};

