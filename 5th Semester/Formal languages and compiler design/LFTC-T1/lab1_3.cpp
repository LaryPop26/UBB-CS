#include <algorithm>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <regex>
#include <ranges>
#include <cctype>
#include <iomanip>
using namespace std;

// ===== Seturi de atomi lexicali =====
static const vector<string> cuvinteCheie = {
    "int","float","struct","char","string","if","else","for",
    "cin","cout","return","include","using","namespace", "endl"
};

static const vector<string> operatori = {
    "+","-","*","/","%","=","<",">","<=",">=","==","!=","<<",">>"
};

static const vector<string> delimitatori = {
    "(",")","{","}",";",",","<",">","#","."
};

// ===== Coduri atomice =====
enum CodAtom {
    CUVANT_CHEIE = 1,
    OPERATOR = 2,
    DELIMITATOR = 3,
    IDENTIFICATOR_SAU_CONSTANTA = 4
};

// ===== Funcții de clasificare =====
bool esteCuvantCheie(const string& s) {
    return ranges::any_of(cuvinteCheie, [&](const string& c){ return s == c; });
}
bool esteOperator(const string& s) {
    return ranges::any_of(operatori, [&](const string& c){ return s == c; });
}
bool esteDelimitator(const string& s) {
    return ranges::any_of(delimitatori, [&](const string& c){ return s == c; });
}
bool esteIdentificator(const string& s) {
    if (s.empty() || !isalpha(static_cast<unsigned char>(s[0]))) return false;

    // identificator simplu sau de forma ID.ID
    bool punctGasit = false;
    for (size_t i = 0; i < s.size(); i++) {
        char ch = s[i];
        if (ch == '.') {
            if (punctGasit) return false;          // maxim un punct
            punctGasit = true;
            // trebuie urmat obligatoriu de literă
            if (i + 1 == s.size() || !isalpha(static_cast<unsigned char>(s[i+1])))
                return false;
        } else if (!isalnum(static_cast<unsigned char>(ch)) && ch != '_') {
            return false;
        }
    }
    return true;
}
bool esteNumar(const string& s) {
    return regex_match(s, regex("^[0-9]+(\\.[0-9]+)?$"));
}

// ===== Tabela de simboluri =====
struct Entry {
    string key;
    int index;
};

class TabelaDeSimboluri {
private:
    static const int M = 211;
    vector<vector<Entry>> buckets;
    int curentIndex = 1;

    int hashFunction(const string& s) const {
        unsigned long h = 0;
        for (unsigned char c : s) h = h * 131 + c;
        return (int)(h % M);
    }

public:
    TabelaDeSimboluri() { buckets.resize(M); }

    int adauga(const string& key) {
        int pos = hashFunction(key);
        for (auto &e : buckets[pos])
            if (e.key == key)
                return e.index;
        buckets[pos].push_back({key, curentIndex});
        return curentIndex++;
    }

    vector<pair<int,string>> getSortedEntries() const {
        vector<pair<int,string>> out;
        for (int i=0;i<M;i++)
            for (auto &e: buckets[i])
                out.push_back({e.index, e.key});
        ranges::sort(out, [](auto &a, auto &b){ return a.first < b.first; });
        return out;
    }
};


vector<pair<int,int>> FIP; // (cod_atom, pozitie_TS)

// ===== Analizor lexical complet =====
int main() {
    ifstream fin("C://Users//popla//Desktop//LFTC//LFTC-T1//lab1_3.txt");
    if (!fin.is_open()) {
        cerr << " Nu s-a putut deschide fisierul lab1_3.txt\n";
        return 1;
    }

    ofstream foutErr("erori.txt");
    TabelaDeSimboluri TS;
    string linie;
    int nrLinie = 0;
    bool inBlockComment = false;

    while (getline(fin, linie)) {
        nrLinie++;

        // elimină spațiile inutile
        auto trim = [](string s) {
            s.erase(s.begin(), find_if(s.begin(), s.end(), [](int ch){ return !isspace(ch); }));
            s.erase(find_if(s.rbegin(), s.rend(), [](int ch){ return !isspace(ch); }).base(), s.end());
            return s;
        };
        linie = trim(linie);

        smatch match;

            // Cout/Cin cu mesaj între ghilimele
        regex coutMsg("^cout\\s*<<\\s*\"([^\"]*)\"\\s*;\\s*$");
        regex cinMsg("^cin\\s*>>\\s*\"([^\"]*)\"\\s*;\\s*$");

        if (regex_match(linie, match, coutMsg)) {
            string mesaj = match[1];
            int poz = TS.adauga(mesaj);
            FIP.push_back({CUVANT_CHEIE, -1});
            FIP.push_back({OPERATOR, -1});
            FIP.push_back({IDENTIFICATOR_SAU_CONSTANTA, poz});
            FIP.push_back({DELIMITATOR, -1});
            continue;
        }
        if (regex_match(linie, match, cinMsg)) {
            string mesaj = match[1];
            int poz = TS.adauga(mesaj);
            FIP.push_back({CUVANT_CHEIE, -1});
            FIP.push_back({OPERATOR, -1});
            FIP.push_back({IDENTIFICATOR_SAU_CONSTANTA, poz});
            FIP.push_back({DELIMITATOR, -1});
            continue;
        }

        // Cout/Cin cu expresie sau variabilă
        regex coutExpr(R"(^cout\s*<<\s*([a-zA-Z_][a-zA-Z0-9_]*(\s*[\+\-\*\/%<>=]\s*[a-zA-Z0-9_\.]+)*)\s*;\s*$)");
        regex cinExpr (R"(^cin\s*>>\s*([a-zA-Z_][a-zA-Z0-9_]*(\s*[\+\-\*\/%<>=]\s*[a-zA-Z0-9_\.]+)*)\s*;\s*$)");

        if (regex_match(linie, match, coutExpr)) {
            string expr = match[1];
            int poz = TS.adauga(expr);
            FIP.push_back({CUVANT_CHEIE, -1});
            FIP.push_back({OPERATOR, -1});
            FIP.push_back({IDENTIFICATOR_SAU_CONSTANTA, poz});
            FIP.push_back({DELIMITATOR, -1});
            continue;
        }
        if (regex_match(linie, match, cinExpr)) {
            string expr = match[1];
            int poz = TS.adauga(expr);
            FIP.push_back({CUVANT_CHEIE, -1});
            FIP.push_back({OPERATOR, -1});
            FIP.push_back({IDENTIFICATOR_SAU_CONSTANTA, poz});
            FIP.push_back({DELIMITATOR, -1});
            continue;
        }

        // ===== Altfel =====
        size_t i = 0;
        const size_t n = linie.size();

        while (i < n) {
            if (inBlockComment) {
                size_t pos = linie.find("*/", i);
                if (pos == string::npos) { i = n; continue; }
                inBlockComment = false;
                i = pos + 2;
                continue;
            }

            if (i+1 < n && linie[i] == '/' && linie[i+1] == '/') break; // comentariu linie
            if (i+1 < n && linie[i] == '/' && linie[i+1] == '*') {
                inBlockComment = true;
                i += 2;
                continue;
            }

            char ch = linie[i];

            // string literal
            if (ch == '"') {
                size_t j = i + 1;
                string content;
                bool closed = false;
                while (j < n) {
                    if (linie[j] == '\\' && j+1 < n) { content.push_back(linie[j]); content.push_back(linie[j+1]); j += 2; continue; }
                    if (linie[j] == '"') { closed = true; j++; break; }
                    content.push_back(linie[j++]);
                }
                if (!closed) {
                    string msg = "Eroare lexica la linia " + to_string(nrLinie) + ": string neinchis\n";
                    foutErr << msg; cerr << msg;
                    i = n;
                } else {
                    int poz = TS.adauga(content);
                    FIP.push_back({IDENTIFICATOR_SAU_CONSTANTA, poz});
                    i = j;
                }
                continue;
            }

            if (isalnum(static_cast<unsigned char>(ch)) || ch == '.' || ch == '_') {
                string token;
                size_t j = i;
                while (j < n && (isalnum(static_cast<unsigned char>(linie[j])) || linie[j] == '.' || linie[j] == '_'))
                    token.push_back(linie[j++]);

                if (esteCuvantCheie(token))
                    FIP.push_back({CUVANT_CHEIE, -1});
                else if (esteNumar(token))
                    FIP.push_back({IDENTIFICATOR_SAU_CONSTANTA, TS.adauga(token)});
                else if (esteIdentificator(token))
                    FIP.push_back({IDENTIFICATOR_SAU_CONSTANTA, TS.adauga(token)});
                else {
                    string msg = "Eroare lexica la linia " + to_string(nrLinie) + ": '" + token + "' necunoscut\n";
                    foutErr << msg; cerr << msg;
                }
                i = j;
                continue;
            }

            if (i+1 < n) {
                string two = linie.substr(i,2);
                if (esteOperator(two)) { FIP.push_back({OPERATOR, -1}); i += 2; continue; }
            }

            string one(1, ch);
            if (esteOperator(one)) { FIP.push_back({OPERATOR, -1}); i++; continue; }
            if (esteDelimitator(one)) { FIP.push_back({DELIMITATOR, -1}); i++; continue; }

            if (isspace(static_cast<unsigned char>(ch))) { i++; continue; }

            string msg = "Eroare lexica la linia " + to_string(nrLinie) + ": simbol necunoscut '";
            msg.push_back(ch); msg.push_back('\''); msg.push_back('\n');
            foutErr << msg; cerr << msg;
            i++;
        }
    }

    fin.close();
    foutErr.close();

    // ===== Salvare FIP și TS =====
    ofstream foutFIP("FIP.txt");
    foutFIP << setw(10) << "COD" << setw(15) << "POZ_TS\n";
    for (auto &p : FIP)
        foutFIP << setw(10) << p.first << setw(15) << p.second << '\n';
    foutFIP.close();

    auto entries = TS.getSortedEntries();
    ofstream foutTS("TS.txt");
    foutTS << "=== TABELA DE SIMBOLURI ===\n";
    for (auto &e : entries)
        foutTS << setw(4) << e.first << "  " << e.second << '\n';
    foutTS.close();

    cout << "\n Analiza terminata.\n";
    cout << "FIP -> FIP.txt\nTS  -> TS.txt\nErori -> erori.txt\n";
    return 0;
}
