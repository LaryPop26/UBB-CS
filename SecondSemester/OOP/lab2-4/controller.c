//
// Created by popla on 11-Mar-25.
//

#include "controller.h"

#include <string.h>

#include "MyList.h"
#include "validation.h"

int addParticipantController(MyList* participants, char* lastName, char* firstName, int score) {
    Participant p = createParticipant(lastName, firstName, score);
    int valCode = validate_entity(p);
    if (valCode != 1) return valCode;
    if (findElem(participants, lastName, firstName) != -1) return -1;
    addElem(participants, p);
    return 0;
}

int updateParticipantController(MyList* participants, char* lastName, char* firstName, int score) {
    Participant participant = createParticipant(lastName, firstName, score);
    int valCode = validate_entity(participant);
    if (valCode != 1) return valCode;
    if (findElem(participants, lastName, firstName) == -1) return -1;
    updateElem(participants, participant);
    return 0;
}

int deleteParticipantController(MyList* participants, int poz) {
    int valCode = validate_int(poz);
    if (valCode != 1) return valCode;
    if (poz >= size(participants)) return 2;
    deleteElem(participants, poz);
    return 0;
}

MyList filterScore(MyList* participants, int score) {
    MyList filteredList = createEmpty();
    for (int i = 0; i < size(participants); i++) {
        Participant p = getMyElement(participants, i);
        if (p.score<score) addElem(&filteredList, p);
    }
    return filteredList;
}

MyList filterFirstLetter(MyList* participants, char* firstLetter) {
    MyList filteredList = createEmpty();
    for (int i = 0; i < size(participants); i++) {
        Participant p = getMyElement(participants, i);
        if (strncmp(p.lastName,firstLetter,1) == 0) addElem(&filteredList, p);
    }
    return filteredList;
}
