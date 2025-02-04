from repository.repo import RepoEmisiuni
from service.srv import Service
from ui.consola import Consola

repo = RepoEmisiuni('emisiuni.txt')
srv = Service(repo)
consola = Consola(srv)
consola.run()
