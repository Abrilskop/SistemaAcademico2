# controladores/estudiante_controller.py
from servicios.estudiante_service import EstudianteService
from flask import Blueprint, request, jsonify
from modelos.estudiante import Estudiante

estudiante_bp = Blueprint('estudiante', __name__)
servicios = EstudianteService()

@estudiante_bp.route('/api/estudiante/mantenimiento', methods=['POST'])
def mantenimiento_estudiante():
    data = request.get_json()
    accion = data.get('accion')
    id_estudiante = data.get('id')
    nombres = data.get('nombres')
    apellidos = data.get('apellidos')
    correo = data.get('correo')
    id_escuela = data.get('id_escuela')
    
    estudiante = Estudiante(id_estudiante, nombres, apellidos, correo, id_escuela)
    resultado = servicios.crear(accion, estudiante)
    return jsonify(resultado)

@estudiante_bp.route('/api/estudiante/listar', methods=['GET'])
def listar_estudiantes():
    data = servicios.listar()
    return jsonify(data)

# TO DO: Reparar error de obtener_studiante postman
@estudiante_bp.route('/api/estudiante/<int:id_estudiante>', methods=['POST'])
def obtener_estudiante(id_estudiante):
    data = servicios.obtener(id_estudiante)
    return jsonify(data)
