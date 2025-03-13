//
// Created by popla on 12-Mar-25.
//
#include "entity.h"

#ifndef REPOSITORY_H
#define REPOSITORY_H

typedef struct {
    Participant elems[100];
    int length;
}ParticipantsList;

/*
 * Add a participant in list
 * params: participant - Participant, entitate
 *         participants - list of all participants
 * return: a new participant added in the list
 */
int addParticipant(ParticipantsList* participants, Participant participant);

/*
 * Modify a participant in list
 * params: participant - Participant, entitate
 *         participants - list of all participants
 * return: list
 */
int modifyParticipant(ParticipantsList* participants, Participant participant);

/*
 *
 */
int deleteParticipant(ParticipantsList* participants, int ID);

int findParticipant(ParticipantsList* participants, char name);
#endif //REPOSITORY_H
