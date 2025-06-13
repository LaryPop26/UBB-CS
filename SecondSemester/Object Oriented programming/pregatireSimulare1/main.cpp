#include <QApplication>
#include "GUI.h"
#include "repo.h"
#include "service.h"

int main(int argc, char *argv[]) {
    QApplication a(argc, argv);

    Repo repo{"../studenti.txt"};
    Service service(repo);
    GUI gui(service);
    gui.show();

    return QApplication::exec();
}
