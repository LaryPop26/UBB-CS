//
// Created by popla on 29-Mar-25.
//

#include "movie.h"

#include <utility>

auto Movie::getTitle() const -> string {
    return this->title;
}

auto Movie::getGenre() const -> string {
    return this->genre;
}

auto Movie::getYear() const -> int {
    return this->year;
}

auto Movie::getMainChar() const -> string {
    return this->mainChar;
}

/*void Movie::setTitle(string newTitle) {
    this->title = newTitle;
}*/

void Movie::setGenre(string newGenre) {
    this->genre = std::move(newGenre);
}

void Movie::setYear(int newYear) {
    this->year = newYear;
}

void Movie::setMainChar(string newMainChar) {
    this->mainChar = std::move(newMainChar);
}