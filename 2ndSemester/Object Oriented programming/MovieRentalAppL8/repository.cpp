//
// Created by popla on 29-Mar-25.
//
#include "repository.h"
#include <algorithm>  // pentru copy_if, find_if, any_of
#include <iterator>   // pentru back_inserter
#include <ostream>

auto MovieRepository::isin(const Movie& movie_to_search_for) -> bool {
    return std::any_of(movies.begin(), movies.end(), [&](const Movie& movie) {
        return movie.getTitle() == movie_to_search_for.getTitle();
    });
}

void MovieRepository::addMovie(const Movie& movieToAdd) {
    if (isin(movieToAdd)) {
        throw RepoException("Movie is already in the list");
    }
    movies.push_back(movieToAdd);
}

void MovieRepository::deleteMovie(int position) {
    if (position < 0 || position >= static_cast<int>(movies.size())) {
        throw RepoException("Invalid position");
    }
    movies.erase(movies.begin() + position);
}

void MovieRepository::updateMovie(const Movie& movieToUpdate) {
    if (!isin(movieToUpdate)) {
        throw RepoException("Movie isn't in the list");
    }
    for (auto& movie : movies) {
        if (movie.getTitle() == movieToUpdate.getTitle()) {
            movie.setGenre(movieToUpdate.getGenre());
            movie.setYear(movieToUpdate.getYear());
            movie.setMainChar(movieToUpdate.getMainChar());
        }
    }
}

auto MovieRepository::getMovies() const -> const vector<Movie>& {
    return this->movies;
}

auto MovieRepository::findPosition(const string& title) const -> int {
    auto iter = std::find_if(movies.begin(), movies.end(), [&](const Movie& movie) {
        return movie.getTitle() == title;
    });

    if (iter == movies.end()) {
        throw RepoException("Movie position not found");
    }

    return static_cast<int>(std::distance(movies.begin(), iter));
}

auto MovieRepository::searchMovie(const string &title) -> const Movie & {
  auto iter =
      std::find_if(movies.begin(), movies.end(), [&](const Movie &movie) {
        return movie.getTitle() == title;
      });

  if (iter == movies.end()) {
    throw RepoException("Movie not found");
  }

  return *iter;
}
MovieRepository::~MovieRepository() = default;

auto operator<<(ostream &out, const RepoException &repo_exception)
    -> ostream & {
  for (const auto &message : repo_exception.errorMessage) {
    out << message;
  }
  return out;
}


void RepoFile::read_from_file() {
    std::ifstream fin(file_name);
    /*if (!fin.is_open()) {
        throw RepoException("File not found");
    }*/
    while (true) {
        string title;
        std::getline(fin>>std::ws, title);
        if (fin.fail()) {break;}
        string genre;
        std::getline(fin>>std::ws, genre);
        int year=0;
        fin>>year;
        string mainChar;
        std::getline(fin>>std::ws, mainChar);

        Movie movie{ title, genre, year, mainChar};
        MovieRepository::addMovie(movie);
    }
    fin.close();
}

void RepoFile::write_to_file() {
    std::ofstream fout(file_name);
    if (!fout.is_open()) {throw RepoException("File couldn't be found: " + file_name);}
    for (const auto &movie : MovieRepository::getMovies()) {
        fout<<movie.getTitle()<<"\n";
        fout<<movie.getGenre()<<"\n";
        fout<<movie.getYear()<<"\n";
        fout<<movie.getMainChar()<<"\n";
    }
    fout.close();
}




