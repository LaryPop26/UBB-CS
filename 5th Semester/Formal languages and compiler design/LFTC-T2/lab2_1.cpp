#include <iostream>
#include <fstream>
#include <string>
#include <set>
#include <map>

using namespace std;

class AutomatFinit {
private:
    set<string> stari;
    set<char> alfabet;
    string stareInitiala;
    set<string> stariFinale;


    map<pair<string, char>, set<string>> tranzitii;

public:
    void clear() {
        stari.clear();
        alfabet.clear();
        stareInitiala.clear();
        stariFinale.clear();
        tranzitii.clear();
    }

    void citesteDinFisier(const string& numeFisier) {
        clear();
        ifstream fin(numeFisier);
        if (!fin.is_open()) {
            cerr << "Eroare: nu pot deschide fisierul " << numeFisier << "\n";
            return;
        }

        int n, m, f, t;
        fin >> n;
        for (int i = 0; i < n; i++) {
            string s; fin >> s;
            stari.insert(s);
        }

        fin >> m;
        for (int i = 0; i < m; i++) {
            char c; fin >> c;
            alfabet.insert(c);
        }

        fin >> stareInitiala;

        fin >> f;
        for (int i = 0; i < f; i++) {
            string sf; fin >> sf;
            stariFinale.insert(sf);
        }

        fin >> t;
        for (int i = 0; i < t; i++) {
            string din, spre; char c;
            fin >> din >> c >> spre;
            tranzitii[{din, c}].insert(spre);
        }

        fin.close();
    }

    void citesteDeLaTastatura() {
        clear();
        int n, m, f, t;
        cout << "Numar stari: "; cin >> n;
        cout << "Stari: ";
        for (int i = 0; i < n; i++) {
            string s; cin >> s;
            stari.insert(s);
        }

        cout << "Numar simboluri alfabet: "; cin >> m;
        cout << "Simboluri: ";
        for (int i = 0; i < m; i++) {
            char c; cin >> c;
            alfabet.insert(c);
        }

        cout << "Stare initiala: "; cin >> stareInitiala;

        cout << "Numar stari finale: "; cin >> f;
        cout << "Stari finale: ";
        for (int i = 0; i < f; i++) {
            string sf; cin >> sf;
            stariFinale.insert(sf);
        }

        cout << "Numar tranzitii: "; cin >> t;
        cout << "Tranzitii (forma: stare1 simbol stare2):\n";
        for (int i = 0; i < t; i++) {
            string din, spre; char c;
            cin >> din >> c >> spre;
            tranzitii[{din, c}].insert(spre);
        }
    }

    void afiseazaElemente() {
        cout << "Stari: ";
        for (auto& s : stari) cout << s << " ";
        cout << "\nAlfabet: ";
        for (auto& c : alfabet) cout << c << " ";
        cout << "\nStare initiala: " << stareInitiala;
        cout << "\nStari finale: ";
        for (auto& s : stariFinale) cout << s << " ";
        cout << "\nTranzitii:\n";
        for (auto& tr : tranzitii) {
            cout << "(" << tr.first.first << "," << tr.first.second << ") -> ";
            for (auto& spre : tr.second) cout << spre << " ";
            cout << "\n";
        }
    }

    // === Verificare daca este determinist ===
    bool esteDeterminist() {
        for (auto& tr : tranzitii) {
            if (tr.second.size() > 1) return false;
        }
        return true;
    }

    // === Verificare acceptare secventa ===
    bool esteAcceptata(const string& secventa) {
        if (!esteDeterminist()) {
            cerr << "Eroare: automatul nu este determinist!\n";
            return false;
        }

        string stareCurenta = stareInitiala;
        for (char c : secventa) {
            auto it = tranzitii.find({stareCurenta, c});
            if (it == tranzitii.end()) return false;
            stareCurenta = *(it->second.begin()); // are doar o singura stare
        }
        return stariFinale.find(stareCurenta) != stariFinale.end();
    }

    // === Prefix maxim acceptat ===
    string prefixMaxim(const string& secventa) {
        if (!esteDeterminist()) {
            cerr << "Eroare: automatul nu este determinist!\n";
            return "";
        }

        string stareCurenta = stareInitiala;
        string prefix, maxim;
        if (stariFinale.count(stareCurenta)) maxim = "";
        for (char c : secventa) {
            auto it = tranzitii.find({stareCurenta, c});
            if (it == tranzitii.end()) break;
            stareCurenta = *(it->second.begin());
            prefix.push_back(c);
            if (stariFinale.count(stareCurenta)) maxim = prefix;
        }
        return maxim;
    }
};

int main() {
    AutomatFinit af;
    int opt;
    do {
        cout << "\n=== MENIU ===\n";
        cout << "1. Citeste automat din fisier\n";
        cout << "2. Citeste automat de la tastatura\n";
        cout << "3. Afiseaza elementele automatului\n";
        cout << "4. Verifica daca o secventa este acceptata (doar pentru AFD)\n";
        cout << "5. Determina prefix maxim acceptat (doar pentru AFD)\n";
        cout << "0. Iesire\n";
        cout << "Optiune: ";
        cin >> opt;
        cin.ignore();

        if (opt == 1) {
            string nume;
            cout << "Nume fisier: ";
            cin >> nume;
            af.citesteDinFisier(nume);
        }
        else if (opt == 2) {
            af.citesteDeLaTastatura();
        }
        else if (opt == 3) {
            af.afiseazaElemente();
        }
        else if (opt == 4) {
            string secventa;
            cout << "Introdu secventa (Enter pentru ε, sau scrie 'eps'): ";
            getline(cin, secventa);
            if (secventa == "eps" || secventa == "ε") secventa.clear();
            cout << (af.esteAcceptata(secventa) ? "Acceptata\n" : "Respinsa\n");
        }
        else if (opt == 5) {
            string secventa;
            cout << "Introdu secventa: ";
            getline(cin, secventa);
            if (secventa == "eps" || secventa == "ε") secventa.clear();
            cout << "Prefix maxim acceptat: " << af.prefixMaxim(secventa) << "\n";
        }
    } while (opt != 0);

    return 0;
}
