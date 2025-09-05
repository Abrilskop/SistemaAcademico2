# dao/estudiante_dao.py
from modelos.estudiante import Estudiante
from conexion import Conexion

class EstudianteDAO:
    def __init__(self):
        self.conexion = Conexion()

    def operar(self, accion, estudiante: Estudiante):
        return self.conexion.ejecutar("sp_estudiante", [accion, estudiante.id, estudiante.nombres, estudiante.apellidos, estudiante.correo, estudiante.id_escuela])

    def listar(self):
        return self.conexion.ejecutarsinparametros("sp_listar_estudiante")

    def obtener(self, id_estudiante):
        return self.conexion.ejecutar("sp_obtener_estudiante", [id_estudiante])

    def cerrar(self):
        self.conexion.cerrar()
