import random

def jogar():

    print('\n')
    print('=' * 30)
    print('Bem vindo ao jogo Adivinhação')
    print('=' * 30)

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    print('Escolha o nível de dificuldade?', numero_secreto)
    print('(1)Fácil (2)Médio (3)Difícil')

    nivel = int(input('Escolha o nível: '))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas +1):
        print('Tentativa {} de {}'.format(rodada, total_de_tentativas))

        chute_jogador = int(input('Digite o seu número: '))
        print('Você digitou:', chute_jogador)

        if(chute_jogador < 1 or chute_jogador > 100):
            print('Você deve digitar um número entre 1 e 100!')
            continue

        acertou = chute_jogador == numero_secreto
        maior = chute_jogador > numero_secreto
        menor = chute_jogador < numero_secreto

        if(acertou):
            print('Parabéns! Você acertou! e fez {} pontos!'.format(pontos))
            break

        else:
            if(maior):
                print('Você errou! O seu chute foi maior que o número secreto. \n')

            elif(menor):
                print('Você errou! O seu chute foi menor que o número secreto. \n')
            pontos_perdidos = abs(numero_secreto - chute_jogador)
            pontos = pontos - pontos_perdidos

    print("\n>>> Fim do jogo <<<\n")

if(__name__ == "__main__"):
    jogar()
