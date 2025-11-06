#include "TestScurt.h"
#include "../Colectie(cu-rel)/Colectie.h"
#include "../Colectie(cu-rel)/IteratorColectie.h"
#include <assert.h>

void testAll() {
	Colectie c;
	c.adauga(5);
	c.adauga(6);
	c.adauga(0);
	c.adauga(5);
	c.adauga(10);
	c.adauga(8);

	assert(c.dim() == 6);
	assert(c.nrAparitii(5) == 2);

	assert(c.sterge(5) == true);
	assert(c.dim() == 5);

	assert(c.cauta(6) == true);
	assert(c.vida() == false);

	IteratorColectie ic = c.iterator();
	assert(ic.valid() == true);
	while (ic.valid()) {
		ic.element();
		ic.urmator();
	}
	assert(ic.valid() == false);
	ic.prim();
	assert(ic.valid() == true);

}


void testValoareMaxima() {
	Colectie c;
	try {

		assert(c.valoareMaxima() == false);
	}
	catch(std::exception&) {}

	c.adauga(4);
	c.adauga(2);
	c.adauga(9);
	c.adauga(1);
	c.adauga(9);
	c.adauga(7);

	// Verificăm valoarea maximă (ar trebui să fie 9)
	assert(c.valoareMaxima() == 9);

	c.sterge(9); // ștergem un 9, dar mai rămâne unul
	assert(c.valoareMaxima() == 9);

	c.sterge(9); // ștergem și al doilea 9
	assert(c.valoareMaxima() == 7); // noua valoare maximă este 7

	c.sterge(7);
	c.sterge(4);
	c.sterge(2);
	c.sterge(1);

	try {

		assert(c.valoareMaxima() == false);
	}
	catch(std::exception&) {}
}