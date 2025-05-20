#include "TestScurt.h"
#include <assert.h>
#include "../Multime/Multime.h"
#include "../Multime/IteratorMultime.h"

void testAll() { //apelam fiecare functie sa vedem daca exista
	Multime m;
	assert(m.vida() == true);
	assert(m.dim() == 0); //adaug niste elemente
	assert(m.adauga(5)==true);
	assert(m.adauga(1)==true);
	assert(m.adauga(10)==true);
	assert(m.adauga(7)==true);
	assert(m.adauga(1)==false);
	assert(m.adauga(10)==false);
	assert(m.adauga(-3)==true);
	assert(m.dim() == 5);
	assert(m.cauta(10) == true);
	assert(m.cauta(16) == false);
	assert(m.sterge(1) == true);
	assert(m.sterge(6) == false);
	assert(m.dim() == 4);


	IteratorMultime im = m.iterator();
	im.prim();
	int s = 0;
	while (im.valid()) {
		TElem e = im.element();
		s += e;
		im.urmator();
	}
	assert(s == 19);

}

void test_diferentaMaxMin() {
	Multime m;

	// cazul multimii vide
	assert(m.diferentaMaxMin() == -1);

	// adăugăm elemente
	m.adauga(10);
	m.adauga(3);
	m.adauga(7);
	m.adauga(20);
	m.adauga(-5);

	// minim -5, maxim 20 => diferenta = 25
	assert(m.diferentaMaxMin() == 25);

	// adăugăm un element duplicat - nu trebuie să influențeze rezultatul
	m.adauga(10);
	assert(m.diferentaMaxMin() == 25);

	// eliminăm elementul maxim (20)
	m.sterge(20);
	// noua valoare maxima este 10 => diferenta = 15
	assert(m.diferentaMaxMin() == 15);

	// eliminăm toate elementele
	m.sterge(10);
	m.sterge(3);
	m.sterge(7);
	m.sterge(-5);
	assert(m.diferentaMaxMin() == -1); // din nou, mulțimea e vidă
}