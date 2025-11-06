from Domain.domain import Eveniment
from Domain.validator import Validator

class Controller:
    def __init__(self, repo, validator):
        """

        :param repo:
        :param validator:
        """
        self.__repo = repo
        self.__validator = validator

    def add(self, data, ora, descriere):
        if not self.__validator.validare_data(data):
            return Exception("Data invalida")
        if not self.__validator.validare_ora(ora):
            return Exception("Ora invalida")
        event = Eveniment(data, ora, descriere)
        self.__repo.save(event)

    def get_evenimente_pt_data(self, data):
        events = self.__repo.load_from_file()
        if not self.__validator.validare_data(data):
            return Exception("Data invalida")
        filtrare = [event for event in events if event.date == data]
        return sorted(filtrare, key=lambda event: event.time)

    def export_events(self, output, cuvant):
        events = self.__repo.load_from_file()
        filtrare = [event for event in events if cuvant in event.descriere]
        with open(output, 'w') as file:
            for event in filtrare:
                file.write(event.descriere + '\n')
