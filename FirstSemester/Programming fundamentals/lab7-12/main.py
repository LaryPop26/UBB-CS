from Controller.rental_srv import RentalService
from Controller.book_srv import BookService
from Controller.client_srv import ClientService
from Repository.FileRepository.book_file_repo import BookFileRepository
from Repository.FileRepository.client_file_repo import ClientFileRepository
from Repository.FileRepository.rent_file_repo import RentFileRepository
from UI.console import Console
from Domain.Validation.validator import BookValidator, ClientValidator, RentalValidator

# book_repo = BookRepository()
book_repo = BookFileRepository("data/books.txt")
book_validator = BookValidator()
book_srv = BookService(book_repo, book_validator)

# client_repo = ClientRepository()
client_repo = ClientFileRepository("data/clients.txt")
client_validator = ClientValidator()
client_srv = ClientService(client_repo, client_validator)

# rent_repo = RentRepository()
rent_repo = RentFileRepository("data/rent.txt")
rent_validator = RentalValidator()
rent_srv = RentalService(rent_repo, book_repo, client_repo, rent_validator, book_validator, client_validator)

console = Console(book_srv, client_srv, rent_srv)
console.start()
