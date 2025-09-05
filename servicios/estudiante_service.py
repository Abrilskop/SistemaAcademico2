# servicios/estudiante_service.py
from dao.estudiante_dao import EstudianteDAO
from modelos.estudiante import Estudiante

class EstudianteService:
    def __init__(self):
        self.estudianteDAO = EstudianteDAO()

    def crear(self, accion, estudiante):
        return self.estudianteDAO.operar(accion, estudiante)

    def listar(self):
        return self.estudianteDAO.listar()

    def obtener(self, id_estudiante):
        return self.estudianteDAO.obtener(id_estudiante)

    def cerrar(self):
        self.estudianteDAO.cerrar()
