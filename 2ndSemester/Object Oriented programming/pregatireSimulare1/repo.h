//
// Created by popla on 21-May-25.
//

#ifndef REPO_H
#define REPO_H
#include <algorithm>

#include "student.h"
using std::ostream;

class Repo {
    string path;
    vector<Student> students;
    void loadRepo();

    public:
    void saveRepo();
    Repo(const string &path):path(path){loadRepo();};
    void addStudent(const Student &s);
    void deleteStudent(const Student &s);
    int findStudent(int id);
    void updateStudent(int id, int i);
    vector<Student> getStudents(){return students;};

};



#endif //REPO_H
