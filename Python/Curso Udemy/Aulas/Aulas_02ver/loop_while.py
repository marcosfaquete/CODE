"""
Loop while

forma geral

while expressão_booleana:
    // execução do loop

O bloco while será repetido enquanto a expressão booleana for verdadeira.

Expressão Booleana é toda expressão onde o resultado é verdadeiro ou falso.

Exemplo:

num = 5

num < 5

# Exemplo 1

numero = 1
while numero < 10:
    print(numero)
    numero = numero + 1

# OBS: Em um loop while, é importante que cuidemos do critério de parada para não causar loop infinito.
# O valor 10 se tornar falso.

# C ou Java
while(expressão){
    //execução
}

# do while (C ou Java)
do {
    // execução
}while(expressão):

"""
Python
# Exemplo 2

reposta = ''

while reposta != 'sim':
    reposta = input('Já acabou Jéssica? ')
