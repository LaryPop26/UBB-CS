//
// Created by popla on 12-Mar-25.
//
#include "tests.h"

#include "controller.h"

// entity tests:
void  testCreateParticipant() {
    Participant participant = createParticipant("Ionescu", "Paula",50);
    assert(strcmp(participant.lastName, "Ionescu") == 0);
    assert(strcmp(participant.firstName,"Paula")==0);
    assert(participant.score == 50);

    destroyParticipant(&participant);
    assert(strlen(participant.lastName) == 0);
    assert(strlen(participant.firstName)==0);
    assert(participant.score == -1);
}

// MyList tests:
void testCreateList() {
    MyList l = createEmpty();
    assert(size(&l) == 0);
}

void testIterateList() {
    MyList l = createEmpty();
    addElem(&l, createParticipant("Ionescu", "Paula", 60));
    addElem(&l, createParticipant("Popa", "Ioana", 50));
    assert(size(&l) == 2);
    Participant p = getMyElement(&l, 0);
    assert(strcmp(p.lastName, "Ionescu") == 0);
    assert(p.score == 60);
    Participant p2 = getMyElement(&l, 1);
    assert(strcmp(p2.firstName, "Ioana") == 0);
    Participant p3 = createParticipant("Ionescu","Paula" ,90);
    updateElem(&l, p3);
    Participant pUpdate = getMyElement(&l, 0);
    assert(strcmp(pUpdate.lastName, "Ionescu") == 0);
    assert(strcmp(pUpdate.firstName, "Paula") == 0);
    assert(pUpdate.score == 90);

    assert(size(&l) == 2);
    deleteElem(&l,1);
    assert(size(&l) == 1);
    Participant pRemaining = getMyElement(&l, 0);
    assert(strcmp(pRemaining.lastName, "Ionescu") == 0);
    assert(strcmp(pRemaining.firstName, "Paula") == 0);
    assert(pRemaining.score == 90);
    MyList l2 = copyMyList(&l);
    assert(size(&l2) == 1);
    Participant pn = getMyElement(&l2, 0);
    assert(strcmp(pn.lastName, "Ionescu") == 0);
    destroyMyList(&l);
    assert(size(&l) == 0);
}

//Controller tests:
void testController() {
    MyList testl = createEmpty();
    int errorCode = addParticipantController(&testl, "", "O", 200);
    assert(errorCode == 2);
    assert(size(&testl) == 0);
    errorCode = addParticipantController(&testl, "Ionescu", "", 200);
    assert(errorCode == 3);
    assert(size(&testl) == 0);
    errorCode = addParticipantController(&testl, "Ionescu", "Paula", 200);
    assert(errorCode == 4);
    assert(size(&testl) == 0);
    addParticipantController(&testl, "Ionescu", "Paula", 50);
    assert(size(&testl) == 1);
    addParticipantController(&testl, "Dumitrescu", "Alex", 80);
    addParticipantController(&testl, "Stan", "Briana", 90);
    addParticipantController(&testl, "Iliescu", "George", 20);
    addParticipantController(&testl, "Barbu", "Ionela", 40);
    assert(size(&testl) == 5);

    updateParticipantController(&testl, "Ionescu", "Paula", 90);
    Participant p = getMyElement(&testl, 0);
    assert(strcmp(p.lastName, "Ionescu") == 0);
    assert(p.score == 90);

    MyList l2 = filterScore(&testl, 50);
    assert(size(&l2) == 2);
    destroyMyList(&l2);

    MyList l3 = filterFirstLetter(&testl, "I");
    assert(size(&l3) == 2);
    destroyMyList(&l3);

    deleteParticipantController(&testl, 4);
    assert(size(&testl) == 4);

    destroyMyList(&testl);
}

void run_tests() {
    testCreateParticipant();

    testCreateList();
    testIterateList();

    testController();
    printf("All tests passed!\n");
}