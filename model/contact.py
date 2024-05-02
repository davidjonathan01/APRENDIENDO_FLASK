from utils.db import db # importa la instancia de la clase SQLAlchemy para interactuar con la base de datos
from dataclasses import dataclass # importa el decorador dataclass para crear una clase de datos

@dataclass # decorador que convierte la clase en una clase de datos
# una clase de datos es una clase que principalmente contiene datos y no tiene métodos
class Contact(db.Model):
    id: int
    fullname: str
    email: str
    phone: str

    id = db.Column(db.Integer, primary_key=True) # crea una columna de tipo entero que es la clave primaria
    fullname = db.Column(db.String(100)) # crea una columna de tipo cadena con una longitud máxima de 100 caracteres
    email = db.Column(db.String(60)) # crea una columna de tipo cadena con una longitud máxima de 60 caracteres
    phone = db.Column(db.String(20)) # crea una columna de tipo cadena con una longitud máxima de 20 caracteres

    # crea un constructor de la clase
    def __init__(self, fullname, email, phone):
        self.fullname = fullname
        self.email = email
        self.phone = phone