import os

from flask import request, jsonify, make_response, render_template
# from models.response_model import ResponseModel
# from services.filtros_service import FiltrosService
# from services.archivos_service import ArchivosService
# from services.palabras_service import PalabrasService

# filtros_service = FiltrosService()
# archivos_service = ArchivosService()
# palabras_service = PalabrasService()

def index():
    return render_template('palabras.html', url_base=os.getenv("URL_BASE"))

# def listar():
#     palabras = palabras_service.listar_palabras() 
#     return render_template('listar_palabras.html', url_base=os.getenv("URL_BASE"), palabras=palabras)

# def diccionario():
#     respuesta = ResponseModel(200, 'Tarea realizada correctamente')
#     palabras = palabras_service.diccionario()
#     respuesta.data = palabras
#     return make_response(jsonify(respuesta.__dict__), respuesta.status)

