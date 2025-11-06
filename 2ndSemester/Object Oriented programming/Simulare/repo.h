//
// Created by popla on 22-May-25.
//

#ifndef REPO_H
#define REPO_H
#include <vector>

#include "domain.h"

using std::vector;

class Repo {
private:
    vector<Eveniment> evenimente;

public:
    // constructor
    Repo(const std::string& filename) {
        loadFromFile(filename);
    }

    Repo() = default;

    // incarca datele din fisier
    // @param fileName: numele fisierului de intrare
    void loadFromFile(const string& fileName);

    // lista de evenimente
    const vector<Eveniment>& getEvenimente() const { return evenimente; }
};



#endif //REPO_H
