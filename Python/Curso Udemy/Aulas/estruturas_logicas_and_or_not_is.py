"""
Estruturas Lógicas: and(e), or(ou), not(não), is(é)

Operadores unários:
    - not;

Operadores binários:
    - and, or, is



"""

# Para o 'and', ambos os valores precisam ser True
print('\n')

ativo = True        # Ativo tipo na porta do login
logado = False      # Se passou pelo login ou não

if ativo:
    print('Usuário ativo no sistema')


if ativo and logado:
    print('Bem-vindo usuário!')
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')

print('\n')

"""
===================================================================================================
"""

# Para o 'or', um ou outro valor precisa ser True
if ativo:
    print('Usuário ativo no sistema')


if ativo or logado:
    print('Bem-vindo usuário!')
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')
print('\n')

"""
===================================================================================================
"""

# Para o 'not', o valor do booleano é invertido, ou seja, se for True, vira False, se for False vira True.

# Operador de negação

#print(not True)
#output = False

#print(not False)
#output = True


ativo = True
logado = False

if not ativo:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')
else:
    print('Bem-vindo usuário')

print('\n')

"""
=====================================================================================================
"""

ativo = False
logado = False

# usa-se mais if not

if ativo is False:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')
else:
    print('Bem-vindo usuário')




