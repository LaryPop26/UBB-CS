//
// Created by popla on 29-Mar-25.
//

#include "UI.h"
#include <iostream>
#include "tests.h"

using std::cout;
using std::endl;
using std::cin;

constexpr int OptionClose = 0;
constexpr int OptionAddMovie = 1;
constexpr int OptionDeleteMovie = 2;
constexpr int OptionUpdateMovie = 3;
constexpr int OptionSearchMovie = 4;
constexpr int OptionFilterMovie = 5;
constexpr int OptionSortMovie = 6;
constexpr int OptionShowMovies = 7;
constexpr int OptionAddToCart = 8;
constexpr int OptionDeleteCart = 9;
constexpr int OptionEmptyCart = 10;
constexpr int OptionRandomCart = 11;
constexpr int OptionExportCart = 12;
constexpr int OptionShowCart = 13;
constexpr int OptionUndo = 14;

void UI::printMenu() {
    cout << "Movie Rental App" << '\n';
    cout << "1. Add movie" << '\n';
    cout << "2. Delete movie" << '\n';
    cout << "3. Update movie" << '\n';
    cout << "4. Search movie" << '\n';
    cout << "5. Filter" << '\n';
    cout << "6. Sort" << '\n';
    cout << "7. Print all movies" << '\n';
    cout << "8. Add to cart" << '\n';
    cout << "9. Delete cart" << '\n';
    cout << "10. Empty cart" << '\n';
    cout << "11. Random cart" << '\n';
    cout << "12. Export cart" << '\n';
    cout << "13. Show cart" << '\n';
    cout<< "14. Undo" << '\n';
    cout << "0. Exit" << '\n';
}

void UI::printAllMovies(const std::vector<Movie> &movies) {
  if (movies.empty()) {
    cout << "Currently, there are no movies in the list." << '\n';
  } else {
    for (const auto &movie : movies) {
      cout << "Title: " << movie.getTitle() << " | Genre: " << movie.getGenre()
           << " | Year: " << movie.getYear()
           << " | Main Character: " << movie.getMainChar() << '\n';
    }
    }
}

void UI::addUI() const{
    string title;
    string genre;
    string mainChar;
    int year=0;
    cin.ignore();
    cout << "Enter title: ";
    getline(cin, title);
    cout << "Enter genre: ";
    getline(cin, genre);
    cout << "Enter year: ";
    cin >> year;
    cin.ignore();
    cout << "Enter main character: ";
    getline(cin, mainChar);
    srv.addMovie(title, genre, year, mainChar);
}

void UI::deleteUI() const{
    string title;
    cout << "Enter the title of the movie to delete: ";
    getline(std::cin>>std::ws, title);

    srv.deleteMovie(title);
    cout << "Movie deleted successfully." << '\n';
}

void UI::updateUI() const{
    int year = 0;
    string title;
    string genre;
    string mainChar;
    cin.ignore();
    cout << "Enter title: ";
    getline(cin, title);
    cout << "Enter new genre: ";
    getline(cin, genre);
    cout << "Enter new year: ";
    cin >> year;
    cin.ignore();
    cout << "Enter new main character: ";
    getline(cin, mainChar);

    srv.updateMovie(title, genre, year, mainChar);
    cout<< "Movie updated successfully." << '\n';
}

void UI::searchUI() const {
    string title;
    cout << "Enter title: ";
    cin.ignore();
    getline(cin, title);
    const Movie movie = srv.searchMovie(title);
    cout << "Movie:  " << '\n' << "Title: " << movie.getTitle() << " | Genre: " << movie.getGenre() << " | Year: " << movie.getYear()
            << " | Main Character: " << movie.getMainChar() << '\n';;
}

void UI::filterUI() const {
    int type = 0;
    cin.ignore();
    cout << "Enter type of filter: 1 - genre, 2 - year: ";
    cin >> type;
    if (type == 1) {
        string genre;
        cout << "Enter genre: ";
        cin.ignore();
        getline(cin, genre);

        printAllMovies(srv.filterGenre(genre));
    }
    else if (type == 2) {
        int year = 0;
        cout << "Enter year: ";
        cin >> year;

        printAllMovies(srv.filterYear(year));
    }
    else {
        cout << "Invalid input." << '\n';
    }
}
void UI::sortUI() const {
    int type = 0;
    int order = 0;

    // Alegerea tipului de sortare
    cout << "Enter type of sort:\n";
    cout << "1. Title\n";
    cout << "2. Main Character\n";
    cout << "3. Genre + Year\n";
    cout << "Choose an option: ";
    cin >> type;

    // Verificăm dacă inputul pentru tipul de sortare este valid
    if (type < 1 || type > 3) {
        cout << "Invalid input for type." << '\n';
        return;
    }

    // Alegerea ordinii
    cout << "Enter order:\n";
    cout << "1. Ascending\n";
    cout << "2. Descending\n";
    cout << "Choose an option: ";
    cin >> order;

    // Verificăm dacă inputul pentru ordine este valid
    if (order < 1 || order > 2) {
        cout << "Invalid input for order." << '\n';
        return;
    }

    // Folosim enum-urile pentru a selecta tipul de sortare și ordinea
    const auto enumType = static_cast<SortType>(type);
    const auto enumOrder = static_cast<SortOrder>(order);

    // Apelăm funcția de sortare
    const vector<Movie> movies = srv.sorting(enumType, enumOrder);

    // Afișăm rezultatele
    printAllMovies(movies);
}

void UI::addToCartUI() const {
    string title;
    cin.ignore();
    cout << "Enter movie title to be added in cart: ";
    getline(cin, title);
    printAllMovies(srv.addToCart(title));
}

/*void UI::deleteFromCartUI() {
    string title;
    cin.ignore();
    cout << "Enter movie title to be deleted from cart: ";
    printAllMovies(srv.deleteFromCart(title));
}*/

void UI::randomCartUI() const {
    int dim = 0;
    cin.ignore();
    cout << "Enter number of random movies: ";
    cin >> dim;
    printAllMovies(srv.randomCart(dim));
}

void UI::exportUI() const {
    string fileName;
    string type;
    cin.ignore();
    cout << "Enter file type (csv/html): ";
    getline(cin, type);
    cout << "Enter file name: ";
    getline(cin, fileName);
    const vector<Movie>& movies = srv.getAllCart();
    if (type == "csv") {
        MovieRent::exportCSV(fileName, movies);
    }
    else if (type == "html") {
        MovieRent::exportHTML(fileName, movies);
    }
    else {
        cout << "Invalid input." << '\n';
    }
}

void UI::undoUI() const {
    srv.undo();
    printAllMovies(srv.getMovies());
}

void UI::run() const{
    testing();
    bool running = true ;
    int cmd = 0;
    while (running) {
        printMenu();
        cout << "Choose an option: "<< '\n';
        cin >> cmd;
        try {
            switch (cmd) {
                case OptionAddMovie:
                    addUI();
                    break;
                case OptionDeleteMovie:
                    deleteUI();
                    break;
                case OptionUpdateMovie:
                    updateUI();
                    break;
                case OptionSearchMovie:
                    searchUI();
                    break;
                case OptionFilterMovie:
                    filterUI();
                    break;
                case OptionSortMovie:
                    sortUI();
                    break;
                case OptionShowMovies:
                    printAllMovies(srv.getMovies());
                    break;
                case OptionAddToCart:
                    addToCartUI();
                    break;
                case OptionDeleteCart:
                    /*deleteFromCartUI();*/
                    break;
                case OptionEmptyCart:
                    printAllMovies(srv.deleteCart());
                    break;
                case OptionRandomCart:
                    randomCartUI();
                    break;
                case OptionExportCart:
                    exportUI();
                    break;
                case OptionShowCart:
                    printAllMovies(srv.getAllCart());
                    break;
                case OptionUndo:
                    undoUI();
                    break;
                case OptionClose:
                    running = false;
                break;
                default:
                    cout << "Invalid option." << '\n';
                break;
            }
        }
        catch (RepoException& re) {
            cout << re << '\n';
        }
        catch (ValidationError& ve) {
            cout << ve << "\n";
        }
    }
}
