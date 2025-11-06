#include "repository.h"
#include "service.h"
#include "UI.h"

void startApp() {
    //MovieRepository repo;
    RepoFile repo("movies.txt");
    Validator validator;
    ShoppingCart shoppingCart;
    MovieRent srv{repo, validator, shoppingCart};
    UI user_interface{srv};
    user_interface.run();}

auto main() -> int {
    startApp();
    return 0;}
