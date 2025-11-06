//
// Created by popla on 21-May-25.
//

#ifndef STUDENT_H
#define STUDENT_H
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
using std::string;
using std::vector;
using std::to_string;
using std::stringstream;
class Student {
private:
    int nrmatricol;
    string nume;
    int varsta;
    string facultate;

public:
    Student():nrmatricol(0),nume(""),varsta(0),facultate(""){};
    Student(int nr, const string &nume, int varsta, const string &facultate):nrmatricol(nr),nume(nume),varsta(varsta),facultate(facultate){};
    Student(const Student &s):nrmatricol(s.nrmatricol),nume(s.nume),varsta(s.varsta),facultate(s.facultate){};

    Student &operator=(const Student &s)=default;

    int getNrMatricol() const{return nrmatricol;};
    string getNume() const{return nume;};
    int getVarsta() const{return varsta;};
    string getFacultate() const{return facultate;};

    void setNrMatricol(int nr){nrmatricol=nr;};
    void setNume(const string &nume){this->nume=nume;};
    void setVarsta(int varsta){this->varsta=varsta;};
    void setFacultate(const string &facultate){this->facultate=facultate;};

    string print(char del) const;
    friend std::istream &operator>>(std::istream &is, Student &s);
    friend std::ostream &operator<<(std::ostream &os, const Student &s);
};

vector<string> splitLine(const string &line, char del);
bool cmpVarsta(const Student &s1, const Student &s2);

#endif //STUDENT_H
