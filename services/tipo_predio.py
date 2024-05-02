from flask import Blueprint, request, jsonify # importa la clase Blueprint para crear un blueprint, request para manejar las solicitudes HTTP y jsonify para devolver respuestas JSON
from model.tipo_predio import TipoPredio
from utils.db import db # importa la instancia de la clase SQLAlchemy para interactuar con la base de datos

tipopredios= Blueprint('tipopredios', __name__) # crea un blueprint con el nombre 'contacts' para agrupar las rutas relacionadas con los contactos

@tipopredios.route('/tipopredios/v1', methods=['GET']) # decorador que indica la ruta y los métodos HTTP permitidos
# ruta para imprimir un mensaje
def get_Mensaje():
    result = {}
    result['data'] = 'Aprendiendo_Flask - Predios'
    return jsonify(result)

@tipopredios.route('/tipopredios/v1/listar', methods=['GET'])
# ruta para listar los predios
def get_TipoPredio():
    result = {}
    tipopredios = TipoPredio.query.all()
    result['data'] = tipopredios
    result['status_code'] = 200
    result['msg'] = "Se recuperó los tipos de predios sin inconvenientes"
    return jsonify(result), 200

@tipopredios.route('/tipopredios/v1/insert', methods=['POST'])
# ruta para insertar un predio
def insert_TipoPredio():
    result = {}
    body = request.get_json()
    nomre_predio = body.get('nomre_predio')

    if not nomre_predio:
        return jsonify({'error': 'nomre_predios'}), 400
    
    tipo_predio = TipoPredio(nomre_predio=nomre_predio)
    db.session.add(tipo_predio)
    db.session.commit()
    result['data'] = tipo_predio
    result['status_code'] = 201
    result['msg'] = "Se insertó el tipo de predio sin inconvenientes"
    return jsonify(result), 201

@tipopredios.route('/tipopredios/v1/update', methods=['POST'])
# ruta para actualizar un predio
def update_TipoPredio():
    result = {}
    body = request.get_json()
    id_tipo_predio = body.get('id_tipo_predio')
    nomre_predio = body.get('nomre_predio')


    if not id_tipo_predio or not nomre_predio:
        return jsonify({'error': 'id_tipo_predio and nomre_predio son campos requeridos'}), 400
    
    tipo_predio = TipoPredio.query.get(id_tipo_predio)

    if tipo_predio is None:
        return jsonify({'error': f'El tipo de predio con ID: {id_tipo_predio} no existe'}), 404

    tipo_predio.nomre_predio = nomre_predio

    db.session.commit()
    result['data'] = tipo_predio
    result['status_code'] = 200
    result['msg'] = "Se actualizó el predio sin inconvenientes"
    return jsonify(result), 200

@tipopredios.route('/tipopredios/v1/delete', methods=['DELETE'])
# ruta para eliminar un predio
def delete_TipoPredio():
    result = {}
    body = request.get_json()
    id_tipo_predio = body.get('id_tipo_predio')

    if id_tipo_predio is None:
        return jsonify({'error': 'El ID es un campo requerido'}), 400
    
    tipo_predio = TipoPredio.query.get(id_tipo_predio)

    if tipo_predio is None:
        return jsonify({'error': f'El predio con ID: {id_tipo_predio} no existe'}), 404

    db.session.delete(tipo_predio)
    db.session.commit()
    result['data'] = tipo_predio
    result['status_code'] = 200
    result['msg'] = "Se eliminó el predio sin inconvenientes"
    return jsonify(result), 200 # devuelve un mensaje de éxito si se ha eliminado el predio sin problemas