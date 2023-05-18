

from tkinter import *

menu = Tk()

class Aplicativo:
    def __init__(self):
        self.menu = menu
        self.menu_config()
        self.menu_botoes()
       


        self.menu.mainloop()


    def menu_config(self):
        self.menu.title('Software')
        self.menu.geometry('800x800+380+100')
        self.menu.resizable(False, False)
        self.menu.configure(background='skyblue')

    def menu_botoes(self):
        self.botao_1 = Button(self.menu, text='Cadastrar Clientes', command=ordens)
        self.botao_1.pack()

def ordens():
    print('Hello World!')
    txt_1 = Label(menu, text='Nome:')
    txt_1.pack()



Aplicativo()