import json
from application.model.entity.produto import Produto
class ProdutoDAO:
    def __init__(self):
        self._lista_produtos = []
        self._product_list = []

    def lerJson(self):
        with open('C:\\Users\\PICHAU\\Desktop\\Faculdade 4\\Tassio\\P2\\Prova\\Linx-Impulse-test\\application\\view\\static\\json\\products.json') as product_file:
            self._product_list = json.load(product_file)
        return self._product_list

    def instanciarProduto(self):
        self.lerJson()
        for product in self._product_list:
           self._lista_produtos.append(Produto(product['id'], product['name'], product['image'],product['oldPrice'],product['price'],product['description'],product['installments']['count'],product['installments']['value']))

    def listarProduto(self):
        self.instanciarProduto()
        return self._lista_produtos