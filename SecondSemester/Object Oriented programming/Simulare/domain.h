//
// Created by popla on 22-May-25.
//

#ifndef DOMAIN_H
#define DOMAIN_H
#include <string>

using std::string;

class Eveniment {
private:
    string cod;
    string nume;
    string tip;
    string organizator;
    string descriere;
public:
    // constructor
    Eveniment(const std::string& c, const std::string& n, const std::string& t, const std::string& o, const std::string& d)
            : cod(c), nume(n), tip(t), organizator(o), descriere(d) {}

    // getters
    string getCod() const { return cod; }
    string getNume() const { return nume; }
    string getTip() const { return tip; }
    string getOrganizator() const { return organizator; }
    string getDescriere() const { return descriere; }
};



#endif //DOMAIN_H
