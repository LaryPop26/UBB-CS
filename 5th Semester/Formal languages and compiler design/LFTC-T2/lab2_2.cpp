#include <bits/stdc++.h>
using namespace std;

/* =========================
   CLASA AUTOMAT FINIT (AFD)
   ========================= */
class AutomatFinit {
    set<string> stari;
    set<char> alfabet;
    map<pair<string,char>, string> tranzitii;
    string stareInitiala;
    set<string> stariFinale;

public:
    void seteazaInitiala(const string& s) { stareInitiala = s; stari.insert(s); }
    void adaugaFinala(const string& s) { stariFinale.insert(s); stari.insert(s); }
    void adaugaTranzitie(const string& from, char c, const string& to) {
        tranzitii[{from, c}] = to;
        stari.insert(from); stari.insert(to); alfabet.insert(c);
    }
    bool accepta(const string& secv) const {
        string cur = stareInitiala;
        for (char cc : secv) {
            auto it = tranzitii.find({cur, cc});
            if (it == tranzitii.end()) return false;
            cur = it->second;
        }
        return stariFinale.count(cur) > 0;
    }
};

/* =========================
   AFD-uri SPECIFICE
   ========================= */

// Identificatori: [a-zA-Z_][a-zA-Z0-9_]*
AutomatFinit makeAF_Ident() {
    AutomatFinit af;
    af.seteazaInitiala("q0");
    af.adaugaFinala("q1");

    for (char c='a'; c<='z'; ++c) af.adaugaTranzitie("q0", c, "q1");
    for (char c='A'; c<='Z'; ++c) af.adaugaTranzitie("q0", c, "q1");
    af.adaugaTranzitie("q0", '_', "q1");

    for (char c='a'; c<='z'; ++c) af.adaugaTranzitie("q1", c, "q1");
    for (char c='A'; c<='Z'; ++c) af.adaugaTranzitie("q1", c, "q1");
    for (char c='0'; c<='9'; ++c) af.adaugaTranzitie("q1", c, "q1");
    af.adaugaTranzitie("q1", '_', "q1");

    return af;
}

// Int: [0-9]+
AutomatFinit makeAF_Int() {
    AutomatFinit af;
    af.seteazaInitiala("q0");
    af.adaugaFinala("q1");
    for (char c='0'; c<='9'; ++c) {
        af.adaugaTranzitie("q0", c, "q1");
        af.adaugaTranzitie("q1", c, "q1");
    }
    return af;
}

// Real: [0-9]+\.[0-9]+
AutomatFinit makeAF_Real() {
    AutomatFinit af;
    af.seteazaInitiala("q0");
    af.adaugaFinala("q3");
    for (char c='0'; c<='9'; ++c) {
        af.adaugaTranzitie("q0", c, "q1");
        af.adaugaTranzitie("q1", c, "q1");
        af.adaugaTranzitie("q2", c, "q3");
        af.adaugaTranzitie("q3", c, "q3");
    }
    af.adaugaTranzitie("q1", '.', "q2");
    return af;
}

/* =========================
   Tabela de simboluri (hash)
   ========================= */
struct Entry { string key; int index; };

class TabelaDeSimboluri {
    static const int M = 211;
    vector<vector<Entry>> bkt;
    int nextIdx = 1;

    int hf(const string& s) const {
        unsigned long h = 0;
        for (unsigned char c : s) h = h * 131 + c;
        return (int)(h % M);
    }
public:
    TabelaDeSimboluri(): bkt(M) {}
    int adauga(const string& key) {
        int pos = hf(key);
        for (auto& e : bkt[pos]) if (e.key == key) return e.index;
        bkt[pos].push_back({key, nextIdx});
        return nextIdx++;
    }
    vector<pair<int,string>> entriesSorted() const {
        vector<pair<int,string>> out;
        for (auto& v : bkt) for (auto& e : v) out.push_back({e.index, e.key});
        sort(out.begin(), out.end());
        return out;
    }
};

/* =========================
   seturi statice
   ========================= */
static const vector<string> CUVINTE_CHEIE = {
    "int","float","struct","char","string","if","else","for",
    "cin","cout","return","include","using","namespace","endl","while","do","break","continue"
};
static const vector<string> OP2 = {"<=",">=","==","!=","<<",">>","&&","||","++","--","+=","-=","*=","/=","%="};
static const vector<string> OP1 = {"+","-","*","/","%","=","<",">","!","&","|","^","~"};
static const vector<string> DELIMS = {"(",")","{","}","[","]",";",",","#",".",":"};

/* =========================
   FIP
   ========================= */
enum CodAtom { CUVANT_CHEIE = 1, OPERATOR = 2, DELIMITATOR = 3, IDENT_SAU_CONST = 4 };

/* =========================
   Utilitare
   ========================= */
static inline bool isLetter(char c){ return std::isalpha((unsigned char)c); }
static inline bool isDigit (char c){ return std::isdigit((unsigned char)c); }
static inline bool isIdChar(char c){ return std::isalnum((unsigned char)c) || c=='_'; }

bool inVec(const vector<string>& v, const string& s) {
    return find(v.begin(), v.end(), s) != v.end();
}

/* încearcă să potrivească operator de 2 sau 1 caractere */
bool matchOperator(const string& src, size_t pos, string& op) {
    if (pos + 1 < src.size()) {
        string two = src.substr(pos, 2);
        if (inVec(OP2, two)) { op = two; return true; }
    }
    string one(1, src[pos]);
    if (inVec(OP1, one)) { op = one; return true; }
    return false;
}
bool matchDelimiter(const string& src, size_t pos, string& d) {
    string one(1, src[pos]);
    if (inVec(DELIMS, one)) { d = one; return true; }
    return false;
}

/* =========================
   Analizor lexical cu AF
   ========================= */
int main(int argc, char** argv) {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string inputPath = (argc >= 2 ? string(argv[1]) : string("test.txt"));
    ifstream fin(inputPath);
    if (!fin.is_open()) {
        cerr << "Nu s-a putut deschide fisierul: " << inputPath << "\n";
        return 1;
    }

    ofstream ferr("erori.txt");
    TabelaDeSimboluri TS;
    vector<pair<int,int>> FIP;

    AutomatFinit AF_ID   = makeAF_Ident();
    AutomatFinit AF_INT  = makeAF_Int();
    AutomatFinit AF_REAL = makeAF_Real();

    bool inBlockComment = false;
    string line;
    int nrLinie = 0;

    while (getline(fin, line)) {
        ++nrLinie;
        size_t i = 0, n = line.size();

        while (i < n) {
            char c = line[i];

            // Comentarii block /* ... */
            if (inBlockComment) {
                size_t endpos = line.find("*/", i);
                if (endpos == string::npos) { // continuă pe linia următoare
                    i = n; break;
                } else {
                    inBlockComment = false;
                    i = endpos + 2;
                    continue;
                }
            }

            // Skipp whitespace
            if (isspace((unsigned char)c)) { ++i; continue; }

            // Comentariu linie //
            if (c=='/' && i+1<n && line[i+1]=='/') break;

            // Început comentariu block
            if (c=='/' && i+1<n && line[i+1]=='*') {
                inBlockComment = true; i += 2; continue;
            }

            // String literal " ... "
            if (c == '"') {
                size_t j = i + 1;
                string content;
                bool closed = false;
                while (j < n) {
                    if (line[j] == '\\' && j+1 < n) { // escape
                        content.push_back(line[j]);
                        content.push_back(line[j+1]);
                        j += 2;
                        continue;
                    }
                    if (line[j] == '"') { closed = true; ++j; break; }
                    content.push_back(line[j++]);
                }
                if (!closed) {
                    string msg = "Eroare lexica la linia " + to_string(nrLinie) + ": string neinchis\n";
                    ferr << msg; cerr << msg;
                    i = n; continue;
                } else {
                    int poz = TS.adauga("\"" + content + "\""); // stocăm inclusiv ghilimelele pentru unicitate
                    FIP.push_back({IDENT_SAU_CONST, poz});
                    i = j; continue;
                }
            }

            // Identificatori / cuvinte cheie / numere
            if (isLetter(c) || c=='_' || isDigit(c)) {
                // colectăm token maximal format din [a-zA-Z0-9_ .] dar gestionăm special punctul pentru numere reale
                size_t j = i;
                string token;

                if (isLetter(c) || c=='_') {
                    // identificator sau cuvânt cheie
                    while (j<n && isIdChar(line[j])) token.push_back(line[j++]);

                    if (inVec(CUVINTE_CHEIE, token)) {
                        FIP.push_back({CUVANT_CHEIE, -1});
                    } else if (AF_ID.accepta(token)) {
                        int poz = TS.adauga(token);
                        FIP.push_back({IDENT_SAU_CONST, poz});
                    } else {
                        string msg = "Eroare lexica la linia " + to_string(nrLinie) + ": identificator invalid '" + token + "'\n";
                        ferr << msg; cerr << msg;
                    }
                    i = j; continue;
                }

                // altfel începe cu cifră => întreg sau real
                if (isDigit(c)) {
                    // adună partea întreagă
                    while (j<n && isDigit(line[j])) token.push_back(line[j++]);

                    // verific real: '.' urmat de cifră
                    if (j<n && line[j]=='.' && (j+1<n) && isDigit(line[j+1])) {
                        token.push_back(line[j++]); // punct
                        while (j<n && isDigit(line[j])) token.push_back(line[j++]);
                        if (AF_REAL.accepta(token)) {
                            int poz = TS.adauga(token);
                            FIP.push_back({IDENT_SAU_CONST, poz});
                        } else {
                            string msg = "Eroare lexica la linia " + to_string(nrLinie) + ": constanta reala invalida '" + token + "'\n";
                            ferr << msg; cerr << msg;
                        }
                        i = j; continue;
                    } else {
                        // rămâne întreg
                        if (AF_INT.accepta(token)) {
                            int poz = TS.adauga(token);
                            FIP.push_back({IDENT_SAU_CONST, poz});
                        } else {
                            string msg = "Eroare lexica la linia " + to_string(nrLinie) + ": constanta intreaga invalida '" + token + "'\n";
                            ferr << msg; cerr << msg;
                        }
                        i = j; continue;
                    }
                }
            }

            // Operator (2-char prioritar) sau delimitator
            string op;
            if (matchOperator(line, i, op)) {
                FIP.push_back({OPERATOR, -1});
                i += op.size();
                continue;
            }

            string d;
            if (matchDelimiter(line, i, d)) {
                FIP.push_back({DELIMITATOR, -1});
                i += 1;
                continue;
            }

            // Simbol necunoscut
            {
                string msg = "Eroare lexica la linia " + to_string(nrLinie) + ": simbol necunoscut '";
                msg.push_back(line[i]); msg += "'\n";
                ferr << msg; cerr << msg;
                ++i;
            }
        }
    }

    fin.close();
    ferr.close();

    // Scriere FIP
    ofstream ffip("FIP.txt");
    ffip << setw(10) << "COD" << setw(15) << "POZ_TS\n";
    for (auto &p : FIP) ffip << setw(10) << p.first << setw(15) << p.second << "\n";
    ffip.close();

    // Scriere TS
    ofstream fts("TS.txt");
    fts << "=== TABELA DE SIMBOLURI ===\n";
    for (auto &e : TS.entriesSorted())
        fts << setw(4) << e.first << "  " << e.second << "\n";
    fts.close();

    cout << "Analiza terminata.\nFIP -> FIP.txt\nTS  -> TS.txt\nErori -> erori.txt\n";
    return 0;
}
