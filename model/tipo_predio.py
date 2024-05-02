from utils.db import db # importa la instancia de la clase SQLAlchemy para interactuar con la base de datos
from dataclasses import dataclass # importa el decorador dataclass para crear una clase de datos

@dataclass # decorador que convierte la clase en una clase de datos
# una clase de datos es una clase que principalmente contiene datos y no tiene métodos
class TipoPredio(db.Model):
    id_tipo_predio: int
    nomre_predio: str
 

    id_tipo_predio = db.Column(db.Integer, primary_key=True)
    nomre_predio=db.Column(db.String(100))


    # crea un constructor de la clase
    def __init__(self, nomre_predio):
        self.nomre_predio = nomre_predio