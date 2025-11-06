from Controller.locatie_srv import LocatieSrv
from Domain.validator import Validator
from Repository.locatie_repo import LocatieFileRepo
from UI.consola import Consola

repo_locatii = LocatieFileRepo("locatii.txt")
validator_locatii = Validator()
srv_locatii = LocatieSrv(repo_locatii, validator_locatii)
consola = Consola(srv_locatii)

consola.run()
