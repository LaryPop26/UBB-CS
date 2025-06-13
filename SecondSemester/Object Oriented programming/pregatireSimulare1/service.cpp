//
// Created by popla on 21-May-25.
//

#include "service.h"

#include <algorithm>

#include "exceptii.h"

void Service::stergeMultipla(const vector<Student> &students) {
    for (const auto &s: students) {
        to_undo.push_back(std::make_unique<UndoStergere>(s,repo));
        repo.deleteStudent(s);
    };
    repo.saveRepo();
}

void Service::updateAll(int i) {
    for (auto &s: repo.getStudents()) {
        to_undo.push_back(std::make_unique<UndoModifica>(s,-i,repo));
        if (s.getVarsta()+i<0) throw Exceptii("Varsta nu poate fi negativa");
        int varsta=s.getVarsta()+i;
        repo.updateStudent(s.getNrMatricol(),varsta);
    };
}

void Service::undo() {
    if (to_undo.empty()) throw Exceptii("Nu se mai poate face undo");
    string type=to_undo.back()->typeUndo();
    auto st=to_undo.back()->getStudent();

    if (type=="Stergere") {
        to_redo.push_back(std::make_unique<RedoStergere>(st,repo));
    }
    if (type=="Modificare") {
        int i=0;
        while (i<repo.getStudents().size()) {
            to_redo.push_back(std::make_unique<RedoModifica>(st.getNrMatricol(),st.getVarsta(),repo));
            i++;
        }
    }
    to_undo.back()->doUndo();
    to_undo.pop_back();
}

void Service::redo() {
    if (to_redo.empty()) throw Exceptii("Nu se mai poate face redo");
    to_redo.back()->doRedo();
    to_redo.pop_back();
}

vector<Student> Service::getStudents() {
    auto sorted=repo.getStudents();
    sort(sorted.begin(),sorted.end(),cmpVarsta);
    return sorted;
}