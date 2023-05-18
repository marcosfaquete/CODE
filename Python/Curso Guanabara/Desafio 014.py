"""
    Escreva um programa que converta uma temperatura digitada
    em °C e converta para °F.
"""

    # My Code

celcius = float(input('Digite a temperatura Celcius: '))
calc1 = ((celcius * 9) / 5 ) + 32
print('Temperatura convertida em °F {:.2f}'.format(calc1))

    # Guanabara Code

c = float(input('Informe a temperatura em °C '))
f = 9 * c / 5 + 32
print('A temperatura de {}°C corresponde a {}°F!'.format(c, f))