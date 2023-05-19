import datetime

on = True
iteration = 1


while on:
    print('=' * 50)
    print('<<< Fy31 >>>\n')

    IDcli = str(input('ID do Cliente: C-'))
    quantDome = int(input('Quantas Câmeras Dome?\n'))
    quantBullet = int(input('Quantas Bullet?\n'))
    print('\n')
 
    def Dome_1():
         # Câmera Dome + Suporte Completo
             tipoCampo = "Society"
             cameraDome = 1
             suportesDome = 1
             borrachaVedacaoTampaSuporteDome = 1
             tampaSuporteDome = 1
             parafusoFecharTampaSuporteDome = 4
             parafusoPrendCameraDome = 3
             porcaPrendeCameraDome = 3
             adesivoInstrucaoPS = 1
             
             # Botão + Suporte para prendelo Completo
             botoeira = 1
             botaoCogumelo = 1
             parafusoAliparaBotao = 1

             chapaFerroAtrazDaBotoeira = 2
             parafusoPrendeChapaNaBotoeira = 4
             porcaParaParafusonaDaBotoeira = 4

             parafusoTravante = 4
             chapaFerroTravanteLisa = 2
             arruela = 4
             arruelaDePressao = 4
             porca = 4
             
             print("<<< Material Necessário: >>>")
             print('Tipo de campo: ' + tipoCampo)
             print('Câmeras Dome: ', cameraDome)
             print(suportesDome)
             print(borrachaVedacaoTampaSuporteDome)
             print(tampaSuporteDome)
             print(parafusoFecharTampaSuporteDome)
             print(parafusoPrendCameraDome)
             print(porcaPrendeCameraDome)
             print(adesivoInstrucaoPS)
             
             print(botoeira)
             print(botaoCogumelo)
             print(parafusoAliparaBotao)
             print(chapaFerroAtrazDaBotoeira)
             print(parafusoPrendeChapaNaBotoeira)
             print(porcaParaParafusonaDaBotoeira)
             print(parafusoTravante)
             print(chapaFerroTravanteLisa)
             print(arruela)
             print(arruelaDePressao)
             print(porca)
             
    if quantDome == 0 and quantBullet == 0:
         Error01 = input('Erro! Valor Inválido\n')

    if quantDome == 1 and quantBullet == 0:
         Dome_1()

    if quantDome == 2 and quantBullet == 0:
         Dome_2()
           



    #   Armazenando Dados No Bloco de Notas
    dados = f" ID do Cliente: C-{IDcli}\n Quantidade de Câmeras Dome: {quantDome}\n Quantidade de Câmeras Bullet: {quantBullet}"
    nome_arquivo = f"C-{IDcli}.txt"
    
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(dados)
    iteration += 1
    
    #   Le o arquivo txt
    #with open('C-50.txt', 'r') as arquivo:
     #       conteudo = arquivo.read()
      #      print(conteudo)



    #   Loop
    choice = input("Você quer Continuar? (yes/no): ")
    if choice.lower() == "no":
        on = False

        

