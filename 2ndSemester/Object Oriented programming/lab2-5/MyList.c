//
// Created by popla on 11-Mar-25.
//

#include "MyList.h"
#include <stdlib.h>

MyList* createEmpty(DestroyFct f) {
    MyList* lst = malloc(sizeof(MyList));
    lst->capacity = 2;
    lst->length = 0;
    lst->destroy = f;
    lst->elems = malloc(sizeof(TElem) * lst->capacity);

    return lst;
}

void destroyMyList(void* list) {
    MyList* lst = (MyList*)list;
    for (int i = 0; i < lst->length; i++) {
        lst->destroy(lst->elems[i]);
    }

    free(lst->elems);
    lst->length = 0;
    free(lst);
}

TElem getMyElement(MyList* lst, int poz) {
    return lst->elems[poz];
}

TElem setMyElement(MyList* lst, int poz, TElem el) {
    TElem replaced = getMyElement(lst, poz);
    lst->elems[poz] = el;
    return replaced;
}

void add(MyList* lst, TElem el) {
    if (lst->capacity == lst->length) {
        int newCapacity = lst->capacity * 2;
        TElem* newElements = malloc(newCapacity * sizeof(TElem));
        for (int i = 0; i < lst->length; i++) {
            newElements[i] = lst->elems[i];
        }
        free(lst->elems);
        lst->elems = newElements;
        lst->capacity = newCapacity;
    }
    lst->elems[lst->length] = el;
    lst->length++;
}

TElem deleteE(MyList* lst, int poz) {
    TElem delElem = getMyElement(lst, poz);
    for (int i = poz; i < lst->length-1; i++) {
        lst->elems[i] = lst->elems[i+1];
    }
    lst->length--;
    return delElem;
}

int size(MyList* lst) {
    return lst->length;
}

MyList* copyMyList(MyList* lst, CopyFct copyFct) {
    MyList* copyList = createEmpty(lst->destroy);
    for (int i = 0; i < size(lst); i++) {
        TElem el=getMyElement(lst, i);
        add(copyList, copyFct(el));
    }
    return copyList;
}