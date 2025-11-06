#include <iostream>

using namespace std;

int cerc() {
    struct circle {
        float r;};
    struct circle cerc;
    float pi = 3.14;

    cout<< " Introdu raza: ";
    cin >> cerc.r;

    cout << "Perimetru = ";
    cout << 2 * pi * cerc.r;
    cout << endl;
    cout << "Arie: ";
    cout << pi * cerc.r * cerc.r;
    cout << endl;
    return 0;
}

int cmmdc() {
    int a;
    int b;
    int r;
    cout<< " Introdu numerele: ";
    cin >> a;
    cin >> b;
    while(b != 0) {
        r = a % b;
        a = b;
        b = r;
    }
    cout << "Cmmdc: ";
    cout << a;
    cout << endl;
    return 0;
}

int suma() {
    int n;
    int x;
    cout<< " Introdu nr de numere: ";
    cin >> n;
    int s = 0;
    for(int i = 1; i <= n; i++) {
        cout<< " Introdu un numar: ";
        cin >> x;
        s = s + x;
    }
    cout <<"Suma este: ";
    cout << s;
    cout << endl;
    return 0;
}

int main() {
    cerc();
    cmmdc();
    suma();

    return 0;
}

// eroare in MLP si in limbaj
int err1() {
    int a // lipseste operatorul de final ;
    int int; // cuvant cheie folosit ca identificator
    cout<< " Introdu numarul: ";
    cin >> a;
    cout << "Suma e" << (a+ int)<< endl;
}

// eroare in MLP dar nu si in limbaj
int err2() {
    int a,b; // in MLP declararea se face pe linii separate
    int val[5]; // in MLP nu sunt definiti vectorii
    cout << "Introdu 2 numere: ";
    cin >> val[0] >> val[1]; // in MLP nu se permite citirea pt mai multe var
    cout << "Suma e" << (val[0] + val[1]) << endl; // in MLP afisarea se face cu cate o instr pe linie
    return 0;
}