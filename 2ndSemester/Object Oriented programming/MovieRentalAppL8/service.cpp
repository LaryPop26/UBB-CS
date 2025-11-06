//
// Created by popla on 29-Mar-25.
//

#include "service.h"
#include <algorithm>
#include <fstream>

#include <ios>
#include <map>

void MovieRent::addMovie(const string& title,const string& genre,const int year,const string& mainChar) {
    const Movie movie{title, genre, year, mainChar};
    Validator::validate(movie);
    repo.addMovie(movie);
    UndoActions.push_back(std::make_unique<AddUndo>(movie, this->repo));
}

void MovieRent::deleteMovie(const string& title) {
    const int position = repo.findPosition(title);
    Movie movie = repo.searchMovie(title);
    repo.deleteMovie(position);
    UndoActions.push_back(std::make_unique<DeleteUndo>(movie, this->repo));
}

void MovieRent::updateMovie (const string& title,const string& genre, const int year,const string& mainChar) {
    const Movie movie{title, genre, year, mainChar};
    Validator::validate(movie);
    Movie oldMovie = repo.searchMovie(title);
    repo.updateMovie(movie);
    UndoActions.push_back(std::make_unique<UpdateUndo>(oldMovie, this->repo));
}

auto MovieRent::searchMovie(const string &title) const -> Movie{
    return repo.searchMovie(title);
}

auto MovieRent::filterGenre(const string &genre) const -> vector<Movie> {
    const vector<Movie> movies = repo.getMovies();
    vector<Movie> filtered;

    std::copy_if(movies.begin(), movies.end(), std::back_inserter(filtered),
                 [&genre](const Movie& movie) {
                     return movie.getGenre() == genre;
                 });

    return filtered;
}

auto MovieRent::filterYear(const int year) const -> vector<Movie> {
    const vector<Movie>& movies = repo.getMovies();
    std::map<int, vector<Movie>> yearToMovies;

    for (const auto& movie : movies) {
        yearToMovies[movie.getYear()].push_back(movie);
    }

    // Dacă anul nu există în map, returnează vector gol
    if (yearToMovies.find(year) == yearToMovies.end()) {
        return {};
    }

    return yearToMovies[year];
}

auto cmpTitleAscending(const Movie &movie1, const Movie &movie2) -> bool {
    return movie1.getTitle() < movie2.getTitle();
}

auto cmpTitleDescending(const Movie &movie1, const Movie &movie2) -> bool {
    return movie1.getTitle() > movie2.getTitle();
}

auto cmpMainCharAscending(const Movie &movie1, const Movie &movie2) -> bool {
    return movie1.getMainChar() < movie2.getMainChar();
}

auto cmpMainCharDescending(const Movie &movie1, const Movie &movie2) -> bool {
    return movie1.getMainChar() > movie2.getMainChar();
}

auto cmpGenreYearAscending(const Movie &movie1, const Movie &movie2) -> bool {
    if (movie1.getYear() == movie2.getYear()) {
        return movie1.getGenre() < movie2.getGenre();
}
    return movie1.getYear() < movie2.getYear();
}

auto cmpGenreYearDescending(const Movie &movie1, const Movie &movie2) -> bool {
    if (movie1.getYear() == movie2.getYear()) {
        return movie1.getGenre() > movie2.getGenre();
}
    return movie1.getYear() > movie2.getYear();
}

auto MovieRent::sorting(SortType type, SortOrder order) const -> vector<Movie> {
    vector<Movie> movies = repo.getMovies();
    bool (*cmp)(const Movie &, const Movie &) = nullptr;

    if (type == SortType::Title) {
        cmp = (order == SortOrder::Ascending) ? cmpTitleAscending : cmpTitleDescending;
    } else if (type == SortType::MainChar) {
        cmp = (order == SortOrder::Ascending) ? cmpMainCharAscending : cmpMainCharDescending;
    } else if (type == SortType::GenreYear) {
        cmp = (order == SortOrder::Ascending) ? cmpGenreYearAscending : cmpGenreYearDescending;
    }

    if (cmp == nullptr) {
        throw RepoException("Invalid sort type or order");
    }

    std::sort(movies.begin(), movies.end(), cmp);
    return movies;
}

auto MovieRent::getMovies() const -> const vector<Movie> & {
    return repo.getMovies();
}

auto MovieRent::addToCart(const string & title) const -> vector<Movie> {

    const vector<Movie> movies = getAllCart();
    const Movie& searchedMovie = this->repo.searchMovie(title);
    for (const auto &movie : movies) {
        if (movie.getTitle() == title) {
            throw RepoException("Movie already exists");
        }
    }
    this ->shoppingCart.addToCart(searchedMovie);
    return getAllCart();
}

auto MovieRent::deleteCart() const -> vector<Movie> {
    this->shoppingCart.deleteCart();
    return getAllCart();
}

auto MovieRent::randomCart(const int dim) const -> vector<Movie> {
    this->shoppingCart.randomCart(dim, getMovies());
    return getAllCart();
}

auto MovieRent::getAllCart() const -> vector<Movie> {
    return this->shoppingCart.getallShoppingCart();
}

void MovieRent::exportCSV(const string& fileName, const vector<Movie>& movies) {
    std::ofstream fout(fileName, std::ios::trunc);
    if (!fout.is_open()) { throw RepoException("Error opening file"); }
    for (const auto &movie : movies) {
        fout << movie.getTitle() <<","<<movie.getGenre() << ","<< movie.getYear() << ","<< movie.getMainChar() << "\n";
    }
    fout.close();
}

void MovieRent::exportHTML(const string &fileName,
                           const vector<Movie> &movies) {
  std::ofstream fout(fileName);
  if (!fout.is_open()) { throw RepoException("Error opening file"); }
  fout << "<html><body>\n";
  fout << "<table border=\"1\" style=\"width:100 % \">\n";
  for (const auto &movie : movies) {
    fout << "<tr>\n"
         << "<td>" << movie.getTitle() << "</td>\n"
         << "<td>" << movie.getGenre() << "</td>\n"
         << "<td>" << movie.getYear() << "</td>\n"
         << "<td>" << movie.getMainChar() << "</td>\n"
         << "</tr>\n";
  }
  fout << "</table>\n";
  fout << "</body></html>\n";
  fout.close();
}
void MovieRent::undo() {
    if (UndoActions.empty()) { throw RepoException("Cannot undo anymore"); }
    UndoActions.back()->doUndo();
    UndoActions.pop_back();
}


