#include "IteratorMultime.h"
#include "Multime.h"

IteratorMultime::IteratorMultime(const Multime& m): mult(m) {
	/* de adaugat */
	curent = mult.prim;
}

// Teta(1)
TElem IteratorMultime::element() const {
	/* de adaugat */
	return curent->getEl();
}

// Teta(1)
bool IteratorMultime::valid() const {
	/* de adaugat */
	return curent != nullptr;
}

// Teta(1)
void IteratorMultime::urmator() {
	/* de adaugat */
	curent=curent->getUrmator();
}

// Teta(1)
void IteratorMultime::prim() {
	/* de adaugat */
	curent=mult.prim;
}

