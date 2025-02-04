from controller.service import SrvAutomobil
from domain.validator import Validator
from repository.repository import RepoAutomobil
from ui.console import Consola

repo = RepoAutomobil('./data/automobil.txt')
validator = Validator()
srv = SrvAutomobil(repo, validator, [])
console = Consola(srv)
console.run()
