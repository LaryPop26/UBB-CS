//
// Created by popla on 11-Mar-25.
//
#ifndef MYLIST_H
#define MYLIST_H
#include "entity.h"

typedef void* TElem;
typedef void (*DestroyFct)(TElem);
typedef TElem (*CopyFct)(TElem);

typedef struct {
    TElem* elems;
    int length;
    int capacity;
    DestroyFct destroy;
}MyList;

/*
 * Create an empty list with a destruction function
 */
MyList* createEmpty(DestroyFct f);

/*
 * Destroy list and alements
 * @param myList: list to be destroyed
 * post: free the memory used by list and elements
 */
void destroyMyList(void* lst);

/*
 * Get an element from the list
 * @param: myList - MyList*, the given list
 * @param: poz - position of element,
 * pre: need to be valid
 * @return: element found on position poz
 */
TElem getMyElement(MyList* lst, int poz);

/*
 *
 */
TElem setMyElement(MyList* lst, int poz, TElem e);

/*
 * return number of elements in the list
 */
int size(MyList* lst);

/*
 * Add element into the list
 * param: myList - MyList*, the given list
 *        el - ElemType, el to be added
 * post: element is added to the end of the list
 */
void add(MyList* lst, TElem el);

/*
 * Delete an element from position poz
 * param: myList - MyList*, the given list
 *        poz - position of element, need to be valid
 * return; deleted element
 */
TElem deleteE(MyList* lst, int poz);

/*
 * Make a shallow copy of the list
 * return MyList containing the same elements as original list
 */
MyList* copyMyList(MyList* lst, CopyFct c);

#endif //MYLIST_H
