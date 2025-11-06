//
// Created by popla on 22-May-25.
//

#include "service.h"
#include <algorithm>

vector<Eveniment> Service::sortByNume() const {
    auto all = repo.getEvenimente();
    sort(all.begin(), all.end(), [](const Eveniment& e1, const Eveniment& e2) {
        return e1.getNume() < e2.getNume();
    });
    return all;}

vector<Eveniment> Service::sortByOrganizator() const {
    auto all = repo.getEvenimente();
    sort(all.begin(), all.end(), [](const Eveniment& e1, const Eveniment& e2) {
        return e1.getOrganizator() < e2.getOrganizator();
    });
    return all;}