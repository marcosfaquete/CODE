"""
Crie um programa que leia dois números e mostre a soma entre eles.
"""
# My Code
lane = '===================================='
space = '\n'
print(lane)
name = str(input('\nOla qual o seu nome? \n'))
print('Seja Bem vindo(a) {}.'.format(name))
print(space)
n1 = int(input('Digite um número: \n'))
n2 = int(input('Digite outro número \n'))
totalsoma = (n1 + n2)
print('\nMuito Bem! \n')
print('{}, o resultado entre a soma do número {} e número {} é: {}'.format(name, n1, n2, totalsoma))
print(space)
print(lane)

# Guanabara Code

n1 = input('Digite um valor: ')
n2 = input('Digite outro valor: ')
s = (n1 + n2)
print('A soma entre {} e {} é igual a {}!'.format(n1, n2, s))