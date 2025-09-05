# controladores/curso_controller.py
from modelos.curso import Curso
from servicios.curso_service import CursoService
from flask import Blueprint, request, jsonify

curso_bp = Blueprint('curso', __name__)
servicios = CursoService()

@curso_bp.route('/api/curso/mantenimiento', methods=['POST'])
def mantenimiento_curso():
    data = request.get_json()
    accion = data.get('accion')
    id_curso = data.get('id')
    nombre = data.get('nombre')
    creditos = data.get('creditos')
    
    curso = Curso(id_curso, nombre, creditos)
    resultado = servicios.crear(accion, curso)
    return jsonify(resultado)

@curso_bp.route('/api/curso/listar', methods=['GET'])
def listar_cursos():
    data = servicios.listar()
    return jsonify(data)

@curso_bp.route('/api/curso/<int:id_curso>', methods=['POST'])
def obtener_curso(id_curso):
    data = servicios.obtener(id_curso)
    return jsonify(data)
