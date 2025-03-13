//
// Created by popla on 11-Mar-25.
//

#include "MyList.h"
#include <string.h>

MyList createEmpty() {
    MyList participants;
    participants.length = 0;
    return participants;
}

void destroyMyList(MyList* myList) {
    myList->length = 0;
}

void addElem(MyList* myList, ElemType eL) {
    myList->elems[myList->length] = eL;
    myList->length++;
}

ElemType getMyElement(MyList* myList, int poz) {
    return myList->elems[poz];
}

ElemType setMyElement(MyList* myList, int poz, ElemType elem) {
    ElemType delElem = getMyElement(myList, poz);
    myList->elems[poz] = elem;
    return delElem;
}

ElemType deleteElem(MyList* myList, int poz) {
    ElemType delElem = getMyElement(myList, poz);
    ElemType lastElem = getMyElement(myList, myList->length - 1);
    setMyElement(myList, poz, lastElem);
    myList->length--;
    return delElem;
}

ElemType updateElem(MyList* participants, Participant participant) {
    for (int i = 0; i < participants->length; i++) {
        if (strcmp(participant.lastName,participants->elems[i].lastName)==0
            && strcmp(participant.firstName, participants->elems[i].firstName)==0) {
            participants->elems[i] = participant;
        }
    }
    return participant;
}

int findElem(MyList* participants, char* lastName, char* firstName) {
    for (int i = 0; i < participants->length; i++) {
        if (strcmp(participants->elems[i].lastName, lastName) == 0 &&
            strcmp(participants->elems[i].firstName, firstName) == 0) {
            return i; // Returnează poziția participantului
            }
    }
    return -1; // Nu a fost găsit
}

int size(MyList* myList) {
    return myList->length;
}

MyList copyMyList(MyList* myList) {
    MyList participants=createEmpty();
    for (int i = 0; i < size(myList); i++) {
        ElemType eL=getMyElement(myList, i);
        addElem(&participants, eL);
    }
    return participants;
}