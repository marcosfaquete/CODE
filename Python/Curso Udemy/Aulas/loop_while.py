"""
Loop while

Forma geral

while expressão_booleana:
    //execução do loop

O vloco do while será repetido enquanto a expressão booleana for verdadeira.

Expressão Booleana é toda expressão onde o resultado é verdadeiro ou falso.

Exemplo 3:

num = 5
num < 5

True or False


numero = 1

while numero < 10:
    print(numero)
    numero = numero + 1


==========================================================================================================
#   Exemplo de loop Infinito

# OBS: Em um loop while, é importante que cuidemos do critério de parada para não causar
um loop infinito.

numero = 1

while numero < 10:
    print(numero)
    
==========================================================================================================

# Exemplo 2 


resposta = ''

while resposta != 'sim':
    resposta = input('Já acabou Jéssica?')
    
    
==========================================================================================================
"""
# Meu exemplo kkk

on = True

while on:
    print('Olá')
    choice_exit = int(input('Digite 3 para Sair: '))
    if choice_exit == 3:
        on = False


