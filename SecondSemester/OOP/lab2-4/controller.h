//
// Created by popla on 11-Mar-25.
//

#ifndef CONTROLLER_H
#define CONTROLLER_H
#include "MyList.h"

/*
 * Add a participant
 * params: participants - MyList, current list
 *         lastName - char, name of a person
 *         firstName - char, name of a person
 *         score - int, score of the participant
 * return: 0..3 - succes of process
 */
int addParticipantController(MyList* participants, char* lastName, char* firstName, int score);

/*
 * Update a participant score
 * params: participants - MyList, current list
 *         lastName - char, name of a person
 *         firstName - char, name of a person
 *         score - int, score of the participant
 * return: 0..3 - succes of process
 */
int updateParticipantController(MyList* participants, char* lastName, char* firstName, int score);

/*
 * Delete a participant
 * params: participants - MyList, current list
 *         poz - int, position to be cleared
 * return: 0..1 - succes of process
 */
int deleteParticipantController(MyList* participants, int poz);

/*
 * Creates a new list with all participant having score less than given value
 * param: participants - MyList, current list
 *        score - int, score to be compared with
 * return: MyList, a list with valid data for given condition
 */
MyList filterScore(MyList* participants, int score);

/*
 * Creates a new list with all participant having the first letter of lastname the given one
 * param: participants - MyList, current list
 *        firstLetter - char, compared letter
 * return: MyList, a list with valid data for given condition
 */
MyList filterFirstLetter(MyList* participants, char* firstLetter);

/*
 *
 */
MyList sortNamesAscending(MyList* participants);

/*
 *
 */
MyList sortNamesDescending(MyList* participants);

/*
 *
 */
MyList sortScoreAscending(MyList* participants);

/*
 *
 */
MyList sortScoreDescending(MyList* participants);

#endif //CONTROLLER_H
