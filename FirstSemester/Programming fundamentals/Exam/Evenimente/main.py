from Controller.controller import Controller
from Domain.validator import Validator
from Repository.repository import Repository
from UI.console import Console

console = Console(Controller(Repository('eveniment.txt'), Validator))
console.run()
