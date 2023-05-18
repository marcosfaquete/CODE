"""
    Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com
    15% de aumento.
"""
    # My Code

print('## Aumento no salário de 15% ##')
name = str(input('Qual o nome do funcionário? '))
salario_atual = float(input('Qual o salário atual do funcionário? R$'))
aumento = (salario_atual + (salario_atual * 15/100))
print('\n')
print('O salário atual de {} é {:.0f}. Seu novo salário será de R${:.0f}'.format(name, salario_atual, aumento))

    # Guanabara Code

salário = float(input('Qual é o salário do Funcionário? R$'))
novo = salário + (salário * 15 / 100)
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salário, novo))