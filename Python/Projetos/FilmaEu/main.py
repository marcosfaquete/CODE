from tkinter import *
from tkinter import filedialog
import random

menu = Tk()

class menu_cadastro:
    def __init__(self):
        self.menu = menu 
        self.menucadastro()
        self.textomenu()
        self.entradadados()
        self.botoes()
        self.menu.mainloop()
        
############ CONFIGURAÇÃO DO MENU ############
    def menucadastro(self):  # Configuração do menu
        self.menu.title('FilmaEu')
        self.menu.geometry('800x800+600+150')
        self.menu.resizable(False, False)
        self.menu.maxsize(height=800, width=800)
        self.menu.minsize(height=600, width=600)
        self.menu.configure(background='black')
        
        self.quadrado1 = Frame(self.menu, background='gray', highlightbackground='orange', highlightthickness=3, bd=5)  
        self.quadrado1.place(relx=0.01, rely=0.01, relheight=0.98, relwidth=0.98)
        
############ CRIAÇÃO TEXTOS NO MENU ############
    def textomenu(self):  # Criação textos no menu.
        
        self.txt_filmaEu = Label(self.menu, text='FilmaEu',font='Impact 60 bold', background='gray')
        self.txt_filmaEu.place(relx=0.35, rely=0.07)
        self.alterar_cor_aleatoria()
        
        self.txt_nomeCliente = Label(self.menu, font='Helvetica 17 bold', text='ID Cliente', background='#00CCFF')
        self.txt_nomeCliente.place(relx=0.25, rely=0.20, relheight=0.05, relwidth=0.30)

        self.txt_QuantsDome = Label(self.menu, font='Arial 17 bold', text='Quantas Dome?', background='#00CCFF')
        self.txt_QuantsDome.place(relx=0.25, rely=0.30, relheight=0.05, relwidth=0.30)

        self.txt_QuantsBullet = Label(self.menu, font='Arial 17 bold', text='Quantas Bullet?', background='#00CCFF')
        self.txt_QuantsBullet.place(relx=0.25, rely=0.40, relheight=0.05, relwidth=0.30)

############ CRIAÇÃO DOS CAMPOS DA ENTRADA DE DADOS ############
    def entradadados(self):  # Criação dos campos da entrada de dados.
        self.dados_ID = Entry(self.menu, font='Arial 17 bold')
        self.dados_ID.place(relx=0.56, rely=0.20, relheight=0.05, relwidth=0.10)

        self.dados_Dome = Entry(self.menu, font='Arial 17 bold')
        self.dados_Dome.place(relx=0.56, rely=0.30, relheight=0.05, relwidth=0.10)

        self.dados_Bullet = Entry(self.menu, font='Arial 17 bold')
        self.dados_Bullet.place(relx=0.56, rely=0.40, relheight=0.05, relwidth=0.10)

############ CRIAÇÃO DOS BOTÕES ############
    def botoes(self):
        self.botoes_Salvar = Button(self.menu, text='Salvar', font='Arial 17 bold')
        self.botoes_Salvar.pack()
        self.botoes_Salvar.place(x=370, y=500)
        
############ CRIAÇÃO DAS CORES ALEATÓRIAS ############
    def alterar_cor_aleatoria(self):
        # gerar valores aleatórios de R, G e B
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        # criar a cor a partir dos valores aleatórios
        cor_texto = f'#{r:02x}{g:02x}{b:02x}'
        # definir a nova cor do texto
        self.txt_filmaEu.config(fg=cor_texto)
        # chamar a função novamente após um intervalo de tempo (em milissegundos)
        self.menu.after(1000, self.alterar_cor_aleatoria)


        





menu_cadastro()

