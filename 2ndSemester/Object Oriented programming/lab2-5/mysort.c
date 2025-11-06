//
// Created by popla on 13-Mar-25.
//

#include "mysort.h"
void sort(MyList* lst, CmpFct cmp) {
    for (int i = 0; i < size(lst); i++) {
        for (int j = i + 1; j < size(lst); j++) {
            void* el1 = getMyElement(lst, i);
            void* el2 = getMyElement(lst, j);
            if (cmp(el1, el2) > 0) {
                setMyElement(lst, i, el2);
                setMyElement(lst, j, el1);
            }
        }
    }
}