#include "IteratorVectorDinamic.h"
#include "VectorDinamic.h"


IteratorVectorDinamic::IteratorVectorDinamic(const VectorDinamic& _v) :	v(_v) {
	this->act=v.array;
	this->poz=0;
}

void IteratorVectorDinamic::prim() {
	this->act=v.get_arr();
	this->poz=0;
}

bool IteratorVectorDinamic::valid() const{
	if(this->poz<v.get_used())
		return true;
	return false;
}

TElem IteratorVectorDinamic::element() const{
	return *this->act;
}

void IteratorVectorDinamic::urmator() {
	this->act+=1;
	this->poz+=1;
}

