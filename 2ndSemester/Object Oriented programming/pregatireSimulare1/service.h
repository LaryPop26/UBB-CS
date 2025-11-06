//
// Created by popla on 21-May-25.
//

#ifndef SERVICE_H
#define SERVICE_H
#include <memory>
#include "repo.h"
#include "undo.h"

using std::unique_ptr;
class Service {
    Repo& repo;
    vector<unique_ptr<Undo>> to_undo;
    vector<unique_ptr<Redo>> to_redo;
    public:
    Service(Repo &repo):repo(repo){};
    Service(Service& s)=delete;
    void stergeMultipla(const vector<Student> &students);
    void updateAll(int i);
    void undo();
    void redo();

    vector<Student> getStudents();
};



#endif //SERVICE_H
