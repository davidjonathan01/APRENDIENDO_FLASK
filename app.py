from flask import Flask
from config import DATABASE_CONNECTION
from utils.db import db
from services.contact import contacts
from services.predio import predios

app = Flask(__name__) # crea una instancia de la clase Flask
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION # establece la cadena de conexión a la base de datos
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # deshabilita el seguimiento de modificaciones

db.init_app(app) # inicializa la base de datos
app.register_blueprint(contacts) # registra el blueprint en la aplicación
app.register_blueprint(predios) # registra el blueprint en la aplicación
# el blueprint es una forma de organizar y reutilizar código en una aplicación de Flask que actualiza o extiende la aplicación principal

with app.app_context(): # crea un contexto de aplicación
    db.create_all() # crea las tablas en la base de datos si no existen

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000) # inicia la aplicación en el puerto 5000 y habilita el modo de depuración para mostrar errores