from model import Model
from view import View

class Controller():
    def __init__(self) -> None:
        self.model = Model()
        self.view = View()
    def variaveis(self, nome,quantidade,preco,descricao):
        self.model.nome = nome
        self.model.quantidade = quantidade
        self.model.preco = preco
        self.model.descricao = descricao
        self.model.limpar()
        self.model.variaveis()
        




