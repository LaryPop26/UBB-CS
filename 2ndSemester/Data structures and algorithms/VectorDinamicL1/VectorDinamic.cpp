#include "VectorDinamic.h"
#include "IteratorVectorDinamic.h"
#include <exception>

using namespace std;

// Teta(n)
void VectorDinamic::redim() {
	this->max_size *= 2;
	TElem *temp = new int[this->max_size];
	for (int i = 0; i < this->max_size/2; i++)
		temp[i] = this->array[i];
	delete[] this->array;
	this->array = temp;
}

VectorDinamic::VectorDinamic(int cp) {
    if (cp <= 0) throw exception();
	this->array = new int [cp];
    this->used = 0;
	this->max_size = cp;
}

// Complexitate:Teta(1) CF=CM=CD=CT
int VectorDinamic::dim() const{
	return this->used;
}

// Complexitate:Teta(1) CF=CM=CD=CT
TElem VectorDinamic::element(int i) const{
    if(i < 0 || i >= this->used) throw exception();
	return this->array[i];
}

// Complexitate:Teta(1) CF=CM=CD=CT
TElem VectorDinamic::modifica(int i, TElem e) {
	if (i < 0 || i >= this->used)
		throw exception();
	int elem = this->array[i];
	this->array[i]=e;
	return elem;
}

//Complexitate
//Teta(1) CF + nu e nevoie de redmiensionare
//Teta(n) CD e nevoie de redimensionare
//Teta(n) CM
//O(n) CT
void VectorDinamic::adaugaSfarsit(TElem e) {
	if (this->used == this->max_size-1)
		this->redim();
	this->array[this->used] = e;
	this->used++;
}

// Complexitate
//Teta(1)  CF - i==n + nu e nevoie de redimensionare
//Teta(n)  CD - i==0 + e nevoie de redimensionare
//Teta(n)  CM
//O(n)  CT
void VectorDinamic::adauga(int i, TElem e) {
     if (this->used == this->max_size)
     	this->redim();
	for (int index = this->used; index > i; index--)
		this->array[index] = this->array[index-1];
	this->array[i] = e;
	this->used++;
}

//Complexitate
//Teta(1)  CF - i==n
//Teta(n)  CD - i==0
//Teta(n)  CM
//O(n)  CT
TElem VectorDinamic::sterge(int i) {
	if (i < 0 || i >= this->used)
		throw exception();
	int elem = this->array[i];
	for (int index = i; index < this->used - 1; index++)
		this->array[index] = this->array[index + 1];
	this->used--;
	return elem;
}

// Complexitate
// Teta(1) CF nu se muta nimic
// Teta(n) CD se sterg foarte multe elem
// O(n)  CT
void VectorDinamic::eliminaIntre(int i, int j) {
	if (i < 0 || j >= this->used || i > j)
		throw exception();
	int nrElem = j - i + 1;
	for (int index = i; index < this->used - nrElem; index++)
		this->array[index] = this->array[index + nrElem];
	this->used -= nrElem;
}

IteratorVectorDinamic VectorDinamic::iterator() {
	return IteratorVectorDinamic(*this);
}

VectorDinamic::~VectorDinamic() {
	delete[] this->array;
}

// Complexitate:Teta(1) CF=CM=CD=CT
TElem* VectorDinamic::get_arr() const {
	return this->array;}

// Complexitate:Teta(1) CF=CM=CD=CT
int VectorDinamic::get_used() const {
	return this->used;}

