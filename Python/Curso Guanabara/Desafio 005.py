"""
    Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
"""
    # My Code
print('\n')
numero = int(input('Digite um número: '))
print('\n')
nmais = numero + 1
nmenos = numero - 1
print('O antecessor de [{}] é [{}] e seus sucessor é [{}]'.format(numero, nmenos, nmais))


    # Guanabara Code #01

n = int(input('Digite um número: '))
a = n - 1
s = n + 1
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(n, a, s))

    # Guanabara Code #02

n = int(input('Digite um número: '))
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(n, (n-1), (n+1)))