#include "GUI.h"

// Constructor for the movie list window
MovieListWindow::MovieListWindow(MovieRent& srv) : srv{srv} {
    initializeGUI();
    connectSignalsSlots();
    reloadMovieList(false, false);  // Initially load without filtering or sorting
}

void MovieListWindow::initializeGUI() {
    auto* mainLayout = new QHBoxLayout;
    setLayout(mainLayout);

    // ---------------- Left: vertical area ----------------
    auto* verticalLayout = new QVBoxLayout;
    mainLayout->addLayout(verticalLayout);  // Everything on the left (list + form + buttons + filters + undo)

    // --- Movie list ---
    movieList = new QListWidget;
    verticalLayout->addWidget(movieList);

    // --- Form for add/edit ---
    auto* formLayout = new QGridLayout;
    titleEdit = new QLineEdit(this);
    genreEdit = new QLineEdit(this);
    yearEdit = new QLineEdit(this);
    mainCharEdit = new QLineEdit(this);

    formLayout->addWidget(new QLabel("Title:"), 0, 0);
    formLayout->addWidget(titleEdit, 0, 1);
    formLayout->addWidget(new QLabel("Genre:"), 1, 0);
    formLayout->addWidget(genreEdit, 1, 1);
    formLayout->addWidget(new QLabel("Year:"), 2, 0);
    formLayout->addWidget(yearEdit, 2, 1);
    formLayout->addWidget(new QLabel("Actor:"), 3, 0);
    formLayout->addWidget(mainCharEdit, 3, 1);

    verticalLayout->addLayout(formLayout);

    // --- Main buttons ---
    auto* buttonsLayout = new QHBoxLayout;
    addButton = new QPushButton("Add Movie", this);
    deleteButton = new QPushButton("Delete Movie", this);
    updateButton = new QPushButton("Update Movie", this);
    showCartButton = new QPushButton("Show Cart", this);

    buttonsLayout->addWidget(addButton);
    buttonsLayout->addWidget(deleteButton);
    buttonsLayout->addWidget(updateButton);
    buttonsLayout->addWidget(showCartButton);

    verticalLayout->addLayout(buttonsLayout);

    // --- Filtering + sorting ---
    auto* filterSortLayout = new QHBoxLayout;
    genreFilterEdit = new QLineEdit{this};
    yearFilterEdit = new QLineEdit{this};

    QLabel* genreFilterLabel = new QLabel{"Filter by Genre:"};
    QLabel* yearFilterLabel = new QLabel{"Filter by Year:"};

    filterSortLayout->addWidget(genreFilterLabel);
    filterSortLayout->addWidget(genreFilterEdit);
    filterSortLayout->addWidget(yearFilterLabel);
    filterSortLayout->addWidget(yearFilterEdit);

    filterButton = new QPushButton("Filter Movies", this);
    filterSortLayout->addWidget(filterButton);

    sortComboBox = new QComboBox{this};
    sortComboBox->setFixedWidth(200);
    sortComboBox->setFixedHeight(40);
    sortComboBox->addItems({
        "Sort by Title Ascending", "Sort by Title Descending",
        "Sort by Main Character Ascending", "Sort by Main Character Descending",
        "Sort by Genre & Year Ascending", "Sort by Genre & Year Descending"
    });

    filterSortLayout->addWidget(sortComboBox);
    verticalLayout->addLayout(filterSortLayout);

    // --- Undo ---
    auto* controlLayout = new QHBoxLayout;
    undoButton = new QPushButton("Undo");
    controlLayout->addWidget(undoButton);
    verticalLayout->addLayout(controlLayout);

    // ---------------- Right: genre buttons ----------------
    auto* rightSideWidget = new QWidget;
    auto* rightLayout = new QVBoxLayout;
    rightSideWidget->setLayout(rightLayout);
    rightSideWidget->setFixedWidth(200);

    std::vector<std::string> genres = {"Action", "Drama","Science-Fiction"};

    for (const auto& genre : genres) {
        auto* btn = new QPushButton(QString::fromStdString("Show " + genre), this);
        rightLayout->addWidget(btn);

        QObject::connect(btn, &QPushButton::clicked, [this, genre]() {
            auto* win = new GenreWindow(srv, genre);
            win->setAttribute(Qt::WA_DeleteOnClose);
            win->setWindowTitle(QString::fromStdString("Genre: " + genre));
            win->resize(300, 400);
            win->show();
        });
    }

    mainLayout->addWidget(rightSideWidget);  // Add a right-side widget to the main horizontal layout
}

void MovieListWindow::connectSignalsSlots() {
    // When an item is clicked in the movie list, populate the form
    QObject::connect(movieList, &QListWidget::itemClicked, [this](QListWidgetItem* item) {
        string selectedMovieTitle = item->text().toStdString();
        Movie selectedMovie = srv.searchMovie(selectedMovieTitle);
        titleEdit->setText(QString::fromStdString(selectedMovie.getTitle()));
        genreEdit->setText(QString::fromStdString(selectedMovie.getGenre()));
        yearEdit->setText(QString::number(selectedMovie.getYear()));
        mainCharEdit->setText(QString::fromStdString(selectedMovie.getMainChar()));
    });

    // Connect the "add" button
    QObject::connect(addButton, &QPushButton::clicked, [this]() {
        try {
            auto title = titleEdit->text().toStdString();
            auto genre = genreEdit->text().toStdString();
            auto yearText = yearEdit->text().toStdString();
            auto mainChar = mainCharEdit->text().toStdString();

            int year = std::stoi(yearText);

            srv.addMovie(title, genre, year, mainChar);
            reloadMovieList(false, false);
        } catch (const RepoException& e) {
            QMessageBox::warning(this, "Error", QString::fromStdString(e.getMessage()));
        } catch (const ValidationError& e) {
            QMessageBox::warning(this, "Validation Error", QString::fromStdString(e.getFullMessage()));
        } catch (...) {
            QMessageBox::warning(this, "Validation Error", "Year must be a valid number.");
        }
    });

    // Connect the delete button
    QObject::connect(deleteButton, &QPushButton::clicked, [this]() {
        if (auto selectedItem = movieList->currentItem()) {
            try {
                string itemText = selectedItem->text().toStdString();
                size_t pos = itemText.find(" - ");
                string title = itemText.substr(0, pos);

                srv.deleteMovie(title);
                reloadMovieList(false, false);

                titleEdit->clear();
                genreEdit->clear();
                yearEdit->clear();
                mainCharEdit->clear();
            } catch (const RepoException& e) {
                QMessageBox::warning(this, "Error", QString::fromStdString(e.getMessage()));
            }
        }
    });

    // Connect the update button
    QObject::connect(updateButton, &QPushButton::clicked, [this]() {
        try {
            auto title = titleEdit->text().toStdString();
            auto genre = genreEdit->text().toStdString();
            auto yearText = yearEdit->text().toStdString();
            auto mainChar = mainCharEdit->text().toStdString();

            int year = std::stoi(yearText);

            srv.updateMovie(title, genre, year, mainChar);
            reloadMovieList(false, false);
        } catch (const RepoException& e) {
            QMessageBox::warning(this, "Repository Error", QString::fromStdString(e.getMessage()));
        } catch (const ValidationError& e) {
            QMessageBox::warning(this, "Validation Error", QString::fromStdString(e.getFullMessage()));
        } catch (...) {
            QMessageBox::warning(this, "Validation Error", "Year must be a valid number.");
        }
    });

    // Connect the show cart button
    QObject::connect(showCartButton, &QPushButton::clicked, this, &MovieListWindow::showCartWindow);

    // Connect the filter button
    QObject::connect(filterButton, &QPushButton::clicked, [this]() {
        reloadMovieList(true, false);  // Apply only filtering
    });

    // Connect the sort combo box
    QObject::connect(sortComboBox, &QComboBox::currentIndexChanged, [this]() {
        reloadMovieList(false, true);  // Apply only sorting
    });

    // Connect the undo button
    QObject::connect(undoButton, &QPushButton::clicked, [this]() {
        try {
            srv.undo();
            reloadMovieList();
        } catch (const RepoException& e) {
            QMessageBox::warning(this, "Error", QString::fromStdString(e.getMessage()));
        }
    });
}

void MovieListWindow::reloadMovieList(bool applyFilter, bool applySort) {
    movieList->clear();

    vector<Movie> filteredMovies = srv.getMovies();

    if (applyFilter) {
        // Apply filtering
        string genreFilter = genreFilterEdit->text().toStdString();
        int yearFilter = yearFilterEdit->text().toInt();

        if (!genreFilter.empty()) {
            filteredMovies = srv.filterGenre(genreFilter);
        }
        if (yearFilter != 0) {
            filteredMovies = srv.filterYear(yearFilter);
        }
    }

    if (applySort) {
        // Apply sorting
        int sortIndex = sortComboBox->currentIndex();
        SortType sortType = SortType::Title;
        SortOrder sortOrder = SortOrder::Ascending;

        if (sortIndex == 1) {
            sortType = SortType::Title;
            sortOrder = SortOrder::Descending;
        } else if (sortIndex == 2) {
            sortType = SortType::MainChar;
            sortOrder = SortOrder::Ascending;
        } else if (sortIndex == 3) {
            sortType = SortType::MainChar;
            sortOrder = SortOrder::Descending;
        } else if (sortIndex == 4) {
            sortType = SortType::GenreYear;
            sortOrder = SortOrder::Ascending;
        } else if (sortIndex == 5) {
            sortType = SortType::GenreYear;
            sortOrder = SortOrder::Descending;
        }

        filteredMovies = srv.sorting(sortType, sortOrder);
    }

    // Display the movies in the list
    for (const Movie& movie : filteredMovies) {
        movieList->addItem(QString::fromStdString(movie.getTitle()));
    }
}

// Cart window GUI initialization
CartWindow::CartWindow(MovieRent& srv) : srv{srv} {
    initializeGUI();
    connectSignalsSlots();
}

void CartWindow::initializeGUI() {
    auto* mainLayout = new QVBoxLayout;
    setLayout(mainLayout);

    cartTable = new QTableWidget;
    cartTable->setColumnCount(4);
    QStringList headers{"Title", "Genre", "Year", "Main Character"};
    cartTable->setHorizontalHeaderLabels(headers);
    cartTable->horizontalHeader()->setStretchLastSection(true);
    cartTable->setEditTriggers(QAbstractItemView::NoEditTriggers); // read-only
    mainLayout->addWidget(cartTable);

    auto* controlLayout = new QHBoxLayout;
    numMoviesEdit = new QLineEdit;
    generateCartButton = new QPushButton("Generate Cart");
    emptyCartButton = new QPushButton("Empty Cart");
    exportCSVButton = new QPushButton("Export to CSV");
    exportHTMLButton = new QPushButton("Export to HTML");

    controlLayout->addWidget(new QLabel("Number of movies:"));
    controlLayout->addWidget(numMoviesEdit);
    controlLayout->addWidget(generateCartButton);
    controlLayout->addWidget(emptyCartButton);
    controlLayout->addWidget(exportCSVButton);
    controlLayout->addWidget(exportHTMLButton);

    mainLayout->addLayout(controlLayout);
}

void CartWindow::connectSignalsSlots() {
    QObject::connect(generateCartButton, &QPushButton::clicked, [this]() {
        try {
            int num = std::stoi(numMoviesEdit->text().toStdString());
            srv.randomCart(num);
            reloadCartList();
        } catch (const std::exception& e) {
            QMessageBox::warning(this, "Error", e.what());
        }
    });

    QObject::connect(emptyCartButton, &QPushButton::clicked, [this]() {
        srv.deleteCart();
        reloadCartList();
    });

    // Connect CSV export button
    QObject::connect(exportCSVButton, &QPushButton::clicked, [this]() {
        try {
            vector<Movie> movies = srv.getAllCart();
            srv.exportCSV("cart.csv", movies);
            QMessageBox::information(this, "Export Success", "Cart exported to CSV!");
        } catch (const RepoException& e) {
            QMessageBox::warning(this, "Error", QString::fromStdString(e.getMessage()));
        }
    });

    // Connect HTML export button
    QObject::connect(exportHTMLButton, &QPushButton::clicked, [this]() {
        try {
            vector<Movie> movies = srv.getAllCart();
            srv.exportHTML("cart.html", movies);
            QMessageBox::information(this, "Export Success", "Cart exported to HTML!");
        } catch (const RepoException& e) {
            QMessageBox::warning(this, "Error", QString::fromStdString(e.getMessage()));
        }
    });
}

void CartWindow::reloadCartList() {
    cartTable->clearContents();
    const auto& cartMovies = srv.getAllCart();
    cartTable->setRowCount(static_cast<int>(cartMovies.size()));

    for (std::size_t row = 0; row < cartMovies.size(); ++row) {
        const auto& m = cartMovies[row];
        cartTable->setItem(row, 0, new QTableWidgetItem(QString::fromStdString(m.getTitle())));
        cartTable->setItem(row, 1, new QTableWidgetItem(QString::fromStdString(m.getGenre())));
        cartTable->setItem(row, 2, new QTableWidgetItem(QString::number(m.getYear())));
        cartTable->setItem(row, 3, new QTableWidgetItem(QString::fromStdString(m.getMainChar())));
    }
}
