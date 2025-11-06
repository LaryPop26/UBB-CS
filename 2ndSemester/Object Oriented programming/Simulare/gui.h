//
// Created by popla on 22-May-25.
//

#ifndef GUI_H
#define GUI_H
#include <qwidget.h>
#include <QListWidget>
#include <QPushButton>
#include <QLineEdit>
#include "service.h"


class Gui: public QWidget{
    Q_OBJECT
private:
    Service& service;
    QListWidget* listWidget = new QListWidget;

    QPushButton* sortNume = new QPushButton("Sortare dupa nume");
    QPushButton* sortOrganizator = new QPushButton("Sortare dupa organizator");
    QPushButton* reset = new QPushButton("Nesortat");
    QPushButton* descriere = new QPushButton("Afiseaza descriere");

    QLineEdit* codEdit = new QLineEdit;
    QLineEdit* tipEdit = new QLineEdit;

    void init();
    void connectSignals();
    void loadList(const vector<Eveniment>& listaEvenimente);

    public:
    Gui(Service& service): service(service) {
        init();
        connectSignals();
        loadList(service.getEvenimente());
    }
};



#endif //GUI_H
