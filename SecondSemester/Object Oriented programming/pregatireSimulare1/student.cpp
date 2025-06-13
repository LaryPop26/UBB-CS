//
// Created by popla on 21-May-25.
//

#include "student.h"
vector<string> splitLine(const string &line, char del) {
    vector<string> objs;
    string item;
    stringstream stream(line);
    while(getline(stream, item, del)) {
        objs.push_back(item);
    }
    return objs;
}

string Student::print(char del) const {
    return std::to_string(nrmatricol) + del + nume + del + std::to_string(varsta) + del + facultate;
}

std::istream &operator>>(std::istream &is, Student &s) {
    string line;
    getline(is, line);
    if (line=="") return is;
    vector<string> objs = splitLine(line, ',');
    s.nrmatricol = std::stoi(objs[0]);
    s.nume = objs[1];
    s.varsta = std::stoi(objs[2]);
    s.facultate = objs[3];
    return is;
}

std::ostream &operator<<(std::ostream &os, const Student &s) {
    os << s.print(',');
    return os;
}

bool cmpVarsta(const Student &s1, const Student &s2) {
    return s1.getVarsta() < s2.getVarsta();
}