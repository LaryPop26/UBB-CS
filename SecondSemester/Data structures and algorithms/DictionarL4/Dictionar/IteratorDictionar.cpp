#include "IteratorDictionar.h"
#include <exception>
#include "Dictionar.h"

using namespace std;

IteratorDictionar::IteratorDictionar(const Dictionar& d) : dict(d){
	/* de adaugat */
	curent = dict.prim;
}

//Teta(1)
void IteratorDictionar::prim() {
	/* de adaugat */
	curent = dict.prim;
}

//Teta(1)
void IteratorDictionar::urmator() {
	/* de adaugat */
	if (!valid()) throw std::exception();
	curent = dict.urm[curent];
}

//Teta(1)
TElem IteratorDictionar::element() const{
	/* de adaugat */
	return dict.e[curent];
}

//Teta(1)
bool IteratorDictionar::valid() const {
	/* de adaugat */
	return curent != -1;
}

// CF: Teta(1) - k = 1 - se face un singur pas
// CT = CD: Teta(min(k,n)) - k<=n - exista destule elem sa avanseze k pasi
// 							 k>n  - se parcurge lista pana la final
void IteratorDictionar::avanseazaKPasi(int k) {
	if (!valid() || k <= 0) {
		throw std::exception();
	}

	for (int i = 0; i < k; i++) {
		if (!valid()) {
			curent = -1;
			throw std::exception();
		}
		curent = dict.urm[curent];
	}
}

/*
 * Subalgoritm avanseazaKPasi(dict, k - integer)
 *		{pre: Iterator i - valid
 *		@ arunca exceptie : iterator nu e valid / k<=0
 *		Pentru i<-0,k executa
 *			Daca ¬i.valid atunci
 *				curent <- -1
 *			SfDaca
 *		curent <- dict.urm[curent]
 *		SfPentru
 *	SfSubalgoritm
 */