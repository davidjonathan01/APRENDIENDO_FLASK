from utils.db import db # importa la instancia de la clase SQLAlchemy para interactuar con la base de datos
from dataclasses import dataclass # importa el decorador dataclass para crear una clase de datos

@dataclass # decorador que convierte la clase en una clase de datos
# una clase de datos es una clase que principalmente contiene datos y no tiene métodos
class Predio(db.Model):
    id_predio: int
    id_tipo_predio: int
    descripcion: str
    ruc: str
    telefono: str
    correo: str
    direccion: str
    idubigeo: str

    id_predio = db.Column(db.Integer, primary_key=True) # crea una columna de tipo entero que es la clave primaria
    id_tipo_predio = db.Column(db.Integer)
    descripcion = db.Column(db.String(100))
    ruc = db.Column(db.String(20))
    telefono = db.Column(db.String(10))
    correo = db.Column(db.String(80))
    direccion = db.Column(db.String(100))
    idubigeo = db.Column(db.String(6))

    # crea un constructor de la clase
    def __init__(self, id_tipo_predio, descripcion, ruc, telefono, correo, direccion, idubigeo):
        self.id_tipo_predio = id_tipo_predio
        self.descripcion = descripcion
        self.ruc = ruc
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion
        self.idubigeo = idubigeo