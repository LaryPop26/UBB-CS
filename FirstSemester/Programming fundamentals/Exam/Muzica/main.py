from controller.srv import Controller
from domain.validator import Validator
from repository.repo import Repo
from ui.consola import Consola

repo = Repo('./data/melodii.txt')
validator = Validator()
srv = Controller(repo, validator)
consola = Consola(srv)
consola.run()
