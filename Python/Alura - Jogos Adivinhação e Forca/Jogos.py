import Adivinhacao
import Forca

def escolhe_jogo():

    print('\n')
    print('=' * 30)
    print('Escolha seu jogo!')
    print('=' * 30)

    print('(1)Adivinhação (2)Forca')

    jogo = int(input('Qual jogo?'))

    if(jogo == 1):
        print('Jogando Adivinhação')
        Adivinhacao.jogar()

    elif(jogo == 2):
        print('Jogando Forca')
        Forca.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()

    print(hello)