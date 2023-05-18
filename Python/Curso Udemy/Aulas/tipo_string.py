"""
Tipo string

Em Python, um dado é considerado do tipo string sempre que:

- Estiver entre àspas simples -> 'uma string', '234', 'a', 'True', '42.3'
- Estiver entre àspas duplas -> "uma string". "234", "a", "True", "42.3"
- Estiver entre àspas simples triplas -> '''uma string''', '''234''', '''a''', '''True''', '''42.3'''
"""
# Estiver entre àspas duplas triplas -> """uma string""", """234""", """a""", """True""", """42.3"""

nome = "Geek University"
print(nome)
print(type(nome))

nome = "'Nina's Bar"
print(nome)
print(type(nome))

nome = 'Angelina \nJolie'
print(nome)
print(type(nome))

nome = "Angelina \" Jolie"
print(nome)
print(type(nome))

nome = """Angelina
Jolie"""
print(nome)
print(type(nome))

nome2 = 'Geek University'
print(nome2.upper())
#Upper Tudo Maiúsculo

nome3 = 'Geek University'
print(nome3.lower())

nome4 = 'Geek University'
print(nome4.split())     # Transforma em uma lista de strings

# Estiver entre àspas duplas tripas -> """uma string""", """234""", """a""", """True""", """42.3"""

# [ 0    1    2    3    4    5    6    7    8    9   10   11   12   13   14
# ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
nome5 = 'Geek University'

# Retorna a letra conforme a posição inserida
print(nome5[3])

# Retorna delimitando o retorno
print(nome5[0:4])                       # Slice de String

# Posso escolher o que retornar conforme as codernadas das casas
print(nome5[5:15])                       # Slice de String

#     0       1
# ['Geek University']
print(nome5.split()[0])
print(nome5.split()[1])

# Retorna a letra da posicao inserida
print(nome5[14])

# retornadno as letras conforme suas posições
print(nome5[14], nome[13])

# [::-1] -> Comece do primeiro elemento, vá até o último elemento e inverta
print(nome5[::-1]) # Inversão da string Pythônico

print(nome5.replace('e', 'i')) # Substitui o e por i por exemplo

type(nome5)

