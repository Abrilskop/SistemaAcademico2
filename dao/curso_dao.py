# dao/curso_dao.py
from modelos.curso import Curso
from conexion import Conexion

class CursoDAO:
    def __init__(self):
        self.conexion = Conexion()

    def operar(self, accion, curso: Curso):
        return self.conexion.ejecutar("sp_curso", [accion, curso.id, curso.nombre, curso.creditos])

    def listar(self):
        return self.conexion.ejecutarsinparametros("sp_listar_cursos")

    def obtener(self, id_curso):
        return self.conexion.ejecutar("sp_obtener_curso", [id_curso])

    def cerrar(self):
        self.conexion.cerrar()
