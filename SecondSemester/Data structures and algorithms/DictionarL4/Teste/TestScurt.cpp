#include "TestScurt.h"
#include <assert.h>
#include <exception>

#include "../Dictionar/Dictionar.h"
#include "../Dictionar/IteratorDictionar.h"


void testAll() { //apelam fiecare functie sa vedem daca exista
	Dictionar d;
	assert(d.vid() == true);
	assert(d.dim() == 0); //adaug niste elemente
	assert(d.adauga(5,5)==NULL_TVALOARE);
	assert(d.adauga(1,111)==NULL_TVALOARE);
	assert(d.adauga(10,110)==NULL_TVALOARE);
	assert(d.adauga(7,7)==NULL_TVALOARE);
	assert(d.adauga(1,1)==111);
	assert(d.adauga(10,10)==110);
	assert(d.adauga(-3,-3)==NULL_TVALOARE);
	assert(d.dim() == 5);
	assert(d.cauta(10) == 10);
	assert(d.cauta(16) == -1);
	assert(d.sterge(1) == 1);
	assert(d.sterge(6) == -1);
	assert(d.dim() == 4);


	TElem e;
	IteratorDictionar id = d.iterator();
	id.prim();
	int s1 = 0, s2 = 0;
	while (id.valid()) {
		e = id.element();
		s1 += e.first;
		s2 += e.second;
		id.urmator();
	}
	assert(s1 == 19);
	assert(s2 == 19);
}

void testAvanseazaKPasi() {
    Dictionar d;

    // Populăm dicționarul cu elemente
    d.adauga(1, 100);
    d.adauga(2, 200);
    d.adauga(3, 300);
    d.adauga(4, 400);
    d.adauga(5, 500);

    IteratorDictionar id = d.iterator();

    // Test 1: Avansare cu k = 1
    id.prim();
    id.avanseazaKPasi(1);
    assert(id.element().first == 2);

    // Test 2: Avansare cu k > 1
    id.prim();
    id.avanseazaKPasi(2);
    assert(id.element().first == 3);

    // Test 3: Avansare până la ultimul element
    id.prim();
    id.avanseazaKPasi(4);
    assert(id.element().first == 5);

    // Test 4: k negativ - ar trebui să arunce excepție
    id.prim();
    try {
        id.avanseazaKPasi(-1);
        assert(false);  // Nu ar trebui să ajungă aici
    }
    catch (std::exception&) {
        assert(true);
    }

    // Test 5: k = 0 - ar trebui să arunce excepție
    try {
        id.avanseazaKPasi(0);
        assert(false);  // Nu ar trebui să ajungă aici
    }
    catch (std::exception&) {
        assert(true);
    }

    // Test 6: Iterator invalid - ar trebui să arunce excepție
    id.prim();
    id.avanseazaKPasi(5);  // Ajunge la sfârșit
    try {
        id.avanseazaKPasi(1);
        assert(false);  // Nu ar trebui să ajungă aici
    }
    catch (std::exception&) {
        assert(true);
    }

    // Test 7: k mai mare decât numărul de elemente rămase
    id.prim();
    try {
        id.avanseazaKPasi(6);
        assert(false);  // Nu ar trebui să ajungă aici
    }
    catch (std::exception&) {
        assert(true);
    }

    // Test 8: Avansare multiplă secvențială
    id.prim();
    id.avanseazaKPasi(2);
    assert(id.element().first == 3);
    id.avanseazaKPasi(1);
    assert(id.element().first == 4);

    // Test 9: Dicționar cu un singur element
    Dictionar d2;
    d2.adauga(1, 100);
    IteratorDictionar id2 = d2.iterator();
    try {
        id2.avanseazaKPasi(2);
        assert(false);  // Nu ar trebui să ajungă aici
    }
    catch (std::exception&) {
        assert(true);
    }
}





void testFiltreaza() {
	Dictionar d;

	// Test on empty dictionary
	auto estePar = [](TCheie c) { return c % 2 == 0; };
	d.filtreaza(estePar);
	assert(d.vid() == true);

	// Add some elements
	d.adauga(1, 100);
	d.adauga(2, 200);
	d.adauga(3, 300);
	d.adauga(4, 400);
	d.adauga(5, 500);
	assert(d.dim() == 5);

	// Filter even numbers (should keep odd numbers)
	d.filtreaza(estePar);
	assert(d.dim() == 3);  // Should keep 1, 3, 5
	assert(d.cauta(1) == 100);
	assert(d.cauta(2) == NULL_TVALOARE);
	assert(d.cauta(3) == 300);
	assert(d.cauta(4) == NULL_TVALOARE);
	assert(d.cauta(5) == 500);

	// Test with another condition (numbers greater than 3)
	Dictionar d2;
	d2.adauga(1, 100);
	d2.adauga(2, 200);
	d2.adauga(3, 300);
	d2.adauga(4, 400);
	d2.adauga(5, 500);

	auto maiMare3 = [](TCheie c) { return c > 3; };
	d2.filtreaza(maiMare3);
	assert(d2.dim() == 3);  // Should keep 1, 2, 3
	assert(d2.cauta(1) == 100);
	assert(d2.cauta(2) == 200);
	assert(d2.cauta(3) == 300);
	assert(d2.cauta(4) == NULL_TVALOARE);
	assert(d2.cauta(5) == NULL_TVALOARE);

	// Test filtering all elements
	auto all = [](TCheie) { return true; };
	d2.filtreaza(all);
	assert(d2.vid() == true);
	assert(d2.dim() == 0);
}

