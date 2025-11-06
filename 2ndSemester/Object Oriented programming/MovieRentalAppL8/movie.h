//
// Created by popla on 29-Mar-25.
//

#ifndef MOVIE_H
#define MOVIE_H
#include <string>
using std::string;
class Movie {
private:
    string title;
    string genre;
    int year;
    string mainChar;

public:
    Movie()= default;
    Movie(const string &title,const string &genre,const int year,const string &mainChar)/*
    {
        this->title = title;
        this->genre = genre;
        this->year = year;
        this->mainChar = mainChar;
    }*/
    :title{title}, genre{genre}, year{year}, mainChar{mainChar} {};
    Movie(const Movie &ot) : title(ot.title), genre(ot.genre), year(ot.year), mainChar(ot.mainChar) {};

    bool operator == (const Movie &m) const {
        return this->getTitle() == m.getTitle() /*&& this->getGenre() == m.getGenre()*/;
    }

    Movie& operator=(const Movie& ot) {
        if (this != &ot) {
            title = ot.title;
            genre = ot.genre;
            year = ot.year;
            mainChar = ot.mainChar;
        }
        return *this;
    }

    [[nodiscard]] string getTitle() const;
    [[nodiscard]] string getGenre() const;
    [[nodiscard]] int getYear() const;
    [[nodiscard]] string getMainChar() const;

    void setGenre(string newGenre);
    void setYear(int year);
    void setMainChar(string mainChar);
};

#endif //MOVIE_H
