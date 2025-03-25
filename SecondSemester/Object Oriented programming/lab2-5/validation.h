//
// Created by popla on 12-Mar-25.
//

#ifndef VALIDATION_H
#define VALIDATION_H
#include "entity.h"

/*
 * Verify if a participant data is valid to be saved
 * param: participant- Participant entity
 * return: bool, True if it is a valid entity, false otherwise
 */
int validate_entity(Participant* participant);

/*
 * Verify if a number is positive
 * param: poz- number to be checked
 * return: bool, True if it is a valid entity, false otherwise
 */
int validate_int(int poz);

#endif //VALIDATION_H
