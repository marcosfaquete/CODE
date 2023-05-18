# Gerador de boas vindas

# Crie um programa que pede ao usuário seu nome e depois o dá boas-vindas
# dizendo "X seja bem-vindo", onde X é o nome do usuário.

print('\n')
print('=' * 50)
print('             <<< Gerador Boas-Vindas >>>')
print('=' * 50)
print('\n')
name = str(input('Digite seu nome: '))
print('Seja Bem-Vindo {}'.format(name.capitalize()))

