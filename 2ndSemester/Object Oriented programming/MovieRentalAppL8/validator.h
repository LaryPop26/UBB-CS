//
// Created by popla on 31-Mar-25.
//

#ifndef VALIDATOR_H
#define VALIDATOR_H
#include <string>
#include <utility>
#include <vector>
#include "movie.h"
using std::string;
using std::vector;
using std::ostream;

class ValidationError {
    vector<string> errorValidation;
public:
    ValidationError(vector<string> message) :errorValidation{std::move(message)} {}
    friend auto operator<<(ostream& out, const ValidationError& exceptie) -> ostream&;

    auto getMessage() -> vector<string> { return errorValidation; }
};

auto operator<<(ostream& out, const ValidationError& exceptie) -> ostream&;

class Validator {
public:
  static void validate(const Movie &movie) ;
};

#endif //VALIDATOR_H
