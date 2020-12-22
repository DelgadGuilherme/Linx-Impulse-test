from flask import render_template, request
from application import app 
import json
from application.model.entity.produto import Produto


@app.route('/')
@app.route('/home')
def home():
  with open('C:\\Users\\PICHAU\\Desktop\\Faculdade 4\\Tassio\\P2\\Prova\\Linx-Impulse-test\\application\\view\\static\\json\\products.json') as product_file:
    product_list = json.load(product_file)

  lista_produtos = []
  for product in product_list:
    lista_produtos.append(Produto(product['id'], product['name'], product['image'],product['oldPrice'],product['price'],product['description'],product['installments']['count'],product['installments']['value']))

  return render_template('index.html',  lista_produtos= lista_produtos)
    