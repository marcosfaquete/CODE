"""
Tipo string

Em Python, um dado é considerado do tipo string sempre que:

- Estiver entre àspas simples -> 'uma string', '234', 'a', 'True', '42.3'
- Estiver entre àspas duplas -> "uma string", "234", "a", "True", "42.3"
- Estiver entre àspas simples tripas -> 'uma string', '234', 'a', 'True', '42.3'

nome = 'Geek University'
print(nome)
print(type(nome))

nome = "Gina's Bar"
print(nome)
print(type(nome))

nome = 'Angelina \nJolie'
print(nome)
print(type(nome))

nome = 'Geek University'
print(nome[0:4])   # Slice de tring

print(nome[5:15])  # Slice de tring

print(nome.split()[0])

print(nome.split()[1])
"""
# Estiver entre àspas duplas triplas -> """uma string""", """234""", """a""", """True""", """42.3"""

# [ 0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,  13,  14,]
# ['G', 'e', 'e', 'k', ' ', 'u', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']


nome = 'Geek University'
"""
[::-1] -> Comece do primeiro elemento, vá até o ultimo elemento e inverta
"""

print(nome[::-1])