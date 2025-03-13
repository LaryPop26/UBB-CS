//
// Created by popla on 12-Mar-25.
//

#include "repository.h"

int addParticipant(ParticipantsList* participants, Participant participant) {
    int found = 0;
    for (int i = 0; i < participants->length; i++) {
        if (participant.lastName == participants->elems[i].lastName && participant.firstName == participants->elems[i].firstName) {
            found = 1;
        }
    }
    if (!found) {
        participants->elems[participants->length] = participant;
        participants->length++;
        return 1;
    }
    return 0;
}

int modifyParticipant(ParticipantsList* participants, Participant participant) {
    for (int i = 0; i < participants->length; i++) {
        if (participant.ID == participants->elems[i].ID) {
            participants->elems[i] = participant;
            return 1;
        }
    }
    return 0;
}

int deleteParticipant(ParticipantsList* participants, int ID) {
    int p = 0;
    for (int i = 0; i < participants->length; i++) {
        if (ID == participants->elems[i].ID) p = 1;
        if (p == 1) participants->elems[i] = participants->elems[i + 1];
    }
    if (p == 1) {
        participants->length--;
        return 1;
    }
    return 0;
}