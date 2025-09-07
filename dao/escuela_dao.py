from modelos.escuela import Escuela
from conexion import Conexion
class EscuelaDAO:
    def __init__(self):
        self.conexion = Conexion()

    def operar(self, accion, escuela: Escuela):
        return self.conexion.ejecutar("sp_escuela", [accion, escuela.id, escuela.nombre])

    def listar(self):
        return self.conexion.ejecutarsinparametros("sp_listar_escuela")
    
    def obtener(self, id_escuela):
        return self.conexion.ejecutar("sp_obtener_escuela", [id_escuela])

    def cerrar(self):
        self.conexion.cerrar()