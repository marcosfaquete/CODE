"""
    Escreva um programa que pergunte a quantidade de Km percorridos por um carro
    alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
    sabendo que o carro custa R$60 por dia e R$0,15 por KM rodado.
"""
    # My Code

print('='*43)
print('## Calcule o valor total a ser cobrado ##')
name = str(input('Nome do Cliente: '))
dias = int(input('Quantos dias o veículo permaneceu alugado? '))
km = int(input('Quantos kilometros foram rodados? '))
total_dias = (dias * 60)
total_km = (km * 0.15)
print('='*43)
finish = (total_dias + total_km)
print('Nome do Cliente: {}.'.format(name))
print('Dias com o carro: {} Dias.'.format(dias))
print('Kilometros rodados: {:.0f} Km.'.format(km))
print('Valor cobrado por Dias R${:.2f}.'.format(total_dias))
print('Valor cobrado por Km rodado R${:.2f}.'.format(total_km))
print('Total a pagar R${:.2f}'.format(finish))
print('='*43)

    # Guanabara Code

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(pago))