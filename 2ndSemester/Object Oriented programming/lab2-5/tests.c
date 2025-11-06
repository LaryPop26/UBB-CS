//
// Created by popla on 12-Mar-25.
//
#include "tests.h"

#include "controller.h"
#include "entity.h"

// entity tests:
void  testCreateParticipant() {
    Participant* participant = createParticipant("Ionescu", "Paula",50);
    assert(strcmp(participant->lastName, "Ionescu") == 0);
    assert(strcmp(participant->firstName,"Paula")==0);
    assert(participant->score == 50);

    destroyParticipant(participant);
}

// MyList tests:

void testIterateList() {
    MyList* l = createEmpty(destroyParticipant);

    Participant* pA = createParticipant("Ionescu", "Paula", 60);
    Participant* pB = createParticipant("Popa", "Ioana", 50);
    add(l, pA);
    add(l, pB);
    assert(size(l) == 2);
    Participant* p = getMyElement(l, 0);
    assert(strcmp(p->lastName, "Ionescu") == 0);
    assert(p->score == 60);
    Participant* p2 = getMyElement(l, 1);
    assert(strcmp(p2->firstName, "Ioana") == 0);
    Participant* p3 = createParticipant("Ionescu","Paula" ,90);
    setMyElement(l,0 ,p3);
    Participant* pUpdate = getMyElement(l, 0);
    assert(strcmp(pUpdate->lastName, "Ionescu") == 0);
    assert(strcmp(pUpdate->firstName, "Paula") == 0);
    assert(pUpdate->score == 90);

    assert(size(l) == 2);
    deleteE(l,1);
    assert(size(l) == 1);
    Participant* pRemaining = getMyElement(l, 0);
    assert(strcmp(pRemaining->lastName, "Ionescu") == 0);
    assert(strcmp(pRemaining->firstName, "Paula") == 0);
    assert(pRemaining->score == 90);
    destroyParticipant(pA);
    destroyParticipant(pB);
    destroyMyList(l);
}

//Controller tests:
void testController() {
    ManagerParticipants testl = createManagerParticipants();
    assert(undo(&testl) == 0);
    int errorCode = addParticipant(&testl, "", "O", 200);
    assert(errorCode == 0);
    assert(size(testl.lstParticipants) == 0);
    errorCode = addParticipant(&testl, "Ionescu", "", 200);
    assert(errorCode == 0);
    assert(size(testl.lstParticipants) == 0);
    errorCode = addParticipant(&testl, "Ionescu", "Paula", 200);
    assert(errorCode == 0);
    assert(size(testl.lstParticipants) == 0);
    addParticipant(&testl, "Ionescu", "Paula", 50);
    assert(size(testl.lstParticipants) == 1);
    errorCode = addParticipant(&testl, "Ionescu", "Paula", 50);
    assert(errorCode == -1);
    assert(size(testl.lstParticipants) == 1);
    addParticipant(&testl, "Dumitrescu", "Alex", 80);
    addParticipant(&testl, "Stan", "Briana", 90);
    addParticipant(&testl, "Iliescu", "George", 20);
    addParticipant(&testl, "Barbu", "Ionela", 50);
    assert(size(testl.lstParticipants) == 5);

    MyList* ls1 = sortByName(&testl);
    assert(size(ls1) == 5);
    Participant* p1 = getMyElement(ls1, 0);
    assert(strcmp(p1->lastName, "Barbu") == 0);
    assert(strcmp(p1->firstName, "Ionela") == 0);
    Participant* p2 = getMyElement(ls1, 4);
    assert(strcmp(p2->lastName, "Stan") == 0);
    assert(strcmp(p2->firstName, "Briana") == 0);
    destroyMyList(ls1);

    MyList* ls3 = sortByScore(&testl);
    assert(size(ls3) == 5);
    Participant* p5 = getMyElement(ls3, 0);
    assert(strcmp(p5->lastName, "Iliescu") == 0);
    assert(strcmp(p5->firstName, "George") == 0);
    Participant* p6 = getMyElement(ls3, 4);
    assert(strcmp(p6->lastName, "Stan") == 0);
    assert(strcmp(p6->firstName, "Briana") == 0);
    destroyMyList(ls3);

    int a = updateParticipant(&testl, "Ionescu", "Paula", 90);
    assert(a==1);
    Participant* p = getMyElement(testl.lstParticipants, 0);
    assert(strcmp(p->lastName, "Ionescu") == 0);
    assert(p->score == 90);

    int err = updateParticipant(&testl, "", "Paula", 90);
    assert(err == 0);

    MyList* l2 = filterScore(&testl, 60);
    assert(size(l2) == 2);
    destroyMyList(l2);

    MyList* l3 = filterFirstLetter(&testl, "I");
    assert(size(l3) == 2);
    destroyMyList(l3);

    MyList* l4 = filterFirstLetter(&testl, "Io");
    assert(size(l4) == 5);
    destroyMyList(l4);

    MyList* l5 = filterScore(&testl, -5);
    assert(size(l5) == 5);
    destroyMyList(l5);

    assert(size(testl.lstParticipants) == 5);
    deleteParticipant(&testl, "Ionescu", "Paula");
    assert(size(testl.lstParticipants) == 4);
    assert(deleteParticipant(&testl, "Ionescu", "Paula")==0);
    assert(size(testl.lstParticipants) == 4);
    undo(&testl);
    assert(size(testl.lstParticipants) == 5);
    destroyManagerParticipants(&testl);
}

void run_tests() {
    testCreateParticipant();

    testIterateList();

    testController();
    printf("All tests passed!\n");
}