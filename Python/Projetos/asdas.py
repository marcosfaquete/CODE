import tkinter as tk
from tkinter import filedialog

def salvar_dados():
    # obter o caminho do arquivo onde os dados serão salvos
    caminho_arquivo = filedialog.asksaveasfilename(defaultextension=".txt")

    # abrir o arquivo no modo de gravação
    with open(caminho_arquivo, 'w') as arquivo:
        # escrever os dados dos campos Entry no arquivo
        arquivo.write(f"Nome: {campo_nome.get()}\n")
        arquivo.write(f"Idade: {campo_idade.get()}\n")
        arquivo.write(f"Endereço: {campo_endereco.get()}\n")

# criar a janela principal
janela = tk.Tk()

# criar os campos Entry
campo_nome = tk.Entry(janela)
campo_idade = tk.Entry(janela)
campo_endereco = tk.Entry(janela)

# criar o botão de salvar
botao_salvar = tk.Button(janela, text="Salvar", command=salvar_dados)

# adicionar os campos Entry e o botão de salvar à janela
campo_nome.pack()
campo_idade.pack()
campo_endereco.pack()
botao_salvar.pack()

# iniciar o loop principal da janela
janela.mainloop()
