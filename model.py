import pymongo

class Model():
    def __init__(self, nome,quantidade,preco,descricao):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco
        self.descricao = descricao

    def limpar(self):
        self.entry_nome.delete(0, END)
        self.entry_nota.delete(0, END)
        self.entry_falta.delete(0, END)
        self.entry_obs.delete(0, END)
        self.entry_busca.delete(0, END)

    def conecta_bd(self):
        
        self.collection = pymongo.MongoClient('localhost', 27017)['my_database']['my_collection']


    def variaveis(self):
        self.nome = self.entry_nome.get()
        self.nota = self.entry_nota.get()
        self.falta = self.entry_falta.get()
        self.obs = self.entry_obs.get()
        self.buscar = self.entry_busca.get()
    
    def select_usuario(self):
        self.tv.delete(*self.tv.get_children())
        self.conecta_bd()

        self.rows = list(self.collection.find({},{ "_id": 0,}))
        for x in self.rows:
            self.tv.insert("",'end',values=list(x.values()))

    def espelho(self, event):
        self.limpar()
        self.tv.selection()

        for n in self.tv.selection():

            nome, nota, falta, observacao = self.tv.item(n, 'values')

            self.entry_nome.insert(END, nome)
            self.entry_nota.insert(END, nota)
            self.entry_falta.insert(END, falta)
            self.entry_obs.insert(END, observacao)

    def tabela(self):
        self.variaveis()
        self.conecta_bd()
        self.usuario = {'nome': self.nome, 'nota': self.nota,'falta':self.falta, 'observacao': self.obs}
             
        self.collection.insert_one(self.usuario)
        self.select_usuario()
        self.collection.delete_one({'nome' : ""})
        self.limpar()

    def deletar(self):
        self.variaveis()
        self.conecta_bd()
        self.collection.delete_one({'nome' : self.nome})
        self.limpar()
        self.select_usuario()

    def editar(self):
        self.variaveis()
        self.consulta = {'nome': self.nome}
        self.collection.update_one(self.consulta,{'$set':{'nota' : self.nota, 'falta' : self.falta, 'observacao' : self.obs}})
        self.select_usuario()
        self.limpar()

    def busca(self):
        self.conecta_bd()
        self.tv.delete(*self.tv.get_children())
        
        self.rows = list(self.collection.find({'nome': self.buscar},{ "_id": 0,"nome": 1, "nota": 1,"falta": 1,"observacao": 1,}))
        for x in self.rows:
            self.tv.insert("",'end',values=list(x.values()))