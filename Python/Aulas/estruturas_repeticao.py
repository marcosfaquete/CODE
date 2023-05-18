    # Exemplo 001
"""
contador = 0
while contador < 1000000:
    contador = contador + 1
    print(contador)

#===============================================================

    # Exemplo 002

import time
contador = 0
while contador < 10:
    print('Contando...')
    print(contador)
    contador = contador + 1
    if contador == 11:
        break
    time.sleep(1)
print('Pronto!')

#==================================================================

    # Exemplo 003

soma = 0
for i in range(1, 10):
    if i == 10:
        soma + i
    print(soma)
    """
    # Exemplo 004

qtd = int(input('Quantas vezes esse loop deve rodar? \n'))

for n in range(0, qtd):
    print(f'Imprimindo {n}')

