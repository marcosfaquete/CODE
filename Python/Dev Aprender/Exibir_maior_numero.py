# Crie um programa que recebe dois valores e exibe qual é o maior entre eles.

print('\n')
print('<<< Exibir Número Maior >>>')
print('\n')

numero_1 = int(input('Digite um número: '))
numero_2 = int(input('Digite outro número: '))

if numero_1 > numero_2:
    print('Números digitados {} e {}'.format(numero_1, numero_2))
    print('O número maior é: {}'.format(numero_1))

elif numero_1 < numero_2:
    print('Números digitados {} e {}'.format(numero_1, numero_2))
    print('O número maior é: {}'.format(numero_2))