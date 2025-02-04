class RepositoryException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return str(self.message)

class BookAlreadyExists(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self, "Book already exists!")

class BookNotFound(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self, "There is no book with that ID!")

class ClientAlreadyExists(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self, "Client already exists!")

class ClientNotFound(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self, "There is no client with that ID!")

class RentAlreadyExists(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self, "Rent already exists!")

class RentNotFound(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self, "There is no rent with that ID!")

class ValidationException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return str(self.message)
