//
// Created by popla on 11-Mar-25.
//

#include <string.h>
#include "controller.h"
#include "MyList.h"
#include "validation.h"
#include "mysort.h"

ManagerParticipants createManagerParticipants() {
    ManagerParticipants contest;
    contest.lstParticipants = createEmpty(destroyParticipant);
    contest.undoLst = createEmpty(destroyMyList);
    return contest;
}

void destroyManagerParticipants(ManagerParticipants* contest) {
    destroyMyList(contest->lstParticipants);
    destroyMyList(contest->undoLst);
}

int addParticipant(ManagerParticipants* contest, char* lastName, char* firstName, int score) {
    Participant* p = createParticipant(lastName, firstName, score);
    int successful = validate_entity(p);
    if (!successful) {
        destroyParticipant(p);
        return 0;
    }
    if (findElem(contest, lastName, firstName) != -1) {
        destroyParticipant(p);
        return -1;
    }
    MyList* toUndo = copyMyList(contest->lstParticipants, copyParticipant);
    add(contest->undoLst, toUndo);
    add(contest->lstParticipants, p);
    return 1;
}

int findElem(ManagerParticipants* contest, char* lastName, char* firstName) {
    int poz = -1;
    for (int i = 0; i < contest->lstParticipants->length; i++) {
        Participant* p = getMyElement(contest->lstParticipants, i);
        if (strcmp(p->lastName, lastName) == 0 && strcmp(p->firstName, firstName) == 0) {
            poz = i;
            break;;
        }
    }
    return poz;
}

int updateParticipant(ManagerParticipants* contest, char* lastName, char* firstName, int newScore) {
    int position = findElem(contest, lastName, firstName);
    if (position != -1) {
        MyList* toUndo = copyMyList(contest->lstParticipants, copyParticipant);
        add(contest->undoLst, toUndo);

        Participant* newP = createParticipant(lastName, firstName, newScore);
        Participant* replacedP = setMyElement(contest->lstParticipants, position, newP);
        destroyParticipant(replacedP);
        return 1;
    }
    return 0;
}

int deleteParticipant(ManagerParticipants* contest, char* lastName, char* firstName) {
    int position = findElem(contest, lastName, firstName);
    if (position != -1) {
        MyList* toUndo = copyMyList(contest->lstParticipants, copyParticipant);
        add(contest->undoLst, toUndo);

        Participant* p = deleteE(contest->lstParticipants, position);
        destroyParticipant(p);
        return 1;
    }
    return 0;
}

MyList* filterScore(ManagerParticipants* contest, int maxScore) {
    if (validate_int(maxScore)) {
        MyList* filteredList = createEmpty(destroyParticipant);
        for (int i = 0; i < size(contest->lstParticipants); i++) {
            Participant* p = getMyElement(contest->lstParticipants, i);
            if (p->score<maxScore)
                add(filteredList, copyParticipant(p));
        }
        return filteredList;
    }
    return copyMyList(contest->lstParticipants, copyParticipant);
}

MyList* filterFirstLetter(ManagerParticipants* contest, char* firstLetter) {
    if (strlen(firstLetter)==1) {
        MyList* filteredList = createEmpty(destroyParticipant);
        for (int i = 0; i < size(contest->lstParticipants); i++) {
            Participant* p = getMyElement(contest->lstParticipants, i);
            if (strncmp(p->lastName,firstLetter,1) == 0)
                add(filteredList, createParticipant(p->lastName,p->firstName,p->score));
        }
        return filteredList;
    }
    return copyMyList(contest->lstParticipants, copyParticipant);
}

int cmpName(void* p1, void* p2) {
    Participant *p11 = (Participant*)p1;
    Participant *p22 = (Participant*)p2;
    return strcmp(p11->lastName, p22->lastName);
}

int cmpScore(void* p1, void* p2) {
    Participant *p11 = (Participant*)p1;
    Participant *p22 = (Participant*)p2;
    if (p11->score == p22->score)
        return 0;
    if (p11->score > p22->score)
        return 1;
    return -1;
}

MyList* sortByName(ManagerParticipants* contest) {
    MyList* sortedList = copyMyList(contest->lstParticipants, copyParticipant);
    sort(sortedList, cmpName);
    return sortedList;
}

MyList* sortByScore(ManagerParticipants* contest) {
    MyList* sortedList = copyMyList(contest->lstParticipants, copyParticipant);
    sort(sortedList, cmpScore);
    return sortedList;
}

int undo(ManagerParticipants* contest) {
    if (size(contest->undoLst) == 0)
        return 0;
    MyList* lst = deleteE(contest->undoLst, contest->undoLst->length-1);
    destroyMyList(contest->lstParticipants);
    contest->lstParticipants = lst;
    return 1;
}