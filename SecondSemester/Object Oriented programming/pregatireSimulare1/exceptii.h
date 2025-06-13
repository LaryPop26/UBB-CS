//
// Created by popla on 21-May-25.
//

#ifndef EXCEPTII_H
#define EXCEPTII_H
#include <string>


class Exceptii {
    std::string mesaj;
public:
    Exceptii(const std::string &mesaj):mesaj(mesaj){};
    std::string getMesaj(){return mesaj;};
};



#endif //EXCEPTII_H
