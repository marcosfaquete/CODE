from tkinter import *
from tkinter import ttk


root = Tk()

class Funcs():
    def __init__(self):
        self.codigo_entry = None
        self.nome_entry = None
        self.cidade_entry = None
        self.telefone_entry = None

    def limpa_tela(self):
        self.codigo_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.telefone_entry.delete(0, END)
        self.cidade_entry.delete(0, END)

class Application(Funcs):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.lista_frame2()

        root.mainloop()

    def tela(self):
        self.root.title('Cadastro de Clientes')
        self.root.configure(background='#1e3743')
        self.root.geometry('900x800')
        self.root.resizable(True, True)
        self.root.maxsize(width=900, height=700)
        self.root.minsize(width=400, height=300)

    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bd=9, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness=3)
        self.frame_1.place(relx=0.10, rely=0.10, relwidth=0.80, relheight=0.50)

        self.frame_2 = Frame(self.root, bd=9, bg='#dfe3ee', highlightbackground='#759fe8', highlightthickness=3)
        self.frame_2.place(relx=0.10, rely=0.65, relwidth=0.80, relheight=0.30)

    def widgets_frame1(self):
        ### Criação do botão limpar

        self.bt_limpar = Button(self.frame_1, text='Limpar',bd=4, fg='blue', font = ('verdana', 8, 'bold'), command= self.limpa_tela)
        self.bt_limpar.place(relx=0.25, rely=0.1, relwidth=0.1, relheight=0.15)

        # Criação do botão buscar
        self.bt_buscar = Button(self.frame_1, text='Buscar', bd=4, fg='blue', font = ('verdana', 8, 'bold'))
        self.bt_buscar.place(relx=0.35, rely=0.1, relwidth=0.1, relheight=0.15)

        # Criação do botão novo
        self.bt_novo = Button(self.frame_1, text='Novo', bd=4, fg='blue', font = ('verdana', 8, 'bold'))
        self.bt_novo.place(relx=0.55, rely=0.1, relwidth=0.1, relheight=0.15)

        # Criação do botão Alterar
        self.bt_alterar = Button(self.frame_1, text='Alterar', bd=4, fg='blue', font = ('verdana', 8, 'bold'))
        self.bt_alterar.place(relx=0.65, rely=0.1, relwidth=0.1, relheight=0.15)

        # Criação do botão apagar
        self.bt_apagar = Button(self.frame_1, text='Apagar', bd=4, fg='blue', font = ('verdana', 8, 'bold'))
        self.bt_apagar.place(relx=0.75, rely=0.1, relwidth=0.1, relheight=0.15)

        # Criação da Label e entrada do código
        self.lb_codigo = Label(self.frame_1, bg='yellow', text = 'Código')
        self.lb_codigo.place(relx= 0.06, rely= 0.06, relwidth=0.09, relheight=0.09)

        self.lb_nome = Label(self.frame_1, text= 'Nome', bg='yellow')
        self.lb_nome.place(relx= 0.06, rely= 0.35, relwidth=0.09, relheight=0.09)

        self.lb_telefone = Label(self.frame_1, text= 'Telefone', bg='yellow')
        self.lb_telefone.place(relx= 0.06, rely= 0.60, relwidth=0.09, relheight=0.09)

        self.lb_cidade = Label(self.frame_1, text= 'Cidade', bg='yellow')
        self.lb_cidade.place(relx= 0.55, rely= 0.60, relwidth=0.09, relheight=0.09)


        # Criacão do espaço preenchimento
        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx= 0.06, rely= 0.17, relwidth=0.09, relheight=0.09,)

        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx= 0.06, rely= 0.46, relwidth=0.60, relheight=0.09)

        self.telefone_entry = Entry(self.frame_1)
        self.telefone_entry.place(relx= 0.06, rely= 0.71, relwidth=0.40, relheight=0.09)

        self.cidade_entry = Entry(self.frame_1)
        self.cidade_entry.place(relx= 0.55, rely= 0.71, relwidth= 0.40, relheight= 0.09)

    def lista_frame2(self):
        self.listaCli = ttk.Treeview(self.frame_2, height= 3, column=('col1', 'col2', 'col3', 'col4'))
        self.listaCli.heading('#0', text="")
        self.listaCli.heading('#1', text="Código")
        self.listaCli.heading('#2', text="Nome")
        self.listaCli.heading('#3', text="Telefone")
        self.listaCli.heading('#4', text="Cidade")

        self.listaCli.column('#0', width=1)
        self.listaCli.column('#1', width=50)
        self.listaCli.column('#2', width=200)
        self.listaCli.column('#3', width=125)
        self.listaCli.column('#4', width=125)

        self.listaCli.place(relx=0.01, rely=0.00, relwidth=0.95, relheight=0.85)

        self.scroolLista = Scrollbar(self.frame_2, orient='vertical')
        self.listaCli.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.0, relwidth=0.04, relheight=0.85)

Application()
