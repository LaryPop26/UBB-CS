//
// Created by popla on 31-Mar-25.
//

#include "validator.h"
constexpr int min_year = 1800;
void Validator::validate(const Movie& movie) {
    vector<string> errorMessage;
    if (movie.getTitle().empty()) { errorMessage.emplace_back("Title is empty");
}
    if (movie.getGenre().empty()) { errorMessage.emplace_back("Genre is empty");
}
    if (movie.getYear()<min_year) { errorMessage.emplace_back("Year is not correct");
}
    if (movie.getMainChar().empty()) { errorMessage.emplace_back("MainChar is empty");
}
    if (!errorMessage.empty()) {
        throw ValidationError(errorMessage);
    }
}

auto operator<<(ostream& out, const ValidationError& exceptie) -> ostream& {
    for (const auto& message : exceptie.errorValidation) {
        out << message;
    }
    return out;
}