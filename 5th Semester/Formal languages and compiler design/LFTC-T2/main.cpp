#include <iostream>
#include <fstream>
#include <map>
#include <set>
#include <string>
#include <vector>
#include <cstdlib>
#include <assert.h>

class AutomatFinit {
public:
	AutomatFinit() {}

	void citeste_din_fisier(std::string& nume_fisier) {
		std::ifstream in(nume_fisier);
		assert(in.is_open());

		std::string linie;
		std::getline(in, linie); 
		std::getline(in, linie);

		// stari
		size_t pos = 0;
		while ((pos = linie.find(',')) != std::string::npos) {
			m_stari.insert(linie.substr(0, pos));
			linie.erase(0, pos + 1);
		}
		if (!linie.empty()) m_stari.insert(linie);

		// alfabet
		std::getline(in, linie);
		std::getline(in, linie);
		for (char c : linie) {
			if (c != ',' && c != ' ') {
				m_alfabet.insert(c);
			}
		}

		// stare initiala
		std::getline(in, linie);
		std::getline(in, m_stare_initiala);

		// stari finale
		std::getline(in, linie);
		std::getline(in, linie);
		pos = 0;
		while ((pos = linie.find(',')) != std::string::npos) {
			m_stari_finale.insert(linie.substr(0, pos));
			linie.erase(0, pos + 1);
		}
		if (!linie.empty()) m_stari_finale.insert(linie);

		// tranzitii
		std::getline(in, linie);
		while (std::getline(in, linie)) {
			if (linie.empty()) continue;

			size_t pos1 = linie.find(',');
			size_t pos2 = linie.find(',', pos1 + 1);

			std::string stare1 = linie.substr(0, pos1);
			char simbol = linie[pos1 + 1];
			std::string stare2 = linie.substr(pos2 + 1);

			m_tranzitii[{stare1, simbol}] = stare2;
		}

		in.close();
		std::cout << "Automat incarcat cu succes!!";
	}

	void citeste_tastatura() {
		int n;
		std::cout << "Numar de stari: ";
		std::cin >> n;
		std::cout << "Introdu starile: ";
		for (int i = 0; i < n; i++) {
			std::string stare;
			std::cin >> stare;
			m_stari.insert(stare);
		}

		std::cout << "Numar de simboluri in alfabet: ";
		std::cin >> n;
		std::cout << "Introdu simbolurile: ";
		for (int i = 0; i < n; i++) {
			char simbol;
			std::cin >> simbol;
			m_alfabet.insert(simbol);
		}

		std::cout << "Stare initiala: ";
		std::cin >> m_stare_initiala;

		std::cout << "Numar de stari finale: ";
		std::cin >> n;
		std::cout << "Introdu starile finale: ";
		for (int i = 0; i < n; i++) {
			std::string stare;
			std::cin >> stare;
			m_stari_finale.insert(stare);
		}

		std::cout << "Numar de tranzitii: ";
		std::cin >> n;
		std::cout << "Introdu tranzitiile (stare1 simbol stare2): ";
		for (int i = 0; i < n; i++) {
			std::string sursa, dest;
			char simbol;
			std::cin >> sursa >> simbol >> dest;
			m_tranzitii[{sursa, simbol}] = dest;
		}

		std::cout << "Automatul a fost introdus cu succes!";
	}

	void afiseaza_stari() {
		clear_screen();
		std::cout << "/////  Multimea Starilor  /////";
		std::cout << "Q = ";
		for (const auto& stare : m_stari) {
			std::cout << stare << " ";
		}

		std::cout << '\n';
	}

	void afiseaza_alfabet() {
		clear_screen();
		std::cout << "/////  Alfabet  /////\n";
		std::cout << "Sigma = \n";
		for (char c : m_alfabet) {
			std::cout << c << " ";
		}

		std::cout << '\n';
	}

	void afiseaza_tranzitii() {
		clear_screen();
		std::cout << "/////  Tranzitii  /////\n";
		std::cout << "Delta = \n";
		for (const auto& tr : m_tranzitii) {
			std::cout << " (" << tr.first.first << ", '" << tr.first.second << "') -> " << tr.second << '\n';
		}
	}

	void afiseaza_stari_finale() {
		clear_screen();
		std::cout << "/////  Stari Finale  /////\n";
		std::cout << "F = \n";
		for (const auto& sf : m_stari_finale) {
			std::cout << sf << " ";
		}

		std::cout << '\n';
		std::cout << "Stare initiala: " << m_stare_initiala << '\n';
	}

	bool verifica_secventa(std::string& secventa) {
		clear_screen();
		std::string stare_curenta = m_stare_initiala;

		std::cout << "/////  Verificare Secventa  /////\n";
		std::cout << "Parcurgere: " << stare_curenta;

		for (char simbol : secventa) {
			auto it = m_tranzitii.find({ stare_curenta, simbol });
			if (it == m_tranzitii.end()) {
				std::cout << "--X\n";
				std::cout << "SECVENTA E RESPINSA\n";
				std::cout << "Nu exista tranzitie pt simbolul " << simbol << " din starea " << stare_curenta;
				return false;
			}
			stare_curenta = it->second;
			std::cout << " -- '" << simbol << "' ---> " << stare_curenta;
		}

		std::cout << '\n';

		bool acceptat = m_stari_finale.find(stare_curenta) != m_stari_finale.end();
		if (acceptat) {
			std::cout << "SECVENTA E ACCEPTATA!\n";
		}
		else {
			std::cout << "SECVENTA E RESPINSA!\n";
			std::cout << "Starea " << stare_curenta << " NU este stare finala!\n";
		}

		return acceptat;
	}

	std::string prefix(std::string& secventa) {
		clear_screen();
		std::string stare_curenta = m_stare_initiala;

		std::string prefix_acceptat = "";

		std::cout << "/////  Cautare Prefix  : " << secventa << "  /////\n";
		if (m_stari_finale.find(stare_curenta) != m_stari_finale.end()) {
			prefix_acceptat = "";
			std::cout << "Sirul vid e acceptat";
		}

		for (size_t i = 0; i < secventa.length(); i++) {
			char simbol = secventa[i];
			auto it = m_tranzitii.find({ stare_curenta, simbol });

			if (it == m_tranzitii.end()) {
				std::cout << "Nu exista tranzitie pentru '" << simbol << "' din starea " << stare_curenta << '\n';
				break;
			}

			stare_curenta = it->second;

			prefix_acceptat = secventa.substr(0, i + 1);
		}

		if (prefix_acceptat.empty()) {
			std::cout << "Nu exista prefix acceptat!";
		}
		else {
			std::cout << "Cel mai lung prefix acceptat: " << prefix_acceptat << " \n";
		}

		return prefix_acceptat;
	}
	private:
		void clear_screen() {
			system("cls");
		}

	private:
		std::set<std::string> m_stari;
		std::set<char> m_alfabet;
		std::string m_stare_initiala;
		std::set<std::string> m_stari_finale;
		std::map<std::pair<std::string, char>, std::string> m_tranzitii;

	/*
	*
	AutomatFinit
	stareInitiala: String
	stari: Set<String>
	alfabet: Set<Char>
	stariFinale: Set<String>
	tranzitii: Map<(String, Char), String>
	 *
	 */
};

void afiseaza_meniu() {
	std::cout << "\n////// MENIU AUTOMAT FINIT //////\n";
	std::cout << "1. Afiseaza multimea starilor\n";
	std::cout << "2. Afiseaza alfabetul\n";
	std::cout << "3. Afiseaza tranzitiile\n";
	std::cout << "4. Afiseaza starile finale\n";
	std::cout << "5. Verifica daca o secventa este acceptata\n";
	std::cout << "6. Gaseste cel mai lung prefix acceptat\n";
	std::cout << "0. Iesire\n";
	std::cout << "=========================================\n";
	std::cout << "Optiune: ";
}

int main() {
	AutomatFinit af;
	int optiune;

	std::cout << "/// INCARCARE AUTOMAT FINIT ///\n";
	std::cout << "1. Citire din fisier\n";
	std::cout << "2. Citire de la tastatura\n";
	std::cout << "Optiune: ";
	std::cin >> optiune;

	if (optiune == 1) {
		std::string numeFisier;
		std::cout << "Numele fisierului: ";
		std::cin >> numeFisier;
		af.citeste_din_fisier(numeFisier);
	}
	else if (optiune == 2) {
		af.citeste_tastatura();
	}
	else {
		std::cout << "Optiune invalida!\n";
		return 1;
	}

	std::cout << "\nApasa ENTER pentru a continua...";
	std::cin.ignore();
	std::cin.get();


	// Meniu principal
	do {
		afiseaza_meniu();
		std::cin >> optiune;

		switch (optiune) {
		case 1:
			af.afiseaza_stari();
			break;
		case 2:
			af.afiseaza_alfabet();
			break;
		case 3:
			af.afiseaza_tranzitii();
			break;
		case 4:
			af.afiseaza_stari_finale();
			break;
		case 5: {
			std::string secventa;
			std::cout << "Introduceti secventa: ";
			std::cin >> secventa;
			af.verifica_secventa(secventa);
			break;
		}
		case 6: {
			std::string secventa;
			std::cout << "Introduceti secventa: ";
			std::cin >> secventa;
			af.prefix(secventa);
			break;
		}
		case 0:
			std::cout << "La revedere!\n";
			break;
		default:
			std::cout << "Optiune invalida!\n";
		}

		if (optiune != 0) {
			std::cout << "\nApasa ENTER pentru a continua...";
			std::cin.ignore();
			std::cin.get();
		}
	} while (optiune != 0);

	return 0;
}