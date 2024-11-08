from database import db
from flask_migrate import Migrate
from models import Usuario, Pizza, Pedido
from flask import Blueprint
bp_pedidos = Blueprint('pedidos', __name__, template_folder='templates')