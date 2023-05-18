



print('\n')
print('>>> Média do Aluno <<<')
print('\n')

nome = str(input('Digite o nome do aluno: '))
nota_1 = int(input('Digite a Primeira nota de {}: '.format(nome)))
nota_2 = int(input('Digite a Segunda nota de {}: '.format(nome)))

media = (nota_1 + nota_2 /2)
print('\n')
print('A Média do Aluno {} é: {}'.format(nome, media))
print('\n')

if media <= 5:
    print('Aluno {} Está REPROVADO!'.format(nome))
    
else: print('Aluno {} Está APROVADO!'.format(nome))

print('\n')


