//
// Created by popla on 11-Mar-25.
//

#ifndef ENTITY_H
#define ENTITY_H

typedef struct {
    int ID;
    char lastName[30];
    char firstName[30];
    int score;
}Participant;

/*
 * Create a new participant
 */
Participant createParticipant(char* lastName, char* firstName, int score);

/*
 * Dealocate memory ocupied by pet
 */
void destroyParticipant(Participant* participant);

#endif //ENTITY_H
