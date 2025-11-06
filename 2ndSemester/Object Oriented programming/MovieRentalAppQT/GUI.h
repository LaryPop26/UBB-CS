#pragma once
#include <QListWidget>
#include <QTableWidget>
#include <QLineEdit>
#include <QPushButton>
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
    QPushButton* addToCartButton{};

    QPushButton* openCrudCartButton{};
    QPushButton* openReadOnlyCartButton{};

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
