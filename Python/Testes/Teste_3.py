from tkinter import *

on = True
def printar():
    print('Hello World!')

app_menu = Tk()
app_menu.title('Infinity Colors')

app_menu.resizable(True, True)
app_menu.geometry('570x570+650+250')
app_menu.maxsize(700,700)
app_menu.minsize(500,500)
app_menu.configure(background="GRAY")

txt1=Label(app_menu, text="LALA", background='GREEN', foreground="YELLOW")
txt1.place(x=10, y=10, width=150, height=30)

botao1 = Button(app_menu, text='Click!', command=printar)
botao1.place(x=10, y=50, width=100, height=50)

app_menu.mainloop()