import time  # Importação da biblioteca para usar time.

on = True  # Declarando variáveis booleanas.

print('\n')
while on == True:  # Enquanto variável (on) for verdadeira faça isso.
    print('\033[1;31m       # Menu #\033[m')
    print('\033[1;31m[1]\033[m \033[1;34mCadastrar Clientes')  # \033[1:31m textocolorido \033[m
    print('\033[1;31m[2]\033[m \033[1;34mConsultar Clientes')  # Códigos de cores.
    print('\033[1;31m[3]\033[m \033[1;34mSair\033[m')

    # Se variável choice receber o número 1 faça isso.
    choice = int(input('\033[1;32mDigite sua escolha: \033[m'))
    if choice == 1:
        print('\n')
        print('\033[1;31m# Cadastro de Clientes #\033[m')
        # print('\033[33mDigite o nome do cliente que deseja cadastrar\033[m')
        codigo = int(input('\033[1;34mCadastre um ID para o cliente: \033[m'))
        nome_1 = str(input('\033[1;34mNome do Cliente: \033[m'))
        data_nasc = str(input('\033[1;34mData de Nascimento: \033[m'))
        sexo = str(input('\033[1;34mSexo: \033[m'))
        endereco = str(input('\033[1;34mEndereço: \033[m'))
        celular = str(input('\033[1;34mCelular: \033[m'))
        print('\n\033[1;32mCliente Cadastrado com Sucesso!\033[m')
        print('\033[1;34mRetornando ao Menu Principal em\033[m \033[1;32m3\033[m')
        time.sleep(1)
        print('\033[1;34mRetornando ao Menu Principal em\033[m \033[1;33m2\033[m')
        time.sleep(1)
        print('\033[1;34mRetornando ao Menu Principal em\033[m \033[1;31m1\033[m\n')
        time.sleep(1)

    # Se variável choice receber o número 2 faça isso.
    elif choice == 2:
        print('\n')
        print('\033[1;31m# Consulta de Clientes #\033[m')
        finder = int(input('\033[1;32mDigite o ID para pesquisar: \033[m'))
        print('\n')
        if finder == codigo:
            print('\033[1;32m#Nome do Cliente Encontrado #\033[m')
            print('\033[1;34mCódigo do Cliente:\033[m {}'.format(codigo))
            print('\033[1;34mNome: \033[m{}'.format(nome_1.capitalize()))
            print('\033[1;34mData Nascimento: \033[m{}'.format(data_nasc))
            print('\033[1;34mSexo: \033[m{}'.format(sexo.capitalize()))
            print('\033[1;34mEndereço: \033[m{}'.format(endereco.capitalize()))
            print('\033[1;34mCelular:\033[m {}'.format(celular))
            time.sleep(1)
            cont1 = str(input('\033[1;35mDigite alguma tecla para continuar...\033[m\n'))
            print('\033[1;34mRetornando ao Menu Principal em\033[m \033[32m3\033[m')
            time.sleep(1)
            print('\033[1;34mRetornando ao Menu Principal em\033[m \033[33m2\033[m')
            time.sleep(1)
            print('\033[1;34mRetornando ao Menu Principal em\033[m \033[31m1\033[m\n')
            time.sleep(1)

        else:
            print('\n\033[1;31m# Código Não Encontrado #\033[m\n')
            cont2 = str(input('\033[1;35mDigite alguma tecla para continuar...\033[m\n'))
            print('\033[1;34mRetornando ao Menu Principal em\033[m \033[1;32m3\033[m')
            time.sleep(1)
            print('\033[1;34mRetornando ao Menu Principal em\033[m \033[1;33m2\033[m')
            time.sleep(1)
            print('\033[1;34mRetornando ao Menu Principal em\033[m \033[1;31m1\033[m\n')
            time.sleep(1)

    # Se variável choice receber o número 3 faça isso.
    elif choice == 3:
        on == False
        print('\033[1;34mSaindo do programa em\033[m \033[32m3\033[m')
        time.sleep(1)
        print('\033[1;34mSaindo do programa em\033[m \033[33m2\033[m')
        time.sleep(1)
        print('\033[1;34mSaindo do programa em\033[m \033[31m1\033[m')
        time.sleep(1)
        break


    elif choice != 1 & 2 | 3:
        print('\n')
        print('\033[1;32mCódigo Inválido!\033[m')
        print('\n')
