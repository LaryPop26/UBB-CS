//
// Created by popla on 21-May-25.
//

#ifndef UNDO_H
#define UNDO_H
#include "student.h"
#include "repo.h"

class Undo {
public:
        virtual void doUndo()=0;
        virtual int getId()=0;
        virtual int getVal()=0;
        virtual string typeUndo()=0;
        virtual Student getStudent()=0;
        virtual ~Undo()=default;
};
class UndoModifica:public Undo {
        Student studentModificat;
        int i;
        Repo& repo;
        public:
        UndoModifica(const Student &s, int is, Repo &repo):studentModificat(s),i(is),repo(repo){};
        void doUndo() override{repo.updateStudent(studentModificat.getNrMatricol(),studentModificat.getVarsta());};
        int getId() override{return studentModificat.getNrMatricol();};
        int getVal() override{return i;};
        string typeUndo() override{return "Modificare";};
        Student getStudent() override{return studentModificat;};

};
class UndoStergere:public Undo {
        Student studentSters;
        Repo& repo;
        public:
        UndoStergere(const Student &s, Repo &repo):studentSters(s),repo(repo){};
        void doUndo() override{repo.addStudent(studentSters);};
        int getId() override{return studentSters.getNrMatricol();};
        int getVal() override{return studentSters.getVarsta();};
        string typeUndo() override{return "Stergere";};
        Student getStudent() override{return studentSters;};
};

class Redo {
public:
        virtual void doRedo()=0;
        virtual ~Redo()=default;
};

class RedoModifica:public Redo {
        int id=0;
        int i=0;
        Repo& repo;
public:
        RedoModifica(int id,int is, Repo &repo):id(id),i(is),repo(repo){};
        void doRedo() override{repo.updateStudent(id,i);};
};
class RedoStergere:public Redo {
        Student studentSters;
        Repo& repo;
        public:
        RedoStergere(const Student &s, Repo &repo):studentSters(s),repo(repo){};
        void doRedo() override{repo.deleteStudent(studentSters);};
};
#endif //UNDO_H
