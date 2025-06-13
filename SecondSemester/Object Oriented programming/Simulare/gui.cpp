//
// Created by popla on 22-May-25.
//
#include <QVBoxLayout>
#include <QMessageBox>
#include <QLabel>
#include "gui.h"

#include <list>
#include <list>
#include <list>
#include <list>

void Gui::init() {
    QVBoxLayout* layout = new QVBoxLayout;

    layout->addWidget(listWidget);
    layout->addWidget(new QLabel("Cod: "));
    layout->addWidget(codEdit);
    layout->addWidget(new QLabel("Tip: "));
    layout->addWidget(tipEdit);

    layout->addWidget(sortNume);
    layout->addWidget(sortOrganizator);
    layout->addWidget(reset);
    layout->addWidget(descriere);

    setLayout(layout);
}

void Gui::connectSignals() {

    QObject::connect(listWidget, &QListWidget::itemClicked, [this](QListWidgetItem* item) {
        int index = listWidget->currentRow();
        if (index < 0 || index >= service.getEvenimente().size()) return;
        auto ev = service.getEvenimente()[index];
        codEdit->setText(QString::fromStdString(ev.getCod()));
        tipEdit->setText(QString::fromStdString(ev.getTip()));
    });

    QObject::connect(sortNume, &QPushButton::clicked, [this]() {
        loadList(service.sortByNume());
    });

    QObject::connect(sortOrganizator, &QPushButton::clicked, [this]() {
        loadList(service.sortByOrganizator());
    });

    QObject::connect(reset, &QPushButton::clicked, [this]() {
        loadList(service.getEvenimente());
    });

    QObject::connect(descriere, &QPushButton::clicked, [this]() {
        int index = listWidget->currentRow();
        if (index < 0 || index >= service.getEvenimente().size()) return;
        auto ev = service.getEvenimente()[index];
        QMessageBox::information(this, "Descriere", QString::fromStdString(ev.getDescriere()));
    });
}

void Gui::loadList(const vector<Eveniment>& listaEvenimente) {
    listWidget->clear();
    for (auto& e: listaEvenimente) {
        listWidget->addItem(QString::fromStdString(e.getNume() + " - " + e.getOrganizator()));
    }
}
