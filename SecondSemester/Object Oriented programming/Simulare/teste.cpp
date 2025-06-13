//
// Created by popla on 22-May-25.
//

#include "teste.h"
#include "service.h"
#include <iostream>
#include <cassert>


void test_domain() {
    Eveniment ev1("E01","Concert Simfonic","concert","Opera Nationala","Muzica");

    assert(ev1.getCod()== "E01");
    assert(ev1.getNume()== "Concert Simfonic");
    assert(ev1.getTip()== "concert");
    assert(ev1.getOrganizator()== "Opera Nationala");
    assert(ev1.getDescriere()== "Muzica");
}

void test_repo() {
    Repo repo("../test_evenimente.txt");
    assert(repo.getEvenimente().size() == 5);
}

void test_service() {
    Repo repo("../test_evenimente.txt");
    Service service(repo);
    assert(service.getEvenimente().size() == 5);

    auto  sortNume = service.sortByNume();
    assert( sortNume[0].getNume() == "Ateliere de creatie");
    assert( sortNume[1].getNume() == "Concert Simfonic");
    assert( sortNume[2].getNume() == "Dansuri traditionale");
    assert( sortNume[3].getNume() == "Expozitie foto Clujul vechi");
    assert( sortNume[4].getNume() == "Proiectie de film romanesc");

    auto sortOrganizator = service.sortByOrganizator();
    assert(sortOrganizator[0].getOrganizator() == "Ansamblul Folcloric Somesul");
    assert(sortOrganizator[1].getOrganizator() == "Asociatia Educatie");
    assert(sortOrganizator[2].getOrganizator() == "Cinema Arta");
    assert(sortOrganizator[3].getOrganizator() == "Muzeul de Istorie");
    assert(sortOrganizator[4].getOrganizator() == "Opera Nationala Romana");
}

void testAll() {
    test_domain();
    test_repo();
    test_service();
    std::cout << "Teste trecute!";
}
