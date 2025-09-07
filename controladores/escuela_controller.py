from servicios.escuela_service import EscuelaService
from flask import Blueprint, request, jsonify
from modelos.escuela import Escuela

escuela_bp = Blueprint('escuela', __name__)
servicios=EscuelaService()

@escuela_bp.route('/api/escuela/mantenimiento', methods=['POST'])
def mantenimiento_escuela():
    data = request.get_json()
    print(data)
    accion = data.get('accion')
    pid = data.get('id')
    pnombre = data.get('nombre')
    escuela=Escuela(pid,pnombre)
    data=servicios.crear(accion,escuela)
    return jsonify(data)

@escuela_bp.route('/api/escuela/listar', methods=['GET'])
def listar_escuela():
    data=servicios.listar()
    return jsonify(data)

@escuela_bp.route('/api/escuela<int:id_escuela>', methods=['POST'])
def obtener_curso(id_curso):
    data = servicios.obtener(id_curso)
    return jsonify(data)
