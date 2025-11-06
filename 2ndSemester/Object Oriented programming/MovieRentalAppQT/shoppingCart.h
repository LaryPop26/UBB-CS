//
// Created by popla on 16-Apr-25.
//

#ifndef SHOPPINGCART_H
#define SHOPPINGCART_H
#include <vector>
#include "observer.h"
#include "movie.h"
using std::vector;

class ShoppingCart : public Observable {
private:
  vector<Movie> shoppingCart{};

public:
  ShoppingCart();

  void addToCart(const Movie &movie);

  void deleteCart();

  void randomCart(size_t dim, vector<Movie> movies);

  const vector<Movie> &getallShoppingCart();

  ~ShoppingCart();
};

#endif //SHOPPINGCART_H
