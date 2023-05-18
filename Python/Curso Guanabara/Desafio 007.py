"""
    Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
"""
    # My Code

print('===================================================')
print('## Calcule a média dos alunos ##\n')
name = str(input('Digite o nome do Aluno: '))
nota1 = float(input('Nota da primeira prova: '))
nota2 = float(input('Nota da segunda prova: '))
mediasoma = (nota1 + nota2)
print('\n')
print('Nome do Aluno: {}'.format(name))
print('Primeira Prova nota {}'.format(nota1))
print('Segunda Prova nota  {}'.format(nota2))
print('Média de {} é: {}'.format(name, (mediasoma / 2)))
print('===================================================')


    # Guanabara Code

n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
média = (n1 + n2) / 2
print('A média entre {:.1f} e {:.1f} é igual a {:.1f}'.format(n1, n2, média))