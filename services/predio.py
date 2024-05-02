from flask import Blueprint, request, jsonify # importa la clase Blueprint para crear un blueprint, request para manejar las solicitudes HTTP y jsonify para devolver respuestas JSON
from model.predio import Predio
from utils.db import db # importa la instancia de la clase SQLAlchemy para interactuar con la base de datos

predios = Blueprint('predios', __name__) # crea un blueprint con el nombre 'contacts' para agrupar las rutas relacionadas con los contactos

@predios.route('/predios/v1', methods=['GET']) # decorador que indica la ruta y los métodos HTTP permitidos
# ruta para imprimir un mensaje
def get_Mensaje():
    result = {}
    result['data'] = 'Aprendiendo_Flask - Predios'
    return jsonify(result)

@predios.route('/predios/v1/listar', methods=['GET'])
# ruta para listar los predios
def get_Predios():
    result = {}
    predios = Predio.query.all()
    result['data'] = predios
    result['status_code'] = 200
    result['msg'] = "Se recuperó los predios sin inconvenientes"
    return jsonify(result), 200

@predios.route('/predios/v1/insert', methods=['POST'])
# ruta para insertar un predio
def insert_Predios():
    result = {}
    body = request.get_json()
    id_tipo_predio = body.get('id_tipo_predio')
    descripcion = body.get('descripcion')
    ruc = body.get('ruc')
    telefono = body.get('telefono')
    correo = body.get('correo')
    direccion = body.get('direccion')
    idubigeo = body.get('idubigeo')

    if not id_tipo_predio or not descripcion or not ruc or not telefono or not correo or not direccion or not idubigeo:
        return jsonify({'error': 'id_tipo_predio, descripcion, ruc, telefono, correo, direccion, and idubigeo son campos requeridos'}), 400
    
    predio = Predio(id_tipo_predio=id_tipo_predio, descripcion=descripcion, ruc=ruc, telefono=telefono, correo=correo, direccion=direccion, idubigeo=idubigeo)
    db.session.add(predio)
    db.session.commit()
    result['data'] = predio
    result['status_code'] = 201
    result['msg'] = "Se insertó el predio sin inconvenientes"
    return jsonify(result), 201

@predios.route('/predios/v1/update', methods=['POST'])
# ruta para actualizar un predio
def update_Predios():
    result = {}
    body = request.get_json()
    id_predio = body.get('id_predio')
    id_tipo_predio = body.get('id_tipo_predio')
    descripcion = body.get('descripcion')
    ruc = body.get('ruc')
    telefono = body.get('telefono')
    correo = body.get('correo')
    direccion = body.get('direccion')
    idubigeo = body.get('idubigeo')

    if not id_predio or not id_tipo_predio or not descripcion or not ruc or not telefono or not correo or not direccion or not idubigeo:
        return jsonify({'error': 'id_predio, id_tipo_predio, descripcion, ruc, telefono, correo, direccion, and idubigeo son campos requeridos'}), 400
    
    predio = Predio.query.get(id_predio)

    if predio is None:
        return jsonify({'error': f'El predio con ID: {id_predio} no existe'}), 404

    predio.id_tipo_predio = id_tipo_predio
    predio.descripcion = descripcion
    predio.ruc = ruc
    predio.telefono = telefono
    predio.correo = correo
    predio.direccion = direccion
    predio.idubigeo = idubigeo

    db.session.commit()
    result['data'] = predio
    result['status_code'] = 200
    result['msg'] = "Se actualizó el predio sin inconvenientes"
    return jsonify(result), 200

@predios.route('/predios/v1/delete', methods=['DELETE'])
# ruta para eliminar un predio
def delete_Predios():
    result = {}
    body = request.get_json()
    id_predio = body.get('id_predio')

    if id_predio is None:
        return jsonify({'error': 'El ID es un campo requerido'}), 400
    
    predio = Predio.query.get(id_predio)

    if predio is None:
        return jsonify({'error': f'El predio con ID: {id_predio} no existe'}), 404

    db.session.delete(predio)
    db.session.commit()
    result['data'] = predio
    result['status_code'] = 200
    result['msg'] = "Se eliminó el predio sin inconvenientes"
    return jsonify(result), 200 # devuelve un mensaje de éxito si se ha eliminado el predio sin problemas