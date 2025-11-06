from Controller.srv_tractor import SrvTractor
from Domain.validator import Validator
from Repository.repo_tractor import RepoTractor
from UI.console import Console

repo = RepoTractor('tractoare.txt')
validator = Validator()
srv = SrvTractor(repo, validator, [])
console = Console(srv)
console.run()
