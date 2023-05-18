"""
    Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo
    retângulo, calcule e mostre o comprimento da hipotenusa.
"""
    # Método sem importação nenhuma
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))

    # Método usando a biblioteca math
import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co, ca) # hypot hipotenusa
print('A hipotenusa vai medir {:.2f}'.format(hi))

    # Método 3 importanto de math o hypot(hipotenusa)
from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))

