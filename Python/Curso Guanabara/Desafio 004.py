"""
    Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações
    possíveis sobre ele.
    """
   # My Code
print('\n')
valor1 = input('Olá digite qualquer valor: ')
print('\n')
print('Tipo do dado digitado  ==>>  ', type(valor1))
print('Ele é Alfanumérico?  ==>>  ', valor1.isalnum())
print('Ele esta no alfabeto?  ==>>  ', valor1.isalpha())
print('Capitalizando o dado   ==>>  ', valor1.capitalize())     # capitalize. Sempre retornará o a string com a primeira letra em maiúscula.
print('Está em maiúsculo?     ==>>  ', valor1.isupper())
print('Está em minúsculo?     ==>>  ', valor1.islower())
print('Ele é um número?       ==>>  ', valor1.isnumeric())
print('Ele é Decimal?         ==>>  ', valor1.isdecimal())
print('Tem espaços?           ==>>  ', valor1.isspace())



a = str(input('Digite uma palavra: \n'))
print('Invertendo String: ', a.swapcase())        # Inverte as Strings.


    # Guanabara Code

a = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(a))
print('Só tem espaços? ', a.isspace())
print('É um número? ', a.isnumeric())
print('É alfabético? ', a.isalpha())
print('É alfanumérico?'), a.isalnum()
print('Está em maiúsculas?'), a.isupper()
print('Está em minúsculas?', a.islower())
print('Está capitalizada? ', a.istitle())


