//
// Created by popla on 20-May-25.
//

#ifndef COSCRUDGUI_H
#define COSCRUDGUI_H
#pragma once
#include "service.h"
#include "observer.h"
#include <QtWidgets/qlabel.h>
#include <QtWidgets/qwidget.h>
#include <QtWidgets/qpushbutton.h>
#include <QtWidgets/qboxlayout.h>
#include <QtWidgets/qlineedit.h>
#include <QtWidgets/qformlayout.h>
#include <QtWidgets/qlistwidget.h>
#include <QtWidgets/qmessagebox.h>
#include <qtablewidget.h>
#include <qdebug.h>
#include <QFormLayout>
#include <qfont.h>
#include <QTextEdit>
#include <vector>
#include <string>

class CosCRUDGUI : public QWidget, public Observer {
public:
    CosCRUDGUI(MovieRent& service, ShoppingCart& cos) : service { service }, cos { cos } {
        initGUI();
        loadData();
        initConnect();
    }

    void update() override {
        loadData();
    }

private:
    MovieRent& service;
    ShoppingCart& cos;
    vector<Movie> filme;

    QListWidget* listaInchirieri = new QListWidget{};
    QLineEdit* numarAdaugareRandomInCosEdit = new QLineEdit;
    QPushButton* butonGolireCos = new QPushButton{ "&Golește cosul" };
    QPushButton* butonAdaugareRandomInCos = new QPushButton{ "&Adaugă random în cos" };

    void initGUI() {
        auto layoutPrincipalCos = new QVBoxLayout{};
        auto layoutButoaneCosInchirieri = new QHBoxLayout{};
        auto casetaAdaugareRandom = new QFormLayout;

        QLabel* textCosInchirieri = new QLabel("Coș de închirieri");

        casetaAdaugareRandom->addRow(numarAdaugareRandomInCosEdit);
        numarAdaugareRandomInCosEdit->setPlaceholderText("Introduceți un număr de filme");
        numarAdaugareRandomInCosEdit->setFixedWidth(185);

        layoutButoaneCosInchirieri->addWidget(butonAdaugareRandomInCos);
        layoutButoaneCosInchirieri->addWidget(butonGolireCos);

        setLayout(layoutPrincipalCos);

        layoutPrincipalCos->addWidget(textCosInchirieri);
        layoutPrincipalCos->addWidget(listaInchirieri);
        layoutPrincipalCos->addLayout(layoutButoaneCosInchirieri);
        layoutPrincipalCos->addLayout(casetaAdaugareRandom);
    }

    void loadData() {
        listaInchirieri->clear();
        for (const auto& film : cos.getallShoppingCart()) {
            QString item = QString::fromStdString(film.getTitle() + ", " + film.getGenre() + ", " +
                std::to_string(film.getYear()) + ", " + film.getMainChar());
            listaInchirieri->addItem(item);
        }
        filme.clear();
    }

    void initConnect() {
        cos.addObserver(this);
        QObject::connect(butonGolireCos, &QPushButton::clicked, [&]() {
            service.deleteCart();
            loadData();
            });

        QObject::connect(butonAdaugareRandomInCos, &QPushButton::clicked, [&]() {
            filme = service.getMovies();
            if (numarAdaugareRandomInCosEdit->text().toStdString() == "")
                QMessageBox::information(this, "Atenție!", "Introduceți un număr de filme pentru închiriat!");

            int numarDeFilmeIntroduse = filme.size();
            if (numarAdaugareRandomInCosEdit->text().toInt() <= numarDeFilmeIntroduse)
                cos.randomCart(numarAdaugareRandomInCosEdit->text().toInt(), filme);
            else
                QMessageBox::warning(this, "Atenție!", "Nu există suficiente filme introduse!");
            loadData();
            });
    }
public:
    ~CosCRUDGUI() {
        cos.deleteObserver(this);
    }

};
#endif //COSCRUDGUI_H
