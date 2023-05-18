"""
Loop for

Loop -> Estrutura de repetição.
For -> Uma dessas estruturas

=============================================
C ou Java

for(int i = 0; i < 10; i++){
    //execução do loop
}
==============================================
PYTHON

for item in interavel:
    //execução do loop

Utilizamos loops para interar sobre sequências ou sobre valores iteráveis

Exemplos de iteráveis:
- String
    nome = 'Geek University'
-Lista
    lista = [1, 3, 5, 7, 9]
-Range
    numeros = range(1, 10)
=====================================================

nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)  # Temos que transformar em uma lista

# Exemplo de for 1 (Iterando em uma string)
for letra in nome:
    print(letra)
===============================================================
# Exemplo de for 2 (Iterando sobre uma lista)
for numero in lista:
    print(numero)
===============================================================
# Exemplo de for 3 (Iterando sobre um range)
# Range (valor inicial, valor final)
#OBS: O valor final não é inclusive.

for numero in range(1, 10):
    print(numero)
===============================================================

"""

qtd = int(input('Quantas vezes esse loop deve rodar? \n'))

for n in range(0, qtd):
    print(f'Imprimindo {n}')


