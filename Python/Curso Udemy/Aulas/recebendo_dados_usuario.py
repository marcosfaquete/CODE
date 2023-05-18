"""
Recebendo dados do usuário

input() -> Todo dado recebido via input é do tipo String

Tudo que estiver entre:
- Aspas simnples;
- Aspas duplas;
- Aspas simples tríplas;
- Aspas duplas triplas;

Exemplos:
- Aspas simples -> 'Angelinas Jolie'
- Aspas duplas -> "Angelinas Jolie"
- Aspas simples triplas -> '''Angelinas Jolie'''
- Aspas duplas triplas -> com 3 asoas duplas
"""
# Entrada de dados
print("Qual seu nome? ")
nome = input()  # Input -> Entrada

nome = input('Qual seu nome? ')

# Exemplo de print 'antigo' 2.x
print('Seja bem-vindo(a) %s' % nome)

# Exemplo de print 'moderno' 3.x
print('Seja bem-vindo(a) {0}'.format(nome))

# Exemplo de print 'mais atual' 3.7
print(f'Seja bem-vindo(a) {nome}')

print("Qual sua idade? ")
idade = input()

idade = input('Qual sua idade? ')

idade = int(input('Qual sua idade? '))

# Processamento

# Saida
# Exemplo de print 'antigo' 2.x
# print('A %s tem %s anos' % (nome, idade))

# Exemplo de print 'moderno' 3.x
print('A {0} tem {1} anos'.format(nome, idade))

# Exemplo de print 'mais atual' 3.7
print(f'A {nome} tem {idade} anos')

"""
# int(idade => cast

Cast é a 'conversão' de um tipo de dado para outro.
"""

# forma poderosa
print(f'A {nome} nasceu em {2018 - int(idade)}')
