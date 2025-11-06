//
// Created by popla on 29-Mar-25.
//

#ifndef UI_H
#define UI_H
#include "service.h"
class UI {
private:
    MovieRent& srv;

    void addUI() const;

    void deleteUI() const;

    void updateUI() const;

    void searchUI() const;

    void filterUI() const;

    void sortUI() const;

    static void printAllMovies(const vector<Movie>& movies);

    void addToCartUI() const;

    /*void deleteFromCartUI();*/

    void randomCartUI() const;

    void exportUI() const;
    void undoUI() const;

  public:
  explicit UI(MovieRent& srv):srv{srv} {};
  UI(const UI& other) = delete;

  ~UI()=default;

  static void printMenu();

  void run() const;
};

#endif //UI_H
