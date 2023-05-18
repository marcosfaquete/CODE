#===================================================================================================================================================================
# Problema 3 - Chute o número

# 1. Quais são os dados de entrada necessários?
# Escreva um programa que, ao iniciar gera um valor aleatório de 1 a 10 e permite que o usuário chute um número até que o valor aleatório gerado
# no início do programa seja chutado corretamente. O programa deve informar se o chute foi a cima, abaixo ou igual o valor aleátorio gerado no início do programa.
#===================================================================================================================================================================

from random import random, randrange
import time

on = True

while on == True:
    print('\n')
    print('=' * 50)
    print('             <<< Chute um Número >>>')
    print('=' * 50)
    print('\n')
    numero_aleatorio = randrange(1, 11)
    numero_digitado = int(input("Digite um número de 1 a 10: "))

    if numero_digitado == numero_aleatorio:
        print('Número sorteado foi: {}'.format(numero_aleatorio))
        print("<<< PARABENS! Você Acertou o Número Sorteado! >>>")
        time.sleep(1)
        choice = str(input("Digite qualquer tecla para jogar novamente ou digite s para Sair "))
        if choice == 's':
            on = False
            print('\n')
            print('Saindo do jogo em ...3')
            time.sleep(1)
            print('Saindo do jogo em ...2')
            time.sleep(1)
            print('Saindo do jogo em ...1')
            time.sleep(1)

    else:
        print('Número sorteado foi: {}'.format(numero_aleatorio))
        print('Você não teve sorte, tente novamente')
        if numero_digitado < numero_aleatorio:
            print('Número digitado menor que o sorteado!')
        elif numero_digitado > numero_aleatorio:
            print('Número digitado maior que o sorteado!')

        time.sleep(1)
        choice = str(input("Digite qualquer tecla para jogar novamente ou digite s para Sair "))
        if choice == 's':
            on = False
            print('\n')
            print('Saindo do jogo em ...3')
            time.sleep(1)
            print('Saindo do jogo em ...2')
            time.sleep(1)
            print('Saindo do jogo em ...1')
            time.sleep(1)



