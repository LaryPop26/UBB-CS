#include <algorithm>
#include <iostream>
#include <fstream>
#include <string>
#include <regex>
#include <vector>
#include <cctype>
using namespace std;

bool esteCuvantCheie(const string& s) {
    static const vector<string> cuvCheie = {
        "int","float","struct","char","string","if","else","for","cin","cout","return"
    };
    return ranges::any_of(cuvCheie, [&](const string& c) {
        return s == c;
    });
}

bool esteOperator(const string& s) {
    static const vector<string> op = {
        "+","-","*","/","%","=","<",">","<=",">=","==","!="
    };
    for (auto& c : op)
        if (s == c) return true;
    return false;
}

bool esteDelimitator(const string& s) {
    static const vector<string> del = {
        "(",")","{","}",";",","
    };
    return ranges::any_of(del, [&](const string& c) {
        return s == c;
    });
}

bool esteIdentificator(const string& s) {
    if (!isalpha(s[0])) return false;
    return ranges::all_of(s, [](unsigned char ch) {
        return isalnum(ch);
    });
}

bool esteNumar(const string& s) {
    return regex_match(s, regex("^[0-9]+(\\.[0-9]+)?$"));
}

int main() {
    ifstream fin("C://Users//popla//Desktop//LFTC//LFTC-T1//cerc.txt");
    if (!fin.is_open()) {
        cout << "Eroare: nu s-a putut deschide fisierul program.txt\n";
        return 1;
    }

    string cuv;
    cout << "=== ATOMI LEXICALI IDENTIFICATI ===\n\n";

    while (fin >> cuv) {

        string token;
        for (char ch : cuv) {
            if (isalnum(ch) || ch == '.' || ch == '_')
                token += ch;
            else {
                if (!token.empty()) {
                    if (esteCuvantCheie(token))
                        cout << "< " << token << " , cuvant cheie >\n";
                    else if (esteNumar(token))
                        cout << "< " << token << " , constanta numerica >\n";
                    else if (esteIdentificator(token))
                        cout << "< " << token << " , identificator >\n";
                    token.clear();
                }
                string s(1, ch);
                if (esteOperator(s))
                    cout << "< " << s << " , operator >\n";
                else if (esteDelimitator(s))
                    cout << "< " << s << " , delimitator >\n";
            }
        }
        if (!token.empty()) {
            if (esteCuvantCheie(token))
                cout << "< " << token << " , cuvant cheie >\n";
            else if (esteNumar(token))
                cout << "< " << token << " , constanta numerica >\n";
            else if (esteIdentificator(token))
                cout << "< " << token << " , identificator >\n";
        }
    }

    fin.close();
    return 0;
}
