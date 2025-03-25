//
// Created by popla on 12-Mar-25.
//

#include "validation.h"
#include <string.h>


int validate_entity(Participant* p) {
    if (strlen(p->lastName)== 0)
        return 0;
    if (strlen(p->firstName)== 0)
        return 0;
    if (p->score < 0 || p->score > 100)
        return 0;
    return 1;
}

int validate_int(int poz) {
    if (poz < 0) return 0;
    return 1;
}
