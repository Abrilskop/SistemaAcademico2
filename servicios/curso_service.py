# servicios/curso_service.py
from dao.curso_dao import CursoDAO
from modelos.curso import Curso

class CursoService:
    def __init__(self):
        self.cursoDAO = CursoDAO()

    def crear(self, accion, curso):
        return self.cursoDAO.operar(accion, curso)

    def listar(self):
        return self.cursoDAO.listar()

    def obtener(self, id_curso):
        return self.cursoDAO.obtener(id_curso)

    def cerrar(self):
        self.cursoDAO.cerrar()
