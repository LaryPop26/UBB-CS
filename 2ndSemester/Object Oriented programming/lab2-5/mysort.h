//
// Created by popla on 13-Mar-25.
//

#ifndef MYSORT_H
#define MYSORT_H
#include "MyList.h"

/*
 * Type of comparing function for 2 elements
 * return: 0 if equals, 1 if p1>p2, -1 otherwise
 */
typedef int(*CmpFct)(void* el1, void* el2);

/*
 * Sorting in place
 * cmp - relation for comparing
 */
void sort(MyList* lst, CmpFct cmp);
#endif //MYSORT_H
