import time
print('=' * 25)
name = str(input('Olá, qual é o seu nome? \n'))
time.sleep(1)
print('Seja bem vindo, {}!'.format(name.capitalize()))
time.sleep(1)
print('=' * 25)

on = True
while on == True:
    print('\n')
    print('O que gostaria de saber hoje?')
    print('\n')
    print('[1] - Vale a pena aprender Python?')
    time.sleep(1)
    print('[2] - Quanto tempo leva para conseguir um emprego com Python?')
    time.sleep(1)
    print('[3] - Quanto vou saber que estou Bom o suficiente para conseguir um emprego?')
    time.sleep(1)
    print('[4] - Onde me recomenda estudar Python para conseguir um emprego hoje?')
    time.sleep(1)
    print('[5] - Sair')

    choice = int(input('Digite o número de sua opção: '))
    print('\n')
    if choice == 1:
        print('{} na minha visão vale muito apena, isso porque Python é uma das linguagens que mais cresce no mundo e possui \n'
              'salários mensais que vão desde R$2.100 a até mais R$10.000 no Brasil, além de contar com uma média anual\n'
              'de $85.000 dolares nos EUA.'.format(name.capitalize()))
        confirm = str(input('Digite qualquer tecla para continuar...'))

    elif choice == 2:
        print('{} isso varia muito com o nível de esforço, dedicação e busca diária por vagas de cada indivíduo\n'
              'Alguns conseguem com menos de 3 meses e outros com mais, tudo depende do quanto você já sabe ou\n'
              'está disposto a correr atrás para aprender.'.format(name.capitalize()))
        confirm = str(input('Digite qualquer tecla para continuar...'))

    elif choice == 3:
        print('{} primeiro entenda, ninguém vai te dizer ou chegar magicamente um dia e te dizer que você\n'
              'está BOM o suficiente para conseguir um emprego ou fazer dinheiro com seu conhecimento de \n'
              'programação, seja em Python ou qualquer outra linguagem ou habilidade, você simplesmente\n'
              'tem que começar dar a sua cara a tapa e começar a aplicar para oportunidadades ou até \n'
              'mesmo começar a criar elas, desde o dia que você já domina os fundamentos de uma linguagem\n'
              '(se estamos falando de Python, recomendo aprender no mínimo os 5 pilares de programação.'.format(name.capitalize()))
        confirm = str(input('Digite qualquer tecla para continuar...'))

    elif choice == 4:
        print('{} você pode estudar através de vídeos gratuitos no YouTube, livros e sites de programação\n'
              'porém se buscar um lugar com suporte 1 a 1, estrutura sequencial, projetos novos todos os meses\n'
              'do ano e um curso que vai te ensinar toda a base e habilidades mais lucrativas que precisa para\n'
              'criar aplicações em Python e estar prointo para o mercado, recomendo o cursodepython.net.'.format(name.capitalize()))
        confirm = str(input('Digite qualquer tecla para continuar...'))

    elif choice == 5:
        print('Saindo do programa em 3')
        time.sleep(1)
        print('Saindo do programa em 2')
        time.sleep(1)
        print('Saindo do programa em 1')
        break





