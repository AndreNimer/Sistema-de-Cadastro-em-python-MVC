from tkinter import *
from tkinter import ttk

co0 = "#ffffff" #cinza
co1 = "#d9d9d9" #cinza
co2 = "#2c2c2c" #black
co3 = '#000000' #branco
co4 = "#3f7a3e" #verde-escuro
class Produto:
    def __init__(self, nome, preco, descricao, quantidade):

        self.nome = nome
        self.preco = preco
        self.descricao = descricao
        self.quantidade = quantidade

class View:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.tela()
        self.frames()
        self.widgets_conteudo()
        self.widgets_conteudo1()
        
#_________________________Tela________________________________

    def tela(self):

        self.root.title("Cadastro de Produtos")
        self.root.configure(background=co0)
        self.root.geometry('1200x600')
        self.root.resizable(width=False, height=False)
        

#_________________________Frames________________________________

    def frames(self):

        self.frame_conteudo= Frame(self.root, highlightbackground= co3, highlightthickness=3, bg= co0)
        self.frame_conteudo.place(relx=0.03, rely=0.05, relwidth=0.45, relheight=0.75)

        self.frame_conteudo1= Frame(self.root, highlightbackground=co3, highlightthickness=3, bg= co0)
        self.frame_conteudo1.place(relx=0.52, rely=0.05, relwidth=0.45, relheight=0.75)

#_________________________Conteudo________________________________

    def widgets_conteudo(self):

        #_________________________LABEL________________________________
        
        self.label_nome = Label(self.frame_conteudo, font=('arial 12 bold'), bg=co0, fg=co3, anchor= W, text='Nome do produto:')
        self.label_nome.place(relx=0.1, rely=0.2, relwidth=0.3,relheight=0.09)

        self.label_preco = Label(self.frame_conteudo, font=('arial 12 bold'), bg=co0, fg=co3, anchor= W, text="Preço:")
        self.label_preco.place(relx=0.1, rely=0.4, relwidth=0.3,relheight=0.09)

        self.label_descricao = Label(self.frame_conteudo, font=('arial 12 bold'), bg=co0, fg=co3, anchor= W, text="Descrição:")
        self.label_descricao.place(relx=0.1, rely=0.6, relwidth=0.3,relheight=0.09)
        
        self.label_quantidade = Label(self.frame_conteudo, font=('arial 12 bold'), bg=co0, fg=co3, anchor= W, text="Quantidade:")
        self.label_quantidade.place(relx=0.4, rely=0.4, relwidth=0.3,relheight=0.09)

        #_________________________ENTRY________________________________
        self.entry_busca = Entry(self.frame_conteudo, font=('arial 12'), border=1, relief="solid", justify=CENTER, bg=co0, fg=co2)
        self.entry_busca.place(relx=0.25, rely=0.1, relwidth=0.6,relheight=0.09)

        self.entry_nome = Entry(self.frame_conteudo, font=('arial 12'), border=1, relief="solid", justify=LEFT, bg=co0, fg=co2)
        self.entry_nome.place(relx=0.1, rely=0.3, relwidth=0.7,relheight=0.09)

        self.entry_preco = Entry(self.frame_conteudo, font=('arial 12'), border=1, relief="solid", justify=CENTER, bg=co0, fg=co2)
        self.entry_preco.place(relx=0.1, rely=0.5, relwidth=0.25,relheight=0.09)
        
        self.entry_descricao = Text(self.frame_conteudo, font=('arial 12'), border=1, relief="solid", bg=co0, fg=co2)
        self.entry_descricao.place(relx=0.1, rely=0.7, relwidth=0.7,relheight=0.2)
        #_________________________SCROLLBAR________________________________
         
        self.descricao_scroll = Scrollbar(self.frame_conteudo, orient='vertical')
        self.entry_descricao.configure(yscroll= self.descricao_scroll.set)
        self.descricao_scroll.place(relx=0.79, rely=0.7, relwidth=0.04, relheight=0.2)

        self.entry_quantidade = Entry(self.frame_conteudo, font=('arial 12'), border=1, relief="solid", justify= CENTER, bg=co0, fg=co2)
        self.entry_quantidade.place(relx=0.4, rely=0.5, relwidth=0.15,relheight=0.09)

        #_________________________BUTTON________________________________
        self.bt_buscar = Button(self.frame_conteudo, text='Buscar', anchor="center", font=('arial 12 bold'), bg=co3, fg=co0, border=0,activebackground=co0,activeforeground= co3, command= self.pesquisar) 
        self.bt_buscar.place(relx=0.1, rely=0.1, relwidth=0.15,relheight=0.09)

        self.button_cadastrar = Button(self.root, text='Adicionar', anchor="center", font=('arial 12 bold'), bg=co0, fg=co3, border=2,relief="solid",activebackground=co3,activeforeground= co0,highlightbackground= co3, command=self.cadastrar)
        self.button_cadastrar.place(relx=0.05, rely=0.85, relwidth=0.1,relheight=0.08)

        self.button_excluir = Button(self.root, text='Excluir', anchor="center", font=('arial 12 bold'), bg=co0, fg=co3, border=2,relief="solid",activebackground=co3,activeforeground= co0,highlightbackground= co3, command=self.excluir)
        self.button_excluir.place(relx=0.20, rely=0.85, relwidth=0.1,relheight=0.08)

        self.button_editar = Button(self.root, text='Editar', anchor="center", font=('arial 12 bold'), bg=co0, fg=co3, border=2,relief="solid",activebackground=co3,activeforeground= co0,highlightbackground= co3, command=self.editar)
        self.button_editar.place(relx=0.35, rely=0.85, relwidth=0.1,relheight=0.08)

#_________________________Conteudo-1________________________________

    def widgets_conteudo1(self):

        #_________________________STYLE-TREEVIEW_______________________________
        style = ttk.Style()

        style.theme_use("default")

        style.configure("Treeview.Heading",background=co3,foreground=co0,padding=10, font=('arial 10 bold'))
        style.map("Treeview.Heading", background=[('active', co0)], foreground= [('active',co3)])
        
        style.configure("Treeview",background=co0,foreground=co3,rowheight=45,)
        style.map("Treeview",background=[('selected', co3)],foreground=[('selected', co0)])

        #_________________________TREEVIEW________________________________
        self.tv = ttk.Treeview(self.frame_conteudo1, height= 3 ,columns=('id','nome','precos', 'descricao', 'QNT'),show='headings')

        self.tv.column('id', width=150, anchor= CENTER)
        self.tv.heading('id',text="ID", anchor= CENTER)

        self.tv.column('nome', width=100, anchor= CENTER)
        self.tv.heading('nome',text="Nome", anchor= CENTER)

        self.tv.column('precos', width=80, anchor= CENTER)
        self.tv.heading('precos',text="Precos", anchor= CENTER)

        self.tv.column('descricao', width=100, anchor= CENTER)
        self.tv.heading('descricao',text="Descricao", anchor= CENTER)

        self.tv.column('QNT', width=50, anchor= CENTER)
        self.tv.heading('QNT',text="QNT", anchor= CENTER)

        self.tv.place(relx=0, rely=0, relwidth=0.96, relheight=1.002)
        
        #_________________________SCROLLBAR________________________________
        
        self.tv_scrol = Scrollbar(self.frame_conteudo1, orient='vertical')
        self.tv.configure(yscroll= self.tv_scrol.set)
        self.tv_scrol.place(relx=0.96, rely=0, relwidth=0.04, relheight=1)

        self.tv.bind("<<TreeviewSelect>>", self.selecionar)
        
#_________________________Funções________________________________

    #_________________________Função-Treeview________________________________

    def atualizar(self, produtos): 
        self.tv.delete(*self.tv.get_children())
        for produto in produtos:
            self.tv.insert("", "end", values=(produto["_id"], produto["nome"], produto["preco"], produto["quantidade"], produto["descricao"]))
    
    #_________________________Função-limpar________________________________

    def limpar(self):

        self.entry_nome.delete(0, END)
        self.entry_preco.delete(0, END) 
        self.entry_quantidade.delete(0, END)
        self.entry_descricao.delete("1.0", END)

    #_________________________Função-Selecionar________________________________   

    def selecionar(self, event):
        self.limpar()
        self.tv.selection()

        for n in self.tv.selection():

            id, nome, preco, descricao, quantidade = self.tv.item(n, 'values')

            self.entry_nome.insert(END, nome)
            self.entry_preco.insert(END, preco)
            self.entry_descricao.insert(END, descricao)
            self.entry_quantidade.insert(END, quantidade)

    #_________________________Função-Cadastrar________________________________

    def cadastrar(self):

        nome = self.entry_nome.get()
        preco = float(self.entry_preco.get())
        quantidade = int(self.entry_quantidade.get())
        descricao = self.entry_descricao.get("1.0", "end-1c")
        produto = Produto(nome, preco, quantidade, descricao,)
        self.controller.adicionar_produto(produto)

    #_________________________Função-Excluir________________________________

    def excluir(self):
        item_selecionado = self.tv.selection()
        if item_selecionado:
            nome = self.entry_nome.get()
            self.controller.excluir(nome)

    #_________________________Função-Editar________________________________

    def editar(self):
        nome = self.entry_nome.get()
        preco = float(self.entry_preco.get())
        quantidade = int(self.entry_quantidade.get())
        descricao = self.entry_descricao.get("1.0", "end-1c")
        produto = Produto(nome, preco, quantidade, descricao,)

        item_selecionado = self.tv.selection()
        if item_selecionado:
            id = self.tv.item(item_selecionado)["text"]
            self.controller.editar(produto)

    #_________________________Função-Pesquisar________________________________

    def pesquisar(self):
        termo_pesquisa = self.entry_busca.get()
        self.controller.pesquisar_produtos(termo_pesquisa)


