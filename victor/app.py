# pip install flask
# pip install Flask-SQLAlchemy
# pip install Flask-Migrate
# pip install Flask-Script
# pip install pymysql
# flask db init
# flask db migrate -m "Migração Inicial"
# lask db upgradef

from flask import Flask, render_template, request, flash, redirect, Blueprint
app = Flask(__name__)
app.config['SECRET_KEY'] = 'SNF37Y7dzbfbhFDSBFdzfhKEUdhdf'
from database import db
from flask_migrate import Migrate
from models import Usuario, Pizza, Pedido
conexao = "mysql+pymysql://alunos:cefetmg@127.0.0.1/Victor"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)

from modulos.usuarios.usuarios import bp_usuario
app.register_blueprint( bp_usuario, url_prefix="/usuarios")

from modulos.pedidos.pedido import bp_pedidos
app.register_blueprint( bp_pedidos, url_prefix="/pedidos")

