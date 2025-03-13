//
// Created by popla on 11-Mar-25.
//
#include "entity.h"
#include <string.h>

Participant createParticipant(char* lastName, char* firstName, int score) {
    Participant participant;
    strcpy_s(participant.lastName,sizeof(participant.lastName), lastName);
    strcpy_s(participant.firstName,sizeof(participant.firstName), firstName);
    participant.score = score;
    return participant;
}

void destroyParticipant(Participant* participant) {
    participant->lastName[0] = '\0';
    participant->firstName[0] = '\0';
    participant->score = -1;
}
