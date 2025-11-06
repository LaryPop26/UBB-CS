#include <QApplication>
#include "gui.h"
#include "teste.h"

int main(int argc, char *argv[]) {

    testAll();

    QApplication a(argc, argv);
    Repo repo("../evenimente.txt");
    Service service(repo);
    Gui gui(service);
    gui.show();
    return QApplication::exec();
}
