from queue import Full
from tkinter import *
from tkinter import ttk
import pymongo

co0 = "#545454" #cinza
co1 = "#d9d9d9" #cinza
co2 = "#2c2c2c" #black
co3 = '#ffffff' #branco
co4 = "#3f7a3e" #verde-escuro

janela = Tk()
class View():
    def __init__(self):
        
        self.janela = janela
        self.tela()
        self.frames()
        self.widgets_Cabecalho()
        self.widgets_conteudo()
        self.widgets_conteudo1()
        self.widgets_Rodape()
        
        janela.mainloop()

#_________________________Tela________________________________

    def tela(self):

        self.janela.title('')
        self.janela.overrideredirect(True)
        self.janela.configure(background=co1)
        self.janela.geometry("{0}x{1}+0+0".format(janela.winfo_screenwidth(), janela.winfo_screenheight()))
        self.janela.resizable(width=False, height=False)

#_________________________Frames________________________________

    def frames(self):

        self.frame_cabecalho = Frame(self.janela, bg=co2)
        self.frame_cabecalho.place(relx=0, rely=0, relwidth=1, relheight=0.15)
        
        self.frame_conteudo= Frame(self.janela, bg=co0)
        self.frame_conteudo.place(relx=0, rely=0.15, relwidth=0.5, relheight=0.75)

        self.frame_conteudo1= Frame(self.janela, bg=co0)
        self.frame_conteudo1.place(relx=0.5, rely=0.15, relwidth=0.5, relheight=0.75)

        self.frame_rodape = Frame(self.janela, bg=co2)
        self.frame_rodape.place(relx=0, rely=0.9, relwidth=1, relheight=0.10)

#_________________________Cabecalho________________________________

    def widgets_Cabecalho(self):

        self.logo = Label(self.frame_cabecalho, text='Cadastro de Produtos', anchor="center", font=('arial 20 bold'), bg=co2, fg=co3)
        self.logo.place(relx=0.4, rely=0.3)

        def Sair(): self.janela.destroy()

        self.bt_sair = Button(self.frame_cabecalho, text='Sair', anchor="center", font=('arial 12 bold'), bg=co4, fg=co3, border=0,activebackground=co2,activeforeground= co3, command=Sair) 
        self.bt_sair.place(relx=0.9, rely=0.4, relwidth=0.07,relheight=0.4)



#_________________________Conteudo________________________________

    def widgets_conteudo(self):

        #_________________________STYLE-TREEVIEW________________________________

        style = ttk.Style()

        style.theme_use("default")

        style.configure("Treeview.Heading",background=co2,foreground=co3,padding=10, font=('arial 10 bold'))
        style.map("Treeview.Heading", background=[('active', co4)])
        
        style.configure("Treeview",background=co3,foreground=co2,rowheight=45)
        style.map("Treeview",background=[('selected', co4)])

        #_________________________TREEVIEW________________________________

        self.tv = ttk.Treeview(self.frame_conteudo1, height= 3 ,columns=('nome','QNT','precos', 'Descricao'),show='headings',)
        
        self.tv.column('nome', width=100, anchor= CENTER)
        self.tv.heading('nome',text="Nome", anchor= CENTER)

        self.tv.column('QNT', width=50, anchor= CENTER)
        self.tv.heading('QNT',text="QNT", anchor= CENTER)

        self.tv.column('precos', width=50, anchor= CENTER)
        self.tv.heading('precos',text="precos", anchor= CENTER)

        self.tv.column('Descricao', width=200, anchor= CENTER)
        self.tv.heading('Descricao',text="Descricao", anchor= CENTER)

        self.tv.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.7)
        
        #_________________________SCROLLBAR________________________________

        self.tv_scrol = Scrollbar(self.frame_conteudo1, orient='vertical')
        self.tv.configure(yscroll= self.tv_scrol.set)
        self.tv_scrol.place(relx=0.89, rely=0.1, relwidth=0.04, relheight=0.7)

        self.tv.bind("<Double-1>", self.espelho)

        self.bt_mostra = Button(self.frame_conteudo1, text='Mostra Tudo', anchor="center", font=('arial 12 bold'), bg=co4, fg=co3, border=0,activebackground=co2,activeforeground= co3, command= self.select_usuario) 
        self.bt_mostra.place(relx=0.72, rely=0.85, relwidth=0.2,relheight=0.09)

#_________________________Conteudo-1________________________________

    def widgets_conteudo1(self):

        #_________________________LABEL________________________________
        
        self.lb_nome = Label(self.frame_conteudo, font=('arial 12 bold'), bg=co0, fg=co3, anchor= W, text='Nome do produto:')
        self.lb_nome.place(relx=0.1, rely=0.3, relwidth=0.3,relheight=0.09)

        self.lb_QNT = Label(self.frame_conteudo, font=('arial 12 bold'), bg=co0, fg=co3, anchor= W, text='Quantidade:')
        self.lb_QNT.place(relx=0.43, rely=0.3, relwidth=0.3,relheight=0.09)

        self.lb_preco = Label(self.frame_conteudo, font=('arial 12 bold'), bg=co0, fg=co3, anchor= W, text='Preço:')
        self.lb_preco.place(relx=0.64, rely=0.3, relwidth=0.3,relheight=0.09)

        self.lb_Descricao = Label(self.frame_conteudo, font=('arial 12 bold'), bg=co0, fg=co3, anchor= W, text='Descrição do produto:')
        self.lb_Descricao.place(relx=0.1, rely=0.5, relwidth=0.3,relheight=0.09)

        #_________________________ENTRY________________________________

        self.entry_busca = Entry(self.frame_conteudo, font=('arial 12'), border=1, justify=CENTER, bg=co3, fg=co2)
        self.entry_busca.place(relx=0.26, rely=0.1, relwidth=0.6,relheight=0.09)

        self.entry_nome = Entry(self.frame_conteudo, font=('arial 12'), border=1, justify=CENTER, bg=co3, fg=co2)
        self.entry_nome.place(relx=0.1, rely=0.4, relwidth=0.3,relheight=0.09)

        self.entry_QNT = Entry(self.frame_conteudo, font=('arial 12'), border=1, justify=CENTER, bg=co3, fg=co2)
        self.entry_QNT.place(relx=0.47, rely=0.4, relwidth=0.08,relheight=0.09)

        self.entry_preco = Entry(self.frame_conteudo, font=('arial 12'), border=1, justify=CENTER, bg=co3, fg=co2)
        self.entry_preco.place(relx=0.65, rely=0.4, relwidth=0.08,relheight=0.09)

        self.entry_Descricao = Entry(self.frame_conteudo, font=('arial 12'), border=1, justify= CENTER, bg=co3, fg=co2)
        self.entry_Descricao.place(relx=0.1, rely=0.6, relwidth=0.8,relheight=0.09)

        #_________________________BUTTON________________________________

        self.bt_buscar = Button(self.frame_conteudo, text='Buscar', anchor="center", font=('arial 12 bold'), bg=co4, fg=co3, border=0,activebackground=co2,activeforeground= co3, command= self.busca) 
        self.bt_buscar.place(relx=0.1, rely=0.1, relwidth=0.15,relheight=0.09)


        self.bt_editar = Button(self.frame_conteudo, text='Editar', anchor="center", font=('arial 12 bold'), bg=co4, fg=co3, border=0,activebackground=co2,activeforeground= co3, command= self.editar) 
        self.bt_editar.place(relx=0.1, rely=0.8, relwidth=0.15,relheight=0.09)

        self.bt_adicionar = Button(self.frame_conteudo, text='Adicionar', anchor="center", font=('arial 12 bold'), bg=co4, fg=co3, border=0,activebackground=co2,activeforeground= co3, command= self.tabela) 
        self.bt_adicionar.place(relx=0.27, rely=0.8, relwidth=0.15,relheight=0.09)

        self.bt_excluir = Button(self.frame_conteudo, text='Excluir', anchor="center", font=('arial 12 bold'), bg=co4, fg=co3, border=0,activebackground=co2,activeforeground= co3, command=self.deletar)
        self.bt_excluir.place(relx=0.44, rely=0.8, relwidth=0.15,relheight=0.09)
#_________________________Rodape________________________________    

    def widgets_Rodape(self):

        self.contato = Label(self.frame_rodape, text='Contato: andrenimer123@gmail.com', font=('arial 12 bold'), bg=co2, fg=co3)
        self.contato.place(relx=0.4, rely=0.3)
View()