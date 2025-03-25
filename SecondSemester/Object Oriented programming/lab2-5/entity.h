//
// Created by popla on 11-Mar-25.
//

#ifndef ENTITY_H
#define ENTITY_H

typedef struct {
    char* lastName;
    char* firstName;
    int score;
}Participant;

/*
 * Create a new participant
 * param: lastname - str, lastname of a participant
 *        firstname - str, firstname of a participant
 *        score - int, obtained score
 * return: created participant
 */
Participant* createParticipant(char* lastName, char* firstName, int score);

/*
 * Dealocate memory ocupied by pet
 * param: p - Participant to be deatroyed
 */
void destroyParticipant(Participant* p);

/*
 * Creates a copy of a participant
 * @param p: Participant*, participant to be copied
 * @return a copy of participant p
 */
Participant* copyParticipant(Participant* p);

#endif //ENTITY_H
