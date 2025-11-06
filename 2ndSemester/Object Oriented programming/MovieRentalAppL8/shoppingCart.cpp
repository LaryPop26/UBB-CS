//
// Created by popla on 16-Apr-25.
//

#include "shoppingCart.h"
#include <algorithm>
#include <random>

ShoppingCart::ShoppingCart() = default;

void ShoppingCart::addToCart(const Movie &movie) {
    this->shoppingCart.push_back(movie);
}

void ShoppingCart::deleteCart() {
    this->shoppingCart.clear();
}

void ShoppingCart::randomCart(size_t dim, vector<Movie> movies) {
    vector<Movie> moviesAux;
    std::shuffle(movies.begin(),movies.end(), std::default_random_engine(std::random_device{}()));
    while ((this->shoppingCart.size() < dim) && (!movies.empty())) {
        this->shoppingCart.push_back(movies.back());
        moviesAux.push_back(movies.back());
        movies.pop_back();
        if (movies.empty() && shoppingCart.size() < dim) {
            movies = moviesAux;
            moviesAux.clear();
            std::shuffle(movies.begin(),movies.end(), std::default_random_engine(std::random_device{}()));
        }
    }
}

auto ShoppingCart::getallShoppingCart() -> const vector<Movie> & {
    return this->shoppingCart;
}

ShoppingCart::~ShoppingCart() = default;