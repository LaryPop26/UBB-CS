#include <QApplication>
#include <QPushButton>
#include "service.h"
#include "tests.h"
#include "GUI.h"

int main(int argc, char *argv[]) {
    testing();

    RepoFile repo("movies.txt");
    Validator validator;
    ShoppingCart shoppingCart;
    MovieRent srv(repo, validator, shoppingCart);

    QApplication a(argc, argv);

    // Creăm fereastra principală
    MovieListWindow* mainWindow = new MovieListWindow{srv};
    mainWindow->show();

    // Creăm fereastra pentru coș
    CartWindow* cartWindow = new CartWindow{srv};

    // Conectăm semnalul pentru afișarea ferestrei coșului
    QObject::connect(mainWindow, &MovieListWindow::showCartWindow,
                     [cartWindow]() { cartWindow->show(); });

    return QApplication::exec();
}
