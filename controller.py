from model import Model
from view import View

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.controller = self

#_________________________Função-Adicionar________________________________
    
    def adicionar_produto(self, produto):
        self.model.adicionar_produto(produto)
        self.view.atualizar(self.model.obter_produtos())
        self.view.limpar()

    
 #_________________________Função-Excluir________________________________
     
    def excluir(self, produto):
        self.model.excluir(produto)
        self.view.atualizar(self.model.obter_produtos())
        self.view.limpar()

#_________________________Função-Editar________________________________
     
    def editar(self, produto):
        self.model.editar(produto)
        self.view.atualizar(self.model.obter_produtos())
        self.view.limpar()

#_________________________Função-Pesquisar________________________________
    def pesquisar_produtos(self, termo_pesquisa):
        produtos = self.model.pesquisar(termo_pesquisa)
        self.view.atualizar(produtos)
    
    

if __name__ == "__main__":
    import tkinter as tk
    root = tk.Tk()
    model = Model()
    view = View(root, Controller)
    controller = Controller(model, view)
    view.atualizar(model.obter_produtos())
    root.mainloop()