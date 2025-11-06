class ValidationError(Exception):
    def __init__(self, message):
        self.message = message

class NotNegative(ValidationError):
    def __init__(self):
        super().__init__('Numarul nu poate fi negativ')

class ServiceError(Exception):
    def __init__(self, message):
        self.message = message

class NoInput(ServiceError):
    def __init__(self):
        super().__init__("List is empthy")

class RepoException(Exception):
    def __init__(self, msg):
        self.msg = msg

class AlreadyExists(RepoException):
    def __init__(self):
        super().__init__('Jucatorul exista deja!')
