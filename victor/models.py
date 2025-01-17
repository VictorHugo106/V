from database import db

class Usuario(db.Model):
    __tablename__="usuario"
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    email = db.Column(db.String(100))
    senha = db.Column(db.String(200))

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

    def __repr__(self):
        return "<Usuario {}>".format(self.nome)
    
class Pizza(db.Model):
    __tablename__="pizza"
    id = db.Column(db.Integer, primary_key = True)
    sabor = db.Column(db.String(100))
    ingredientes = db.Column(db.String(100))
    preço = db.Column(db.Float)

    def __init__(self, sabor, ingredientes, preço):
        self.sabor = sabor
        self.ingredientes = ingredientes
        self.preço = preço

    def __repr__(self):
        return "<Pizza {}>".format(self.sabor)
    
class Pedido(db.Model):
    __tablename__="pedido"
    id = db.Column(db.Integer, primary_key = True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'))
    data = db.Column(db.Date)
    
    usuario = db.relationship('Usuario', foreign_keys=usuario_id)
    pizza = db.relationship('Pizza', foreign_keys=pizza_id)

    def __init__(self, usuario_id, data, pizza_id):
        self.usuario_id = usuario_id

    def __repr__(self):
        return "<Pedido {} - {} - {}>".format(self.usuario.name, self.pizza.sabor, self.date)

