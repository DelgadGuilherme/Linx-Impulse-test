from flask import render_template, request
from application import app 
import json
from application.model.dao.produto_dao import ProdutoDAO


@app.route('/')
@app.route('/home')
def home():
  produto_dao = ProdutoDAO()
  lista_produtos = produto_dao.listarProduto()
  return render_template('index.html',  lista_produtos= lista_produtos)


@app.route('/home/participar', methods=['POST'])
def participar():
    return render_template('email.html', 201, {'content-type': "text/html"})
    