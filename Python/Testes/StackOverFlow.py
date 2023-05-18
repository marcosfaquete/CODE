def return_int():
    try: 
        QuantidadeCabos = int(input("Digite a quantidade de cabos: "))
    except ValueError as err: # formato errado
        print('Formato errado')
    else: # caso o try seja bem sucedido, haja o cast para int
        if(3 < QuantidadeCabos < 6): # verificamos se QuantidadeCabos maior que 3 e menor que 6
            return QuantidadeCabos # tudo bem, retornar valor
        print("Digite um valor entre 3 e 6!")
    return return_int() # repetir a pergunta

print("Quantidade de cabos: ", return_int())