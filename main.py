from controladores.escuela_controller import EscuelaController

controlador = EscuelaController()
html = controlador.mostrar_escuela()
print(html)
controlador.cerrar()
