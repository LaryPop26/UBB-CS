//
// Created by popla on 21-May-25.
//

#include "GUI.h"

#include "exceptii.h"
#include "QHBoxLayout"
#include "QMessageBox"

void GUI::init() {
    QHBoxLayout *main = new QHBoxLayout;
    setLayout(main);
    myTable = new MyTable(srv.getStudents());
    table->setSelectionBehavior(QAbstractItemView::SelectRows);
    table->setModel(myTable);
    main->addWidget(table);

    QVBoxLayout* dr = new QVBoxLayout;
    main->addLayout(dr);
    dr->addWidget(imbatranire);
    dr->addWidget(intinerire);
    dr->addWidget(sterge);
    dr->addWidget(undoButton);
    dr->addWidget(redoButton);

    resize(1000,800);
}

void GUI::connectButton() {
    QObject::connect(sterge, &QPushButton::clicked, [&]() {
        auto sel=table->selectionModel()->selectedRows();
        if (sel.size()==0) QMessageBox::warning(this,"Atentie","Nu a fost selectat nici un student");
        else {
            vector<Student> deSters;
            for (auto i:sel) {
                QModelIndex &index=i;
                auto s=myTable->getStudents(i);
                std::cout << s.getFacultate();
                deSters.push_back(s);
            }
            srv.stergeMultipla(deSters);
            loadTable();
        }
    });

    QObject::connect(intinerire, &QPushButton::clicked, [&]() {
        srv.updateAll(-1);
        loadTable();
    });

    QObject::connect(imbatranire, &QPushButton::clicked, [&]() {
        srv.updateAll(1);
        loadTable();
    });

    QObject::connect(undoButton, &QPushButton::clicked, [&]() {
        try {
            srv.undo();
        }
        catch (Exceptii &e) {
            QMessageBox::warning(this,"Atentie",QString::fromStdString(e.getMesaj()));
        }
        loadTable();
    });

    QObject::connect(redoButton, &QPushButton::clicked, [&]() {
      try {
          srv.redo();
      }
      catch (Exceptii &e) {
          QMessageBox::warning(this,"Atentie",QString::fromStdString(e.getMesaj()));
      }
      loadTable();
  });
}

void GUI::loadTable() {
    myTable->setStudents(srv.getStudents());
}