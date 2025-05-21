#include <QApplication>
#include <QPushButton>

#include "CosCRUDGUI.h"
#include "CosReadOnlyGUI.h"
#include "service.h"
#include "tests.h"
#include "MovieGUI.h"
int main(int argc, char *argv[]) {
    testing();

    RepoFile repo("movies.txt");
    Validator validator;
    ShoppingCart shoppingCart;
    MovieRent srv(repo, validator, shoppingCart);

    QApplication a(argc, argv);

    FilmGUI mainWindow{srv, shoppingCart};
    CosCRUDGUI cosCrudWindow{srv, shoppingCart};
    CosReadOnlyGUI cosReadOnlyWindow{shoppingCart};

    mainWindow.show();
    cosCrudWindow.show();
    cosReadOnlyWindow.show();

    return QApplication::exec();
}

