"""
Estruturas lógicas: and (e), or (ou), not (não), is (é)

Operadores unários:
    - not;

Operadores binários:
    - and, or, is

Regras de funcionamento:

Para o 'and', ambos os valores precisam ser True
Para o 'or', um ou outro valor precisa ser True
Para o 'not', o valor do booleano é invertidom ou seja, se for True, vira o False, se for False vira True

=================================================================================

ativo = True
logado = True

if ativo and logado:
    print('Bem-vindo usuário!')
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')

=================================================================================

ativo = False
logado = False

# Se não estiver ativo
if not ativo:
    print('Você precisa ativar sua conta. Por favor, Cheque seu e-mail')
else:
    print('Bem-vindo usuário')

=====================================================================================

ativo = True
logado = False

if not ativo:
    print('Você precisa ativar sua conta. Por favor, Cheque seu e-mail')
else:
    print('Bem-vindo usuário')

print(not False)

======================================================================================

"""

ativo = True
logado = False

if ativo:
    print('Bem-vindo usuário')
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')

# ativo é Falso?
print(ativo is False)


