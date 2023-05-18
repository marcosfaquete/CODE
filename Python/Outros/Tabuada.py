import time


on = True

name = str(input('Qual é o seu nome?\n'))
print('\n')
print('Seja Bem-Vindo {}!'.format(name))
time.sleep(3)
print('\n')


print('#     MENU     #')
time.sleep(1)
print('[1] Tabuada')
time.sleep(1)
print('[2] Multiplicação')
time.sleep(1)
print('[3] Adição')
time.sleep(1)
print('[4] Subitração')
time.sleep(1)
print('[5] Divisão')
time.sleep(1)
print('\n')
choicemenu = int(input('Por favor {} Digite sua escolha: '.format(name)))
print('\n')

while on == True:
    if choicemenu == 1:
        print('              ## TABUADA ##')
    print(' [1]'
          ' [2]'
          ' [3]'
          ' [4]'
          ' [5]'
          ' [6]'
          ' [7]'
          ' [8]'
          ' [9]'
          ' [10]')

    print('\n')
    print('[0] Sair do programa')
    choicetabuada = int(input('Por favor {} Digite o número da Tabuada que Deseja Visualizar\n'.format(name)))


    print('\n')

    if choicetabuada == 1:
        print('1x1  = 1')
        print('1x2  = 2')
        print('1x3  = 3')
        print('1x4  = 4')
        print('1x5  = 5')
        print('1x6  = 6')
        print('1x7  = 7')
        print('1x8  = 8')
        print('1x9  = 9')
        print('1x10 = 10')
        print('\n')
        conf = str(input('Digite qualquer tecla para continuar...'))


    elif choicetabuada == 2:
        print('2x1  =  2')
        print('2x2  =  4')
        print('2x3  =  6')
        print('2x4  =  8')
        print('2x5  =  10')
        print('2x6  =  12')
        print('2x7  =  14')
        print('2x8  =  16')
        print('2x9  =  18')
        print('2x10 =  20')
        print('\n')
        conf = str(input('Digite qualquer tecla para continuar...'))

    elif choicetabuada == 3:
        print('3x1  =  3')
        print('3x2  =  6')
        print('3x3  =  9')
        print('3x4  =  12')
        print('3x5  =  15')
        print('3x6  =  18')
        print('3x7  =  21')
        print('3x8  =  24')
        print('3x9  =  27')
        print('3x10 =  30')
        print('\n')
        conf = str(input('Digite qualquer tecla para continuar...'))

    elif choicetabuada == 4:
        print('4x1  = 4')
        print('4x2  = 8')
        print('4x3  = 12')
        print('4x4  = 16')
        print('4x5  = 20')
        print('4x6  = 24')
        print('4x7  = 28')
        print('4x8  = 32')
        print('4x9  = 36')
        print('4x10 = 40')
        print('\n')
        conf = str(input('Digite qualquer tecla para continuar...'))

    elif choicetabuada == 5:
        print('5x1  = 5')
        print('5x2  = 10')
        print('5x3  = 15')
        print('5x4  = 20')
        print('5x5  = 25')
        print('5x6  = 30')
        print('5x7  = 35')
        print('5x8  = 40')
        print('5x9  = 45')
        print('5x10 = 50')
        print('\n')
        conf = str(input('Digite qualquer tecla para continuar...'))

    elif choicetabuada == 6:
        print('6x1  = 6')
        print('6x2  = 12')
        print('6x3  = 18')
        print('6x4  = 24')
        print('6x5  = 30')
        print('6x6  = 36')
        print('6x7  = 42')
        print('6x8  = 48')
        print('6x9  = 54')
        print('6x10 = 60')
        print('\n')
        conf = str(input('Digite qualquer tecla para continuar...'))

    elif choicetabuada == 7:
        print('7x1  = 7')
        print('7x2  = 14')
        print('7x3  = 21')
        print('7x4  = 28')
        print('7x5  = 35')
        print('7x6  = 42')
        print('7x7  = 49')
        print('7x8  = 56')
        print('7x9  = 63')
        print('7x10 = 70')
        print('\n')
        conf = str(input('Digite qualquer tecla para continuar...'))

    elif choicetabuada == 8:
        print('8x1  = 8')
        print('8x2  = 16')
        print('8x3  = 24')
        print('8x4  = 32')
        print('8x5  = 40')
        print('8x6  = 48')
        print('8x7  = 56')
        print('8x8  = 64')
        print('8x9  = 72')
        print('8x10 = 80')
        print('\n')
        conf = str(input('Digite qialquer tecla para continuar...'))

    elif choicetabuada == 9:
        print('9x1  = 9')
        print('9x2  = 18')
        print('9x3  = 27')
        print('9x4  = 36')
        print('9x5  = 45')
        print('9x6  = 55')
        print('9x7  = 64')
        print('9x8  = 73')
        print('9x9  = 82')
        print('9x10 = 90')
        print('\n')
        conf = str(input('Digite qualquer tecla para continuar...'))

    elif choicetabuada == 10:
        print('10x1  = 10')
        print('10x2  = 20')
        print('10x3  = 30')
        print('10x4  = 40')
        print('10x5  = 50')
        print('10x6  = 60')
        print('10x7  = 70')
        print('10x8  = 80')
        print('10x9  = 90')
        print('10x10 = 100')
        print('\n')
        conf = str(input('Digite qualquer tecla para continuar...'))

    elif choicetabuada == 0:
        print('Saindo em... 3')
        time.sleep(1)
        print('Saindo em... 2')
        time.sleep(1)
        print('Saindo em... 1')
        on == False
        break