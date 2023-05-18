import time 

def Adicao():
    print('\033[1;31m <<< Adição >>> \033[m')
    n_1 = int(input('\033[1;36mDigite um número: \033[m'))
    n_2 = int(input('\033[1;36mDigite outro número: \033[m'))
    resul_soma = (n_1 + n_2)
    print('\033[1;32mO resultado da soma entre {} e {} é: {}\033[m'.format(n_1, n_2, resul_soma))
    print('\n')
    retorna = input('\033[1;31mDigite qualquer tecla para continuar ...\033[m')

def Sub():
    print('\033[1;31m<<< Subtração >>> \033[m')
    n_1 = int(input('\033[1;36mDigite um número: \033[m'))
    n_2 = int(input('\033[1;36mDigite outro número: \033[m'))
    resul_sub = (n_1 - n_2)
    print('\033[1;32mO resultado da Subtração entre {} e {} é: {}\033[m'.format(n_1, n_2, resul_sub))
    print('\n')
    retorna = input('\033[1;31mDigite qualquer tecla para continuar ...\033[m')

def Div():
    print('\033[1;31m<<< Divisão >>> \033[m')
    n_1 = int(input('\033[1;36mDigite um número: \033[m'))
    n_2 = int(input('\033[1;36mDigite outro número: \033[m'))
    resul_div = (n_1 / n_2)
    print('\033[1;32mO resultado da Divisão entre {} e {} é: {}\033[m'.format(n_1, n_2, resul_div))
    print('\n')
    retorna = input('\033[1;31mDigite qualquer tecla para continuar ...\033[m')

def Mult():
    print('\033[1;31m<<< Multiplicação >>> \033[m')
    n_1 = int(input('\033[1;36mDigite um número: \033[m'))
    n_2 = int(input('\033[1;36mDigite outro número: \033[m'))
    resul_mult = (n_1 * n_2)
    print('\033[1;32mO resultado da Multiplicação entre {} e {} é: {}\033[m'.format(n_1, n_2, resul_mult))
    print('\n')
    retorna = input('\033[1;31mDigite qualquer tecla para continuar ...\033[m')

on = True

while on == True:
    print('\n')
    print('\033[1;31m<<< Calculadora >>>\033[m')
    print('\033[1;32m[1]\033[m \033[1;36mAdição\033[m')
    print('\033[1;32m[2]\033[m \033[1;36mSubtração\033[m')
    print('\033[1;32m[3]\033[m \033[1;36mDivisão\033[m')
    print('\033[1;32m[4]\033[m \033[1;36mMultiplicação\033[m')
    print('\033[1;32m[5]\033[m \033[1;36mSair\033[m')
    opcao = int(input('\033[1;31mDigite sua opção: \033[m'))
    print('\n')

    if opcao == 1:
        Adicao()
    
    elif opcao == 2:
        Sub()
    
    elif opcao == 3:
        Div()

    elif opcao == 4:
        Mult()
    
    elif opcao == 5:
        on = False
        time.sleep(1)
        print('\033[1;32mSaindo do programa em 3\033[m')
        time.sleep(1)
        print('\033[1;32mSaindo do programa em 2\033[m')
        time.sleep(1)
        print('\033[1;32mSaindo do programa em 1\033[m')
        time.sleep(1)

    elif opcao != 1 & 2 & 3 & 4 & 5:
        print('\033[1;36mErro! Opção Inválida!\033[m')
        retorna = input('\033[1;31mDigite qualquer tecla para continuar ...\033[m')
    