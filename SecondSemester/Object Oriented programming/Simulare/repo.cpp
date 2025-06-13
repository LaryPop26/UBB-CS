//
// Created by popla on 22-May-25.
//

#include "repo.h"

#include <fstream>
#include <sstream>
using std::stringstream;
void Repo::loadFromFile(const std::string &fileName) {
    std::ifstream file(fileName);
    std::string line;
    while (std::getline(file,line)) {
        stringstream ss(line);
        string cod, nume, tip, organizator, descriere;
        getline(ss, cod, ';');
        getline(ss, nume, ';');
        getline(ss, tip, ';');
        getline(ss, organizator, ';');
        getline(ss, descriere, ';');
        evenimente.emplace_back(cod, nume, tip, organizator, descriere);
    }
}
