"""
    Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.

Ex:
    Digite um número:6.127 O número 6.127 tem a parte Inteira 6.
"""
    # Guanabara Code

    # Método 1
import math
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, math.trunc(num)))

    # Método 2  Só importa o método trunc
from math import  trunc
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))

    # Método 3 Sem importar biblioteca
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))








