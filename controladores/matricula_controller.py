# controladores/matricula_controller.py
from modelos.matricula import Matricula
from servicios.matricula_service import MatriculaService
from flask import Blueprint, request, jsonify

matricula_bp = Blueprint('matricula', __name__)
servicios = MatriculaService()

@matricula_bp.route('/api/matricula/mantenimiento', methods=['POST'])
def mantenimiento_matricula():
    data = request.get_json()
    accion = data.get('accion')
    id_matricula = data.get('id')
    id_estudiante = data.get('id_estudiante')
    id_curso = data.get('id_curso')
    ciclo = data.get('ciclo')
    
    matricula = Matricula(id_matricula, id_estudiante, id_curso, ciclo)
    resultado = servicios.crear(accion, matricula)
    return jsonify(resultado)

@matricula_bp.route('/api/matricula/listar', methods=['GET'])
def listar_matriculas():
    data = servicios.listar()
    return jsonify(data)
