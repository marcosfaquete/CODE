"""
Listas

Listas em Python funciona como vetores/matrizes (arrays) em outras linguagens, com a diferença
de serem DINÂMICO e também de podermos colocar QUALQUER tipo de dado.

Linguagens C/Java: Arrays

- Possuem tamanho e tipo de dado fixo:
Ou seja, nestas linguagens se voce criar um array do tipo int e com tamanho 5, este array
será SEMPRE do tipo inteiro e poderá ter SEMPRE no máximo 5 valores.

Já em Python:
- Dinâmico: Não possui tamanho fixo; Ou seja, podemos criar a lista e simplesmente ir adicionando
elementos;

- Qualquer tipo de dado: Não possuem tipo de dado fixo: Ou seja, podemos colocar qualquer tipo de dado:

As listas em Python são representadas por colchetes: []
"""
type([])
lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
lista3 = []
lista4 = list(range(11))
lista5 = list('Geek University')

# Podemos facilmente checar se  determinado valor está contido na lista
num = 7
if num in lista4:
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o número {num}')



#   Podemos facilmente ordenar uma lista
lista1.sort()
print(lista1)



#   Podemos facilmente contar o número de ocorências de um valor em uma lista
print(lista1.count(1))
print(lista5.count('e'))

#   Adicionar elementos em listas

"""
Para adicionar elementos em listas, utilizamos a função append

OBS: Com append, nós só conseguimos adicionar 1 elemento por vez
"""
print(lista1)
lista1.append(42)   #append adiciona elemento
print(lista1)

#lista1.append(12, 34, 56)   # Erro só podmeos passar 1 elemento por vez

lista1.append([8, 3, 1]) # adicionando uma lista dentro de outra lista
print(lista1)

if [8, 3, 1] in lista1:
    print('\n')
    print('Encontrei a lista')
else:
    print('Não encontrei a lista')