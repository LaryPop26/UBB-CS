//
// Created by popla on 21-May-25.
//

#include "repo.h"

#include <algorithm>
#include <fstream>

void Repo::loadRepo() {
    std::ifstream fin(path);
    Student s;
    while (fin>>s) {
        students.push_back(s);
    }
    fin.close();
}
void Repo::saveRepo() {
    std::ofstream fout(path);
    for (const auto &s: students) fout << s<<'\n';
    fout.close();
}

int Repo::findStudent(int id) {
    auto it=find_if(students.begin(), students.end(), [id](const Student &s)
        {return s.getNrMatricol()==id;});
    if (it == students.end()) return -1;
    return (int) std::distance(students.begin(), it);
}

void Repo::addStudent(const Student &s) {
    students.push_back(s);
    saveRepo();
}

void Repo::deleteStudent(const Student &s) {
    students.erase(students.begin() + findStudent(s.getNrMatricol()));
    saveRepo();
}

void Repo::updateStudent(int id, int i) {
    Student s = students[findStudent(id)];
    Student newS=Student(s.getNrMatricol(),s.getNume(),i,s.getFacultate());
    students[findStudent(id)]=newS;
    saveRepo();
}
