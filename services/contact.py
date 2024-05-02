from flask import Blueprint, request, jsonify # importa la clase Blueprint para crear un blueprint, request para manejar las solicitudes HTTP y jsonify para devolver respuestas JSON
from model.contact import Contact
from utils.db import db # importa la instancia de la clase SQLAlchemy para interactuar con la base de datos

contacts = Blueprint('contacts', __name__) # crea un blueprint con el nombre 'contacts' para agrupar las rutas relacionadas con los contactos

@contacts.route('/contactos/v1', methods=['GET']) # decorador que indica la ruta y los métodos HTTP permitidos
# ruta para imprimir un mensaje
def get_Mensaje():
    result = {} # crea un diccionario vacío
    result['data'] = 'Aprendiendo_Flask' # agrega un mensaje al diccionario
    return jsonify(result) # devuelve el diccionario como una respuesta JSON

@contacts.route('/contactos/v1/listar', methods=['GET']) 
# ruta para listar los contactos
def get_Contactos():
    result = {} # crea un diccionario vacío
    contactos = Contact.query.all() # obtiene todos los contactos de la base de datos
    result['data'] = contactos # agrega los contactos al diccionario
    result['status_code'] = 200 # agrega un código de estado al diccionario
    result['msg'] = "Se recuperó los contactos sin inconvenientes" # agrega un mensaje al diccionario
    return jsonify(result), 200 # devuelve el diccionario como una respuesta JSON con un código de estado 200

@contacts.route('/contactos/v1/insert', methods=['POST']) # Se usa el método POST para insertar un contacto ya que se envía información al servidor
# ruta para insertar un contacto
def insert_Contactos():
    result = {}
    body = request.get_json() # obtiene los datos del cuerpo de la solicitud en formato JSON
    fullname = body.get('fullname') # obtiene el valor de la clave 'fullname' del cuerpo de la solicitud
    email = body.get('email') # obtiene el valor de la clave 'email' del cuerpo de la solicitud
    phone = body.get('phone') # obtiene el valor de la clave 'phone' del cuerpo de la solicitud

    if not fullname or not email or not phone:
        return jsonify({'error': 'fullname, email, and phone son campos requeridos'}), 400 # devuelve un mensaje de error si falta alguno de los campos requeridos
    
    contacto = Contact(fullname=fullname, email=email, phone=phone)
    db.session.add(contacto) # agrega el contacto a la sesión
    db.session.commit() # confirma los cambios en la base de datos
    result['data'] = contacto # agrega el contacto al diccionario
    result['status_code'] = 201 # 201 significa que se ha creado un nuevo recurso
    result['msg'] = "Se insertó el contacto sin inconvenientes"
    return jsonify(result), 201

@contacts.route('/contactos/v1/update', methods=['POST']) # Se usa el método POST para actualizar un contacto ya que se envía información al servidor
# ruta para actualizar un contacto
def update_Contactos():
    result = {}
    body = request.get_json() # obtiene los datos del cuerpo de la solicitud en formato JSON
    id = body.get('id') # obtiene el valor de la clave 'id' del cuerpo de la solicitud
    fullname = body.get('fullname') # obtiene el valor de la clave 'fullname' del cuerpo de la solicitud
    email = body.get('email') # obtiene el valor de la clave 'email' del cuerpo de la solicitud
    phone = body.get('phone') # obtiene el valor de la clave 'phone' del cuerpo de la solicitud

    if not id or not fullname or not email or not phone:
        return jsonify({'error': 'id, fullname, email, and phone son campos requeridos'}), 400
    
    contacto = Contact.query.get(id) # busca el contacto por su id

    if contacto is None:
        return jsonify({'error': f'El contacto con ID: {id} no existe'}), 404
    
    contacto.fullname = fullname # actualiza el nombre completo del contacto
    contacto.email = email # actualiza el correo electrónico del contacto
    contacto.phone = phone # actualiza el número de teléfono del contacto
    db.session.commit() # confirma los cambios en la base de datos

    result['data'] = contacto # agrega el contacto actualizado al diccionario
    result['status_code'] = 202 # 202 significa que se ha aceptado la solicitud pero aún no se ha procesado
    result['msg'] = "Se actualizó el contacto sin inconvenientes"
    return jsonify(result), 202

@contacts.route('/contactos/v1/delete', methods=['DELETE']) # Se usa el método DELETE para eliminar un contacto ya que se envía información al servidor
# ruta para eliminar un contacto
def delete_Contactos():
    result = {}
    body = request.get_json()
    id = body.get('id')

    if id is None:
        return jsonify({'error': 'El ID es un campo requerido'}), 400
    
    contacto = Contact.query.get(id)

    if contacto is None:
        return jsonify({'error': f'El contacto con ID: {id} no ha sido encontrado'}), 404
    
    db.session.delete(contacto) # elimina el contacto de la sesión
    db.session.commit() # confirma los cambios en la base de datos

    result['data'] = contacto # agrega el contacto eliminado al diccionario
    result['status_code'] = 200 # 200 significa que la solicitud se ha completado con éxito
    result['msg'] = "Se eliminó el contacto sin inconvenientes"

    return jsonify(result), 200 # devuelve el diccionario como una respuesta JSON con un código de estado 200