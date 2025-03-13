//
// Created by popla on 11-Mar-25.
//
#ifndef MYLIST_H
#define MYLIST_H

#include "entity.h"
#define MAX_PARTICIPANTS 100
typedef Participant ElemType;
typedef struct {
    ElemType elems[MAX_PARTICIPANTS];
    int length;
}MyList;

/*
 * Create an empty list
 */
MyList createEmpty();

/*
 * Destroy list
 */
void destroyMyList(MyList* myList);

/*
 * Get an element from the list
 * param: myList - MyList*, the given list
 *        poz - position of element, need to be valid
 * return: element found on position poz
 */
ElemType getMyElement(MyList* myList, int poz);

/*
 * return number of elements in the list
 */
int size(MyList* myList);

/*
 * Add element into the list
 * param: myList - MyList*, the given list
 *        el - ElemType, el to be added
 * post: element is added to the end of the list
 */
void addElem(MyList* myList, ElemType eL);

/*
 * Set a given element into position poz
 * param: myList - MyList*, the given list
 *        poz - position of element, need to be valid (poz< myList.length)
 *        el - ElemType, el to be added
 * return: the previous elemoent in the position
 */
ElemType setMyElement(MyList* myList, int poz, ElemType eL);

/*
 * Delete an element from position poz
 * param: myList - MyList*, the given list
 *        poz - position of element, need to be valid
 * return; deleted element
 */
ElemType deleteElem(MyList* myList, int poz);

/*
 * Update score of one participant
 * param: myList - MyList*, the given list
 *        el - ElemType, el to be added
 * post: entity score is modified
 */

ElemType updateElem(MyList* myList, ElemType eL);

/*
 *
 */
int findElem(MyList* myList, char* lastName, char* firstName);

/*
 * Make a shallow copy of the list
 * return MyList containing the same elements as original list
 */
MyList copyMyList(MyList* myList);

#endif //MYLIST_H
