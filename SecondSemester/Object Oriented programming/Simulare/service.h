//
// Created by popla on 22-May-25.
//

#ifndef SERVICE_H
#define SERVICE_H
#include "repo.h"


class Service {
private:
    Repo& repo;

public:
    // constructor
    Service(Repo& repo) : repo(repo) {};

    // returneaza lista de evenimente
    // return: vector de evenimente
    vector<Eveniment> getEvenimente() { return repo.getEvenimente(); }

    // sorteaza lista de evenimente dupa nume
    // return: vector de evenimente sortat
    vector<Eveniment> sortByNume() const;

    // sorteaza lista de evenimente dupa organizator
    // return: vector de evenimente sortat
    vector<Eveniment> sortByOrganizator() const;
};




#endif //SERVICE_H
