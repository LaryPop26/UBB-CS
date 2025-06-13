//
// Created by popla on 21-May-25.
//

#ifndef MYTABLE_H
#define MYTABLE_H
#include <qabstractitemmodel.h>
#include <qcolor.h>
#include <qvariant.h>
#include <string>

#include "student.h"


class MyTable:public QAbstractTableModel{
    vector<Student> students;
public:
    MyTable(const vector<Student> &students):students(students){};
    void setStudents(const vector<Student> &studs) {
        students=studs;
        QModelIndex topLeft = createIndex(0, 0);
        QModelIndex bottomRight = createIndex(rowCount(),columnCount());
        emit dataChanged(topLeft, bottomRight);
        emit layoutChanged();
    };
    Student getStudents(QModelIndex& index) {return students[index.row()];};
    int rowCount(const QModelIndex& index=QModelIndex()) const override {return students.size();};
    int columnCount(const QModelIndex& index=QModelIndex()) const override {return 4;};
    QVariant data(const QModelIndex &index, int role) const override {
        if (role==Qt::DisplayRole||role==Qt::BackgroundRole) {
            auto student=students[index.row()];
            string fac=student.getFacultate();
            QColor color;
            if (fac=="info") color=Qt::green;
            if (fac=="mate") color=Qt::blue;
            if (fac=="ai") color=Qt::red;
            if (fac=="mate-info") color=Qt::yellow;

            if (index.column()==0) {
                if (role==Qt::BackgroundRole) return color;
                return QString::fromStdString(to_string(student.getNrMatricol()));
            };

            if (index.column()==1) {
                if (role==Qt::BackgroundRole) return color;
                return QString::fromStdString(student.getNume());
            }

            if (index.column()==2) {
                if (role==Qt::BackgroundRole) return color;
                return QString::fromStdString(to_string(student.getVarsta()));
            }

            if (index.column()==3) {
                if (role==Qt::BackgroundRole) return color;
                return QString::fromStdString(student.getFacultate());
            }
        }
        return QVariant();
    }

};



#endif //MYTABLE_H
