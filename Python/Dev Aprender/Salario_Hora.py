#===================================================================================================================================================================
# Escreva um programa que retorne o valor hora de um funcionário com base no
# salário mensal e horas trabalhadas por mês.
#===================================================================================================================================================================

import time

print('\n')
print("Meu Salário por hora")
name = str(input("Digite o nome do funcionário: "))
salario = float(input("Digite o salário mensal de {}: ".format(name)))
horas_trabalhadas = float(input("Digite as horas trabalhadas por {}: ".format(name)))
valorhora = (salario / horas_trabalhadas)

print('\n')
time.sleep(1)
print("Nome do funcionário: {}".format(name))
print("Salario Mensal de: {}".format(salario))
print("Horas trabalhadas: {}".format(horas_trabalhadas))
print("O valor da hora do Funcionário {} é de R${}".format(name, valorhora))
print('\n')


