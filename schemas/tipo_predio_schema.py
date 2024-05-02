from utils.ma import ma
from marshmallow import fields


class TipoPredioSchema(ma.Schema):
    id_tipo_predio=fields.Integer()
    nomre_predio=fields.Sting()

tipo