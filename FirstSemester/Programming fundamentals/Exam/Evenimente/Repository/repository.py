class Repository:
    def __init__(self, filename):
        """

        :param filename:
        """
        self.__filename = filename

    def load_from_file(self):
        evenimente = []
        with open(self.__filename) as file:
            lines = file.readlines()
            for line in file:
                if line.strip() != '\n':
                    data, ora, descriere = [i.strip() for i in line.split(',')]
                    evenimente.append((ora, descriere))
        return evenimente

    def save(self, event):
        with open(self.__filename, 'w') as file:
            file.write(f"{event.data},{event.ora},{event.descrire}")
