#pragma once


#define NULL_TVALOARE -1
typedef int TCheie;
typedef int TValoare;

class IteratorDictionar;

#include <utility>
typedef std::pair<TCheie,TValoare> TElem;

typedef bool (*Conditie)(TCheie);

class Dictionar {
	friend class IteratorDictionar;

	private:
	/* aici e reprezentarea */
	TElem* e;
	int* urm;
	int* prec;

	int capacitate;
	int primLiber;
	int prim;
	int ultim;

	void redimensionare();

	int aloca();

	void dealoca(int i);

	public:

	// constructorul implicit al dictionarului
	Dictionar();

	// adauga o pereche (cheie, valoare) in dictionar	
	// daca exista deja cheia in dictionar, inlocuieste valoarea asociata cheii si returneaza vechea valoare
	// daca nu exista cheia, adauga perechea si returneaza null: NULL_TVALOARE
	TValoare adauga(TCheie c, TValoare v);

	//cauta o cheie si returneaza valoarea asociata (daca dictionarul contine cheia) sau null: NULL_TVALOARE
	TValoare cauta(TCheie c) const;

	//sterge o cheie si returneaza valoarea asociata (daca exista) sau null: NULL_TVALOARE
	TValoare sterge(TCheie c);

	// pastreaza in dictionar nu ai acele perechi ale caror cheie respecta conditia data
	// conditia este o functie care primeste ca parametru o cheie si returneaza true sau fals
	void filtreaza(Conditie cond);

	//returneaza numarul de perechi (cheie, valoare) din dictionar 
	int dim() const;

	//verifica daca dictionarul e vid 
	bool vid() const;

	// se returneaza iterator pe dictionar
	IteratorDictionar iterator() const;

	// destructorul dictionarului	
	~Dictionar();

};


