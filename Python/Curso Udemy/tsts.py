

import time

on = True

while on == True:
    print('\n')
    print('## Menu ##')
    print('[1] Cadastrar')
    print('[2] Consultar')
    print('[3] Sair')
    choice = int(input('Digite sua opção: '))

    if choice == 1:
        print('\n')
        print('## Cadastro de Clientes ##')
        Cli_id = int(input('Código ID: '))
        Cli_name = str(input('Nome: '))
        Cli_idade = int(input('Idade: '))
        Cli_cel = int(input('Cel: '))

    elif choice == 2:
        print('\n')
        print('## Consulta de Clientes ##')
        Cli_pesq = int(input('Digite o ID do Cliente: '))

        if Cli_pesq == Cli_id:
            print('\n')
            print('Cliente Encontrado!')
            print(Cli_id)
            print(Cli_name)
            print(Cli_idade)
            print(Cli_cel)
            stop = input('Digite qualquer tecla para continuar...')

        else:
            print('Cliente não encontrado')
            stop = input('Digite qualquer tecla para continuar...')


    elif choice == 3:
        print('\n')
        print('## Saindo do Programa ##')
        on = False

