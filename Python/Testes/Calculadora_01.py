import keyword
import time

on = True

while on == True:
    print("\n")
    print("### MENU ###")
    print("\n")
    time.sleep(1)
    print("[1] Adição")
    time.sleep(1)
    print("[2] Divisão")
    time.sleep(1)
    print("[3] Multiplicação")
    time.sleep(1)
    print("[4] Subtração")
    time.sleep(1)
    print("\n")

    choice_user = int(input("Digite sua opção: "))

    if choice_user == 1:
        print("\n")
        print("## ADIÇÃO ##")
        print("Digite os dois números que devem ser SOMADOS:\n")
        time.sleep(1)
        number_01_Adicao = float(input("Digite o Primeiro Número: "))
        number_02_Adicao = float(input("Digite o Segundo Número: "))
        resul_Adicao = (number_01_Adicao + number_02_Adicao)
        print("O resultado da soma entre {} e {} é: {}".format(number_01_Adicao, number_02_Adicao, resul_Adicao))
        choice_user_2 = int(input("Digite qualquer tecla para continuar..."))


    elif choice_user == 2:
        print("\n")
        print("## DIVISÃO ##")
        print("Digite os dois números que devem ser DIVIDIDOS \n")
        time.sleep(1)
        number_01_Divisao = float(input("Digite o Primeiro Número: "))
        number_02_Divisao = float(input("Digite o Segundo Número: "))
        resul_Divisao = (number_01_Divisao / number_02_Divisao)
        print("O resultado da soma entre {} e {} é {}".format(number_01_Divisao, number_02_Divisao, resul_Divisao))
        choice_user_02 = int(input("Digite qualquer telca para continuar..."))

    elif choice_user == 3:
        print("\n")
        print("## MULTIPLICAÇÃO ##")
        print("Digite os dois números que devem ser MULTIPLICADOS \n")
        time.sleep(1)
        number_01_Multiplicador = float(input("Digite o Primeiro Número: "))
        number_02_Multiplicador = float(input("Digite o Segundo Número: "))
        resul_Multiplicacao = (number_01_Multiplicador * number_02_Multiplicador)
        print("O resultado da Multiplicação entre {} e {} é {}".format(number_01_Multiplicador, number_02_Multiplicador, resul_Multiplicacao))
        choice_user_02 = int(input("Digite qualquer tecla para continuar..."))


    elif choice_user == 4:
        print("\n")
        print("## SUBTRAÇÃO ##")
        print("Digite os dois números que devem ser SUBTRAIDOS \n")
        time.sleep(1)
        number_01_Subtracao = float(input("Digite o Primeiro Número: "))
        number_02_Subtracao = float(input("Digite o Segundo Número: "))
        resul_Subtracao = (number_01_Subtracao - number_02_Subtracao)
        print("O resultado da Subtração entre {} e {} é {}".format(number_01_Subtracao, number_02_Subtracao, resul_Subtracao))
        choice_user_2 = int(input("Digite qualquer tecla para continuar..."))





