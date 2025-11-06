//
// Created by popla on 29-Mar-25.
//

#ifndef REPOSITORY_H
#define REPOSITORY_H

#include "movie.h"

#include <fstream>
#include <ostream>
#include <utility>
#include <vector>

using std::vector;
using std::ostream;
using std::string;

class RepoException {
    private:
        string errorMessage;
    public:
        explicit RepoException(string message): errorMessage{std::move(message)} {};
        auto getMessage() -> string {
            return this->errorMessage;
        }
        friend auto operator<<(std::ostream& out, const RepoException& repo_exception) -> ostream&;
};

class MovieRepository {
    private:
        vector<Movie> movies;

        /**
         * Verify if a movie is in the list
         * @param movie_to_search_for :Movie(),searched entity
         * @return true/false
         */
        auto isin(const Movie& movie_to_search_for) -> bool;
    public:

        // constructor
        MovieRepository()=default;

        MovieRepository(const MovieRepository& other)=delete;

        /**
         * Add a movie in the movie list
         * @param movie
         * throws an exception if there is already a movie with the same name
         */
        virtual void addMovie(const Movie& movie);

        /**
         * Delete a movie using its position
         * @param position: position in the list
         */
        virtual void deleteMovie(int position);

        /**
         * Update a movie
         * @param movie : movie to be updated
         */
        virtual void updateMovie(const Movie& movie);

        /**
         * Get all movies
         * @return a vector with all movies
         */
        [[nodiscard]] virtual auto getMovies() const -> const vector<Movie>&;

        /**
         * Find an entity after title
         * @param title : string, str to search for
         * @return : movie, if found, exception otherwise
         */
        [[nodiscard]] virtual auto findPosition(const string & title) const -> int;


        /**
         * Search a movie into the list
         * @param title : string , movie title
         * @return movie:Movie, info for searched title
         */
        virtual auto searchMovie(const string &title) -> const Movie &;

        virtual ~MovieRepository();
};

auto operator<<(ostream& out, const RepoException& repo_exception) -> ostream&;

class RepoFile: public MovieRepository {
    private:
        void read_from_file();
        void write_to_file();
        string file_name;
        void clear_file() {
            std::ofstream fin(file_name, std::ios::trunc);
            fin.close();
        }

public:
    RepoFile(string file_name): MovieRepository (), file_name{std::move(file_name)} {
        read_from_file();
    };

    void addMovie(const Movie& movie) override {
        MovieRepository::addMovie(movie);
        write_to_file();
    }

    void deleteMovie(int position) override {
        MovieRepository::deleteMovie(position);
        write_to_file();
    }

    void updateMovie(const Movie& movie) override {
            MovieRepository::updateMovie(movie);
            write_to_file();
        }

    ~RepoFile() override {};
};

#endif //REPOSITORY_H
