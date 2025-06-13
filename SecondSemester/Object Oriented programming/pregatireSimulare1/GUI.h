//
// Created by popla on 21-May-25.
//

#ifndef GUI_H
#define GUI_H
#include "service.h"
#include <QTableView>
#include <QPushButton>

#include "MyTable.h"

class GUI:public QWidget {

    QTableView *table = new QTableView;
    MyTable *myTable;

    QPushButton *intinerire = new QPushButton("intinerire");
    QPushButton *imbatranire = new QPushButton("imbatranire");
    QPushButton *sterge = new QPushButton("sterge");
    QPushButton *undoButton = new QPushButton("Undo");
    QPushButton *redoButton = new QPushButton("Redo");

    Service &srv;

    void init();
    void connectButton();
    void loadTable();

    public:
        GUI(Service &s):srv(s) {
            init();
            connectButton();
            loadTable();
        };

};



#endif //GUI_H
