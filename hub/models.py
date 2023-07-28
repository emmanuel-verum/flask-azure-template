from hub.ext.database import db
from sqlalchemy_serializer import SerializerMixin


class Projetos(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(140))
    ativo = db.Column(db.Boolean)
    descricao = db.Column(db.Text)


class Usuarios(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(140))
    password = db.Column(db.String(512))
    email = db.Column(db.String(512))
    ativo = db.Column(db.Boolean)