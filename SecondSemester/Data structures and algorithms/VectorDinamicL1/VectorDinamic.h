#pragma once
//tip de data generic (pentru moment este intreg)

typedef int TElem;

class IteratorVectorDinamic;


class VectorDinamic {
 friend class IteratorVectorDinamic;
private:
	int max_size;
	// redimensionare
	void redim();

	int *array;
	int used;

public:
		// constructor
		// arunca exceptie in cazul in care capacitate e <=0
		// Complexitate:Teta(1) CF=CM=CD=CT
		VectorDinamic (int capacitate);

		// returnare dimensiune
		// Complexitate:Teta(1) CF=CM=CD=CT
		int dim() const;

		// Complexitate:Teta(1) CF=CM=CD=CT
		TElem* get_arr() const;

		// Complexitate:Teta(1) CF=CM=CD=CT
		int get_used() const ;

		// returnare element
		// arunca exceptie daca i nu e valid
		// indicii ii consideram de la 0
		// Complexitate:Teta(1) CF=CM=CD=CT
		TElem element(int i) const;

		// modifica element de pe pozitia i si returneaza vechea valoare
		// arunca exceptie daca i nu e valid
		// Complexitate:Teta(1) CF=CM=CD=CT
		TElem modifica(int i, TElem e);

		// adaugare element la sfarsit
		// Complexitate
		// Teta(1) CF + nu e nevoie de redmiensionare
		// Teta(n) CD e nevoie de redimensionare
		// Teta(n) CM
		// O(n) CT
		void adaugaSfarsit(TElem e);

		// adaugare element pe o pozitie i
		// arunca exceptie daca i nu e valid
		// Complexitate
		// Teta(1)  CF - i==n + nu e nevoie de redimensionare
		// Teta(n)  CD - i==0 + e nevoie de redimensionare
		// Teta(n)  CM
		// O(n)  CT
		void adauga(int i, TElem e);

		// sterge element de pe o pozitie i si returneaza elementul sters
		// arunca exceptie daca i nu e valid
		// Complexitate
		// Teta(1)  CF - i==n
		// Teta(n)  CD - i==0
		// Teta(n)  CM
		// O(n)  CT
		TElem sterge(int i);

		// returnare iterator
		//O(1) CF=CD=CM=CT
		IteratorVectorDinamic iterator();

		// elimina toate elementele intre doua pozitii i si j
		// arunca exceptie in cazul in care i sau/si j nevalide
		// Complexitate
		// CF = Teta(1) nu se muta nimic
		// CD =  Teta(n) se sterg foarte multe elem
		// CT O(n) se muta n elem
		void eliminaIntre(int i, int j);

		// destructor
		// Teta(n) CF=CD=CM=CT
		~VectorDinamic();
};







