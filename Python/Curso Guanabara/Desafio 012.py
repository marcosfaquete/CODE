"""
    Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
"""

    # My Code
print('## Desconto de 5% Aproveite a Promoção ##')
preco_produto = float(input('Qual o preço original do produto? R$'))
desconto = preco_produto - (preco_produto * 5/100)
print('O preço do produto com desconto sai por R${:.2f}'.format(desconto))

    # Guanabara Code

preço = float(input('Qual é o preço do produto? R$'))
novo = preço - (preço * 5 / 100)
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preço, novo))