from database import db
from flask_migrate import Migrate
from models import Usuario, Pizza, Pedido
from flask import Blueprint
bp_pizza = Blueprint('pizzas', __name__, template_folder='templates')

@bp_pizza.route('/')
def init():
    dados = pizza.query.all()
    return render_template('pizza.html', dados=dados)

@bp_pizza.route('/add')
def add():
    return render_template('pizza_add.html')

@bp_pizza.route('/save', methods=['POST'])
def save():
    sabor = request.form.get('sabor')
    ingredientes = request.form.get('ingredientes')
    preço = request.form.get('preço')
    if sabor and ingredientes and preço:
        bp_pizza = Pizza(sabor, ingredientes, preço)
        db.session.add(bp_pizza)
        db.session.commit()
        flash('pizza salva com sucesso!')
        return redirect('/')
    else:
        flash('/Preencher todos os campos')
        return redirect('/add')
