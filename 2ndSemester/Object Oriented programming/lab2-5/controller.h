//
// Created by popla on 11-Mar-25.
//

#ifndef CONTROLLER_H
#define CONTROLLER_H
#include "MyList.h"

typedef struct {
    MyList* lstParticipants;
    MyList* undoLst;
}ManagerParticipants;

/*
 * Creates a manager for contest participants
 * return: created ManagerParticipants
 */
ManagerParticipants createManagerParticipants();

/*
 * Destroy everything about the partipants manager
 * param: manager - ManagerParticipants, manager for participants
 */
void destroyManagerParticipants(ManagerParticipants* contest);

/*
 * Add a participant
 * params: manager - ManagerParticipants, manager for participants
 *         lastName - char, name of a person
 *         firstName - char, name of a person
 *         score - int, score of the participant
 * return: 0..3 - succes of process
 */
int addParticipant(ManagerParticipants* contest, char* lastName, char* firstName, int score);

/*
 * Search for a participant in the list
 * params: lastName, firstName - str, name of participant
 * return: participant position if fount, -1 otherwise
 */
int findElem(ManagerParticipants* lst, char* lastName, char* firstName);

/*
 * Update a participant score
 * params: manager - ManagerParticipants, manager for participants
 *         lastName - char, name of a person
 *         firstName - char, name of a person
 *         score - int, score of the participant
 * return: 0..3 - succes of process
 */
int updateParticipant(ManagerParticipants* contest, char* lastName, char* firstName, int score);

/*
 * Delete a participant
 * params: manager - ManagerParticipants, manager for participants
 *         poz - int, position to be cleared
 * return: 0..1 - succes of process
 */
int deleteParticipant(ManagerParticipants* contest, char* lastName, char* firstName);

/*
 * Creates a new list with all participant having score less than given value
 * param: manager - ManagerParticipants, manager for participants
 *        score - int, score to be compared with
 * return: MyList, a list with valid data for given condition
 */
MyList* filterScore(ManagerParticipants* contest, int maxScore);

/*
 * Creates a new list with all participant having the first letter of lastname the given one
 * param: manager - ManagerParticipants, manager for participants
 *        firstLetter - char, compared letter
 * return: MyList, a list with valid data for given condition
 */
MyList* filterFirstLetter(ManagerParticipants* contest, char* firstLetter);

/*
 * Sort a list of participants after lastname
 * param: manager - ManagerParticipants, manager for participants
 * return: a sorted list
 */
MyList* sortByName(ManagerParticipants* contest);

/*
 * Sort a list of participants after score
 * param: manager - ManagerParticipants, manager for participants
 * return: a sorted list
 */
MyList* sortByScore(ManagerParticipants* contest);

/*
 *
 */
int undo(ManagerParticipants* contest);

#endif //CONTROLLER_H
