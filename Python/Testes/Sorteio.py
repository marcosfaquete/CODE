"""
    Um professor quer sortear um dos seus quatro alunos para pagar o quadro.
Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

"""

import random
import time

on = True

while on == True:
    print('\b')

    print('=' * 45)
    print('               >>> Sorteio <<<')
    print('=' * 45)
    print('\b')

    print('Digite [0] para sair')

    quantidade_nomes = int(input('Quantos nomes deseja sortear? '))
    print()
    for i in range(quantidade_nomes):

        if quantidade_nomes == 1:
            print('One Person Realy!?')
            quantidade_nomes = 777
        
        elif quantidade_nomes == 2:
            name_1 = input('Primeiro nome: ')
            name_2 = input('Segundo nome: ')
            sorteio = random.randint(1, 2)
            print('O aluno sorteado foi: {}'.format(sorteio))
            pause = input('Digite qualquer tecla para continuar...')
            quantidade_nomes = 777

        elif quantidade_nomes == 3:
            name_3 = input('Primeiro nome: ')
            name_4 = input('Segundo nome: ')
            name_5 = input('Terceiro nome: ')
            pause = input('Digite qualquer tecla para continuar...')
            quantidade_nomes == 777
            quantidade_nomes == 776
            quantidade_nomes == 775

        elif quantidade_nomes == 0:
            print('\b')
            time.sleep(1)
            print('Saindo em 3')
            time.sleep(1)
            print('Saindo em 2')
            time.sleep(1)
            print('Saindo em 1')
            on = False




