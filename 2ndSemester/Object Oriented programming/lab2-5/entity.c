//
// Created by popla on 11-Mar-25.
//
#include "entity.h"
#include <stdlib.h>
#include <string.h>

Participant* createParticipant(char* lastName, char* firstName, int score) {
    Participant* p = malloc(sizeof(Participant));

    int nrC = (int) strlen(lastName) + 1;
    p->lastName = malloc(sizeof(char) * nrC);
    strcpy(p->lastName,lastName);

    nrC = (int) strlen(firstName) + 1;
    p->firstName =malloc(sizeof(char) * nrC);
    strcpy(p->firstName,firstName);

    p->score = score;
    return p;
}

void destroyParticipant(void* p) {
    Participant* pt = (Participant*) p;
    free(pt->lastName);
    free(pt->firstName);
    free(pt);
}

void* copyParticipant(void* p) {
    Participant* participant = (Participant*) p;
    return createParticipant(participant->lastName, participant->firstName, participant->score);
}