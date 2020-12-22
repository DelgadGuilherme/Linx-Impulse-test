from flask import render_template, request
from application import app 
import json



@app.route('/')
@app.route('/home')
def home():
  with open('C:\\Users\\PICHAU\\Desktop\\Faculdade 4\\Tassio\\P2\\Prova\\Linx-Impulse-test\\application\\view\\static\\json\\products.json') as product_file:
    product_list = json.load(product_file)

  for product in product_list:
    print(product['name'])

  return render_template('index.html')
    