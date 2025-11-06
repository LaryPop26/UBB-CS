from Domain.locatie import Locatie

class LocatieFileRepo:
    def __init__(self, filename):
        self.__locatii = []
        self.__filename = filename
        self.__load_from_file()

    def __load_from_file(self):
        """
        incarca toate locatiile din fisier
        """
        with open(self.__filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if line != "\n":
                    id_locatie, denumire, tip, pret_pe_zi = [i.strip() for i in line.split(",")]
                    self.__locatii.append(Locatie(int(id_locatie), denumire, tip, int(pret_pe_zi)))

    def cauta_dupa_id(self, id_loc: int):
        """
        Functia cauta locatia cu id ul dat
        :param id_loc: id de cautat
        :return: locatia, daca este gasita, None altfel
        """
        for loc in self.__locatii:
            if loc.id_locatie == id_loc:
                return loc
        return None

    def get_all(self):
        """
        :return: lista cu locatiile citite
        """
        return self.__locatii
