# servicios/matricula_service.py
from dao.matricula_dao import MatriculaDAO
from modelos.matricula import Matricula

class MatriculaService:
    def __init__(self):
        self.matriculaDAO = MatriculaDAO()

    def crear(self, accion, matricula):
        return self.matriculaDAO.operar(accion, matricula)

    def listar(self):
        return self.matriculaDAO.listar()

    def cerrar(self):
        self.matriculaDAO.cerrar()
