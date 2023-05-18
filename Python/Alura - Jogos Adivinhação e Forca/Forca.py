def jogar():

    print('\n')
    print('=' * 30)
    print('Bem vindo ao jogo Forca')
    print('=' * 30)

    palavra_secreta = 'banana'.upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while(not acertou and not enforcou):
        chute = input('Qual letra? ')
        chute = chute.strip().upper()  #Retira os possíveis espaçoes que o usuário pode digitar.

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra): #upper deixa todas as letras em maiúsculas.
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print('Você ganhou!')
    else:
        print('Você Perdeu!')
    print('Fim do jogo')

if(__name__ == "__main__"):
    jogar()

