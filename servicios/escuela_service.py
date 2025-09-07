from dao.escuela_dao import EscuelaDAO
from modelos.escuela import Escuela

class EscuelaService:
    def __init__(self):
        self.escuelaDAO = EscuelaDAO()

    def crear(self, accion,escuela):
        return self.escuelaDAO.operar(accion, escuela)

    def listar(self):
        return self.escuelaDAO.listar()
    
    def obtener(self, id_escuela):
        return self.escuelaDAO.obtener(id_escuela)

    def cerrar(self):
        self.escuelaDAO.cerrar()