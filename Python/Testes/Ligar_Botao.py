from tkinter import *

def comando():
    print('Led Azul Ligado')


janela1 = Tk()
janela1.title('lol')
janela1.geometry('500x500')

texto1 = Label(text='Botão que liga led azul')
texto1.pack()


botao1 = Button(text='Ligar led azul', command = comando).pack()

janela1.mainloop()