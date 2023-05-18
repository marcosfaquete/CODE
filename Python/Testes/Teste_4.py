import time
from tkinter import *



class app():
    def __init__(self):
        self.menu = Tk()
        self.Botoes()
        self.EntradaDados()
        self.Texto()
        self.MarcaCaixa()
        self.Canvass()
        self.RadioButon()
        self.Frames()
        self.Seila()
        self.Seila2()

        self.menu.resizable(True, True)
        self.menu.title('Menu')
        self.menu.geometry('900x900+600+300')
        self.menu.maxsize(1000, 1000)
        self.menu.minsize(700, 700)
        self.menu.configure(background='gray')


        self.menu.mainloop()

    def Texto(self):
        self.Texto1 = Label(self.menu, text='Nome', foreground='red', highlightthickness='9')
        self.Texto1.place(relx= 0.17, rely=0.27, relheight=0.10, relwidth=0.10)


    def Botoes(self):
        self.botao1 = Button(self.menu, text='OK', bg='green')
        self.botao1.place(relx= 0.10, rely=0.10, relheight=0.10, relwidth=0.10)

    def EntradaDados(self):
        self.Entrada1 = Text(self.menu, highlightthickness='3', highlightcolor='red')
        self.Entrada1.place(relx=0.30, rely=0.30, relheight=0.05, relwidth=0.50)
        #highlightthickness='9' Cria uma bordinha
        #highlightcolor = 'red' Escolhe a cor da bordinha

    def MarcaCaixa(self):
        self.box1 = Checkbutton(self.menu)
        self.box1.place(relx=0.45, rely=0.45, relheight=0.10, relwidth=0.10)
        self.box2 = Checkbutton(self.menu)
        self.box2.place(relx=0.55, rely=0.45, relheight=0.10, relwidth=0.10)

    def Canvass(self):
        self.Canvaa1 = Canvas(self.menu, background='red')    # Um quadrado hahahahha
        self.Canvaa1.place(relx=0.55, rely=0.20, width=50, height=50)


    def RadioButon(self):
        self.RD1= Radiobutton(self.menu, background='blue', foreground='red')
        self.RD1.place(relx=0.10,rely=0.70,relwidth=0.10, relheight=0.10)


    def Frames(self):
        self.Frame1 = Frame(self.menu, background='yellow')
        self.Frame1.place(relx=0.80, rely=0.50, relheight=0.10, relwidth=0.10)

    def Seila(self):
        self.Seila1 = LabelFrame(self.menu)
        self.Seila1.place(relx=0.35, rely=0.35, relwidth=0.10, relheight=0.10)

    def Seila2(self):
        self.Seila3 = Message(self.menu, text='lol')
        self.Seila3.place(relx=0.85, rely=0.85, relwidth=0.10, relheight=0.10)







app()