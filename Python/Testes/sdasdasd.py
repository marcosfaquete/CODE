import tkinter as tk
import random

class Menu:
    def __init__(self, janela):
        self.menu = tk.Frame(janela, bg='#E5E5E5')
        self.menu.place(relx=0, rely=0, relheight=1, relwidth=1)
        self.textomenu()
        
    def textomenu(self):
        self.txt_filmaEu = tk.Label(self.menu, text='FilmaEu', font='Arial 40 bold', background='gray')
        self.txt_filmaEu.place(relx=0.35, rely=0.07, relheight=0.05, relwidth=0.30)
        self.altera_cor()
        
    def altera_cor(self):
        r = lambda: random.randint(0,255)
        cor = '#{:02x}{:02x}{:02x}'.format(r(),r(),r()) # gera uma cor aleatória
        self.txt_filmaEu.configure(background=cor)
        self.menu.after(1000, self.altera_cor) # chama a função a cada 1 segundo

janela = tk.Tk()
janela.geometry("600x400")
Menu(janela)
janela.mainloop()