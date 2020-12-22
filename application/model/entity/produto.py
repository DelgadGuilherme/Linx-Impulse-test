class Produto:
    def __init__(self, id, nome, image, preco_antigo, preco, descricao,parcela,valor_parcela):
        self._id = id
        self._nome = nome
        self._image = image
        self._preco_antigo = preco_antigo
        self._preco = preco
        self._descricao = descricao
        self._parcela = parcela
        self._valor_parcela = valor_parcela


    def get_nome(self):
        return self._nome

    def get_id(self):
        return self._id

    def get_image(self):
        return self._image

    def get_preco_antigo(self):
        return self._preco_antigo

    def get_preco(self):
        return self._preco

    def get_descricao(self):
        return self._descricao

    def get_parcela(self):
        return self._parcela

    def get_valor_parcela(self):
        return self._valor_parcela