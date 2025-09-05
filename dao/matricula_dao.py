# dao/matricula_dao.py
from modelos.matricula import Matricula
from conexion import Conexion

class MatriculaDAO:
    def __init__(self):
        self.conexion = Conexion()

    def operar(self, accion, matricula: Matricula):
        return self.conexion.ejecutar("sp_matricula", [accion, matricula.id, matricula.id_estudiante, matricula.id_curso, matricula.ciclo])

    def listar(self):
        return self.conexion.ejecutarsinparametros("sp_listar_matriculas")

    def cerrar(self):
        self.conexion.cerrar()
