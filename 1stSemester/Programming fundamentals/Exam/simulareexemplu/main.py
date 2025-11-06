from Controller.srv_jucator import SrvJucator
from Domain.validator import Validator
from Repository.repo_jucator import RepoFileJucator
from UI.console import Console

repo = RepoFileJucator("jucatori.txt")
validator = Validator()
srv = SrvJucator(repo, validator)
ui = Console(srv)

ui.run()