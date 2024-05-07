from flask import Blueprint
from controllers.asistencia_controller import definir_api, filtrar_api, index, filtrar, agregar_palabra, activar_palabra, inactivar_palabra, listar, diccionario

asistencia_bp = Blueprint('asistencia_bp', __name__)

asistencia_bp.route('/', methods=['GET'])(index)
# asistencia_bp.route('/listado', methods=['GET'])(listar)
# asistencia_bp.route('/filtrar', methods=['GET'])(filtrar)
