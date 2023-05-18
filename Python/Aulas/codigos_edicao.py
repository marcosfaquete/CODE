"""
CODIGOS DE EDIÇÃO

highlightthickness= 3
highlightbackground='green'

def CatFrame(self):
    self.Frame1 = Frame(self.root, background="gray", highlightthickness=3, highlightbackground='#759fe6')
    self.Frame1.place(relx= 0.08, rely= 0.05, relheight= 0.40, relwidth= 0.85)


highlightthickness= 3 (add borda em volta do frame)
highlightbackground='green' (add a cor em volta do frame)

===================================================================================================================
font = ('verdana', 8, 'bold'))      determina tipo de letra, o tamanho, e o bold é negrito!
bd=4                                bd é a borda do botão
fg='blue'                           a cor da letra dentro do botão


 ### Criação do botão limpar

        self.bt_limpar = Button(self.frame_1, text='Limpar', bd=4, fg='blue', font = ('verdana', 8, 'bold'))
        self.bt_limpar.place(relx=0.25, rely=0.1, relwidth=0.1, relheight=0.15)

==================================================================================================================






"""