"""
    Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
"""
    # My Code

print('\n')
numero1 = int(input('Digite um valor: '))
dobro = numero1 * 2
triplo = numero1 * 3
raiz = numero1 ** (1/2)
print('\n')
print('Número digitado foi {}. Seu dobro é {}. Seu triplo é {}. Sua raiz quadrada é {}'.format(numero1, dobro, triplo, raiz))


    # Guanabara Code 1
n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro de {} vale {}.'.format(n, d))
print('O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}.'.format(n, t, n, r))

    # Guanabara Code 2
n = int(input('Digite um número: '))
print('O dobro de {} vale {}.'.format(n, (n*2)))
print('O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}.'.format(n, (n*3), n, (n**(1/2))))

    # Guanabara Code 3
n = int(input('Digite um número: '))
print('O dobro de {} vale {}.'.format(n, (n*2)))
print('O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}.'.format(n, (n*3), n, pow(n, (1/2))))