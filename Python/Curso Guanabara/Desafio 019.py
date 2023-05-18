"""
    Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que
    ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
"""

    # My Code

import random   # Importando random para fazer o sorteio das variáveis.

print('\033[31m##\033[m \033[33mPrograma Sorteio do Aluno\033[m \033[31m##\033[m')  # codigos de cor \033[32m ex_textocolorido \033[m
print('\033[32mDigite o nome dos alunos(a) para o sorteio\033[m')
name1 = str(input('\033[34mPrimeiro nome: \033[m'))
name2 = str(input('\033[34mSegundo nome:  \033[m'))
name3 = str(input('\033[34mTerceiro nome: \033[m'))
name4 = str(input('\033[34mQuarto nome:   \033[m'))
name5 = str(input('\033[34mQuinto nome:   \033[m'))
sorteio = random.randint(1, 5)  # Variável sorteio recebendo o número aleatório de random.radint de 1 a 5.

if sorteio == 1:    # Se a variável sorteio recebeu for igual a 1 escreva isso:
    print('\033[34mO aluno(a) sorteado foi\033[m \033[31m{}\033[m'.format(name1.capitalize()))  # Capitalize para retornar nome escrito certo, caso preenchido incorreto(só minúsculas)
elif sorteio == 2:
    print('\033[34mO aluno(a) sorteado foi\033[m \033[31m{}\033[m'.format(name2.capitalize()))
elif sorteio == 3:
    print('\033[34mO aluno(a) sorteado foi\033[m \033[31m{}\033[m'.format(name3.capitalize()))
elif sorteio == 4:
    print('\033[34mO aluno(a) sorteado foi\033[m \033[31m{}\033[m'.format(name4.capitalize()))
elif sorteio == 5:
    print('\033[34mO aluno(a) sorteado foi\033[m \033[31m{}\033[m'.format(name5.capitalize()))


    # Guanabara Code

    # Método 1
import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))


    # Método 2
from random import choice
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
