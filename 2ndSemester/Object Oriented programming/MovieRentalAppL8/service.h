//
// Created by popla on 29-Mar-25.
//

#ifndef SERVICE_H
#define SERVICE_H
#include "repository.h"
#include "shoppingCart.h"
#include "undo.h"
#include "validator.h"

#include <cstdint>
#include <memory>

using std::vector;

enum class SortType : std::uint8_t { Title = 1, MainChar, GenreYear };
enum class SortOrder : std::uint8_t { Ascending = 1, Descending };

class MovieRent {
    private:
        MovieRepository& repo;
        Validator& validator;
        ShoppingCart& shoppingCart;
        vector<std::unique_ptr<UndoAction>> UndoActions;

    public:
        MovieRent(MovieRepository& repo, Validator& validator, ShoppingCart& shoppingCart) noexcept:
            repo(repo), validator(validator) , shoppingCart(shoppingCart){};

        MovieRent(const MovieRent& other);
    
        /**
         * Add a movie into the list
         * @param title : string, movie title
         * @param genre : string, movie genre
         * @param year : int, movie year
         * @param mainChar : string, movie main character
         */
        void addMovie(const string &title, const string &genre, int year, const string &mainChar);
    
        /**
         * Delete a movie from list
         * @param title : string, movie title to be deleted
         */
        void deleteMovie(const string &title);

        /**
         * Update movie information
         * @param title : string, movie title
         * @param genre  : string, updated movie title
         * @param year  : int, updated movie year
         * @param mainChar : string, updated movie main Char
         */
        void updateMovie (const string &title, const string &genre, int year, const string &mainChar);

        /**
         * Search a movie into the list
         * @param title : string , movie title
         * @return movie:Movie, info for searched title
         */
        [[nodiscard]] auto searchMovie(const string &title) const -> Movie;

        /**
         * Filter the list after genre criteria
         * @param genre: genre to be searched
         * @return all Movies with genre - genre
         */
        [[nodiscard]] auto filterGenre(const string &genre) const -> vector<Movie>;

        /*vector<Movie> filterTitle(const string &title);*/

        /**
         * Filter the list after year criteria
         * @param year: year to be searched
         * @return all Movies with year - year
         */
        [[nodiscard]] auto filterYear(int year) const -> vector<Movie>;

        /**
         * Sort the list after a type ascending/descending
         * @param type : criteria to sort by
         * @param order : sort order - ascending or descending
         * @return sorted list
         */
        [[nodiscard]] auto sorting(SortType type, SortOrder order) const -> vector<Movie>;

        /**
         * Get all movies
         * @return list, all movies
         */
        [[nodiscard]] auto getMovies() const -> const std::vector<Movie>&;

        [[nodiscard]] auto addToCart(const string & title) const -> vector<Movie>;

        [[nodiscard]] auto deleteCart() const -> vector<Movie>;

        [[nodiscard]] auto randomCart(int dim) const -> vector<Movie>;

        [[nodiscard]] auto getAllCart() const -> vector<Movie>;

        static void exportCSV(const string& fileName, const vector<Movie>& movies);

        static void exportHTML(const string& fileName, const vector<Movie> &movies);

        void notify() const { this->shoppingCart.notify();}

        void undo();

};

#endif //SERVICE_H
