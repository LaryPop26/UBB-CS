from datetime import datetime

class Validator:
    @staticmethod
    def validare_data(data: str):
        """

        :param data:
        :return:
        """
        try:
            datetime.strptime(data, '%d.%m.%Y')
            return True
        except ValueError:
            return False

    @staticmethod
    def validare_ora(ora: str):
        """

        :param ora:
        :return:
        """
        try:
            datetime.strptime(ora, '%h:%m')
            return True
        except ValueError:
            return False
