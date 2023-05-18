from tkinter import *


menu = Tk()

class Aplication():
    def __init__(self):
        self.menu = menu 
        self.menuConfig()
        self.menuBotoes()
        

        self.menu.mainloop()

    def menuConfig(self):
         self.menu.title('Software')
         self.menu.geometry('800x800+500+150')
         self.menu.resizable(False, False)
         self.menu.configure(background='skyblue')   

    def menuBotoes(self):
         self.botaoCadastro = Button(self.menu, text=('Cadastrar Clientes'), command=txtCadastro)
         self.botaoCadastro.pack()

def txtCadastro():
        janelaCadastro = Tk()
        txtNome = Label(menu, text='Nome:')
        txtNome.pack()
        
        

Aplication()