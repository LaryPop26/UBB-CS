#pragma once
#include <QMainWindow>
#include <QListWidget>
#include <QTableWidget>
#include <QLineEdit>
#include <QPushButton>
#include <QVBoxLayout>
#include <QHBoxLayout>
#include <QLabel>
#include <QMessageBox>
#include <QGridLayout>
#include <QComboBox>  // Adăugat pentru combobox-ul de sortare
#include "service.h"
#include <QHeaderView>

class MovieListWindow : public QWidget {
    Q_OBJECT
private:
    MovieRent& srv;
    QListWidget* movieList{};
    QLineEdit* titleEdit{};
    QLineEdit* genreEdit{};
    QLineEdit* yearEdit{};
    QLineEdit* mainCharEdit{};
    QPushButton* addButton{};
    QPushButton* deleteButton{};
    QPushButton* updateButton{};
    QPushButton* showCartButton{};

    // Elemente pentru filtrare
    QLineEdit* genreFilterEdit{};
    QLineEdit* yearFilterEdit{};
    QPushButton* filterButton{};

    // ComboBox pentru sortare
    QComboBox* sortComboBox{};

    QPushButton* undoButton{};

    void initializeGUI();
    void connectSignalsSlots();
    void reloadMovieList(bool applyFilter = false, bool applySort = false);

public:
    explicit MovieListWindow(MovieRent& srv);

    signals:
        void showCartWindow();
};

class CartWindow : public QWidget {
    Q_OBJECT
private:
    MovieRent& srv;
    QTableWidget* cartTable;
    QPushButton* emptyCartButton;
    QPushButton* generateCartButton;
    QLineEdit* numMoviesEdit;
    QPushButton* exportCSVButton;
    QPushButton* exportHTMLButton;

    void initializeGUI();
    void connectSignalsSlots();
    void reloadCartList();

public:
    explicit CartWindow(MovieRent& srv);
};



class GenreWindow : public QWidget {
    Q_OBJECT
private:
    MovieRent& srv;
    QListWidget* list;
    QLabel* countLabel;
    std::string genre;

public:
    GenreWindow(MovieRent& srv, const std::string& genre) : srv{srv}, genre{genre} {
        auto* layout = new QVBoxLayout;
        list = new QListWidget;
        countLabel = new QLabel;

        layout->addWidget(new QLabel(QString::fromStdString("Movies of genre: " + genre)));
        layout->addWidget(list);
        layout->addWidget(countLabel);
        setLayout(layout);

        reload();
    }

    void reload() {
        list->clear();
        auto filtered = srv.filterGenre(genre);
        for (const auto& m : filtered) {
            list->addItem(QString::fromStdString(m.getTitle()));
        }
        countLabel->setText("Count: " + QString::number(filtered.size()));
    }
};
