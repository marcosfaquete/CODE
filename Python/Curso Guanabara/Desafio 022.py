"""
    Crie um programa que leia o nome completo de uma pessoa e mostre:
    
    # O nome com todas as letras maiúsculas
    # O nome com todas minúsculas.
    # Quantas letras ao todo (sem considerar espaços).
    # Quantas letras tem o primeiro nome.
"""
    # My Code
print('\033[31mOlá, Seja Bem Vindo(a)\033[m')
name = str(input('\033[32mDigite seu nome completo: \033[m')).strip() # Caso não colocar strip, se o campo for preenchido com espaço ele será contado.
print('\033[31mAnalisando seu nome...\033[m')
print('\033[32mSeu nome em maiúsculas: \033[m{}'.format(name.upper()))
print('\033[34mSeu nome em minúsculas: \033[m{}'.format(name.lower()))
print('\033[33mSeu nome tem ao todo\033[m {}\033[33m letras\033[m'.format(len(name) - name.count(' ')))
print('\033[35mSeu primeiro nome tem\033[m {} \033[35mletras\033[m'.format(name.find(' ')))
separa = name.split()
print('\033[36mSeu primeiro nome é\033[m {} \033[36me ele tem \033[m{} \033[36mletras\033[m'.format(separa[0], len(separa[0])))

    # Guanabara Code
nome = str(input('Digite o seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count((' '))))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))

