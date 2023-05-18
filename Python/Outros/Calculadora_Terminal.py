
import time;

print('\n')
name_admin = str(input("Ola, qual é o seu nome? \n"))
print("\n")
print("Olá {}, é um prazer te conhecer!".format(name_admin.capitalize()))


on = True

while on == True:
    print('\n')
    print('[1]>> Adição')
    print('[2]>> Divisão')
    print('[3]>> Subtração')
    print('[4]>> Multiplicação')
    choice_admin = int(input("Digite sua escolha {}\n".format(name_admin.capitalize())))

    if choice_admin == 1:
        print('\n')
        time.sleep(1)
        print('<<< Adição >>>')
        time.sleep(1)
        print("Olá {}, digite os números que deseja Somar...".format(name_admin.capitalize()))
        adicao_n1 = int(input("Digite o Primeiro Número: "))
        adicao_n2 = int(input("Digite o Segundo Número: "))
        time.sleep(1)
        resul_adicao = (adicao_n1 + adicao_n2)
        print('\n')
        print('O resuldado da Adição entre {} e {} é: {}'.format(adicao_n1, adicao_n2, resul_adicao))
        print('\n')
        exit_confirm = input("Digite Qualquer tecla para continuar...")

    elif choice_admin == 2:
        print('\n')
        time.sleep(1)
        print("<<< Divisão >>>")
        time.sleep(1)
        print("Olá {}, digite os números que deseja Dividir...".format(name_admin.capitalize()))
        div_n1 = int(input("Digite o Primeiro Número: "))
        div_n2 = int(input("Digite o Segundo Número: "))
        time.sleep(1)
        resul_div = (div_n1 / div_n2)
        print('\n')
        print('O resultado da Divisão entre {} e {} é: {}'.format(div_n1, div_n2, resul_div))
        print('\n')
        exit_confirm = input("Digite Qualquer tecla para continuar...")

    elif choice_admin == 3:
        print('\n')
        time.sleep(1)
        print("<<< Subtração >>>")
        time.sleep(1)
        print("Olá {}, digite os números que deseja Subtrair...".format(name_admin.capitalize()))
        sub_n1 = int(input("Digite o Primeiro Número: "))
        sub_n2 = int(input("Digite o Segundo Número: "))
        resul_sub = (sub_n1 - sub_n2)
        print('\n')
        print('O resultado da Subtração entre {} e {} é: {}'.format(sub_n1, sub_n2, resul_sub))
        print('\n')
        exit_confirm = input("Digite Qualquer tecla para continuar...")

    elif choice_admin == 4:
        print('\n')
        time.sleep(1)
        print("<<< Multiplicação >>>")
        time.sleep(1)
        print("Olá {}, digite os números que deseja Multiplicar...".format(name_admin.capitalize()))
        mult_n1 = int(input("Digite o Primeiro Número: "))
        mult_n2 = int(input("Digite o Segundo Número: "))
        resul_mult = (mult_n1 * mult_n2)
        print('\n')
        print("O resultado da Multiplicação entre {} e {} é: {}".format(mult_n1, mult_n2, resul_mult))
        print('\n')
        exit_confirm = input("Digite Qualquer tecla para continuar...")

    elif choice_admin == input():
        print('Enter Digitado')



        # IDEIA DE USAR O FOR PARA PERGUNTAR QUANTOS NUMEROS DESEJA SOMAR OU IR PERGUNTANDO EX:
        # ou criar um comando que quando apertado ele pede a entrada de um novo numero para ser somado com os anteriores
        #e assim sucessivamente






