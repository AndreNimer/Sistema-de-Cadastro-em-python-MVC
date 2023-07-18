from bson.objectid import ObjectId
from pymongo import MongoClient

class Model:
    def __init__(self):

        self.client = MongoClient('mongodb://localhost:27017/')  
        self.db = self.client['cadastro_produtos']
        self.produtos = self.db['produtos']
    #_________________________Função-Adicionar________________________________

    def adicionar_produto(self, produto):

        produto_data = {'nome': produto.nome, 'preco': produto.preco, 'descricao': produto.descricao, 'quantidade': produto.quantidade}
        self.produtos.insert_one(produto_data)

    #_________________________Função-Obter________________________________

    def obter_produtos(self):
        return list(self.produtos.find({},{}))
    
    #_________________________Função-Excluir________________________________

    def excluir(self, nome):
        self.produtos.delete_one({'nome' : nome})

    #_________________________Função-Editar________________________________

    def editar(self, produto):
        self.consulta = {'nome': produto.nome}
        self.produtos.update_one(self.consulta,{"$set": {"preco": produto.preco, 'descricao': produto.descricao, 'quantidade': produto.quantidade}})
    
    #_________________________Função-Pesquisar________________________________

    def pesquisar(self, termo_pesquisa):
        Pesquisar = {}
    
        if ObjectId.is_valid(termo_pesquisa):
            Pesquisar['_id'] = ObjectId(termo_pesquisa)
        else:
            Pesquisar["$or"] = [
                {"nome": {"$regex": termo_pesquisa, "$options": "i"}},
            ]
        return list(self.produtos.find(Pesquisar, {}))


    