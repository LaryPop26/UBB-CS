#include "TestScurt.h"
#include "../Multime(cu-rel)/Multime.h"
#include "../Multime(cu-rel)/IteratorMultime.h"
#include <assert.h>
#include <iostream>
#include <bits/ostream.tcc>

void testAll() { //apelam fiecare functie sa vedem daca exista
	int vverif[5];
	int iverif;
	TElem e;

	Multime m1;
	assert(m1.adauga(5)==true);
	assert(m1.adauga(1)==true);
	assert(m1.adauga(10)==true);
	IteratorMultime im1 =  m1.iterator();
	im1.prim();
	iverif=0;
	e=im1.element();
	vverif[iverif++] = e;
	im1.urmator();
	while (im1.valid()) {
    	assert(rel(e,im1.element()));
 		e = im1.element();
		vverif[iverif++] = e;
		im1.urmator();
	}
	assert((vverif[0]==1) &&(vverif[1]==5)&&(vverif[2]==10));


	Multime m;
	//return;
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
	iverif=0;
	im.prim();
	e = im.element();
	vverif[iverif++] = e;
	im.urmator();
	while (im.valid()) {
		assert(rel(e,im.element()));
		e = im.element();
		vverif[iverif++] = e;
		im.urmator();
	}
	assert((vverif[3]==10) &&(vverif[2]==7)&&(vverif[1]==5)&&(vverif[0]==-3));

}

void testIntersectie() {
	Multime mA;
	mA.adauga(1);
	mA.adauga(2);
	mA.adauga(3);
	mA.adauga(4);
	mA.adauga(5);

	Multime mB;
	mB.adauga(3);
	mB.adauga(4);
	mB.adauga(5);
	mB.adauga(6);
	mB.adauga(7);

	mA.intersectie(mB); // mA trebuie să conțină doar 3, 4, 5

	IteratorMultime it = mA.iterator();
	it.prim();
	int v[3], i = 0;
	while (it.valid()) {
		v[i++] = it.element();
		it.urmator();
	}
	assert(i == 3);
	assert(v[0] == 3);
	assert(v[1] == 4);
	assert(v[2] == 5);

	// Test intersectie când nu există elemente comune
	Multime mC;
	mC.adauga(1);
	mC.adauga(2);

	Multime mD;
	mD.adauga(100);
	mD.adauga(200);

	mC.intersectie(mD); // mC trebuie să fie vidă

	assert(mC.vida() == true);

}