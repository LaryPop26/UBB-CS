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

void destroyParticipant(Participant* p) {
    free(p->lastName);
    free(p->firstName);
    free(p);
}

Participant* copyParticipant(Participant* p) {
    return createParticipant(p->lastName, p->firstName, p->score);
}