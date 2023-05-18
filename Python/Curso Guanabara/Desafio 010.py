"""
    Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
e mostre quantos Dólares ela pode comprar. Considere US$1,00 = R$3,27
"""
    # My Code

dinheiro = float(input('Quantos reais você tem? '))
preco_dolar = 3.27
resul = (dinheiro / preco_dolar)
print('Com R${:.2f} você pode comprar US${:.2f}'.format(dinheiro, resul))

    # Guanabara Code

real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 3.27
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))