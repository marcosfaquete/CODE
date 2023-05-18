"""
Definindo Funções

- Funções são pequenas partes de código que realizam tarefas especificas;
- Pode ou não receber entradas de dados e retornar uma saída de dados;
- Muito uteis para executar procedimentos similares por repetidas vezes;

OBS: Se você escrever uma função q ue realiza várias tarefas dentro dela;
é bom fazer uma verificação para que a função seja simplificada.

Já utilizamos várias funções desde que iniciamos este curso:
- print()
- len()
- max()
- min()
- count()
- e muitas outras:

"""

# Exemplo de utilização de funções:
# Dado tipo lista
cores = ['verde', 'amarelo', 'azul', 'branco']

# Utilizando a função integrada (Built-in) do Python print()
print(cores)

# Dado tipo string
curso = 'Programação em Python: Essencial'
print(curso)

cores.append('roxo') # append('') adiciona um dado em uma lista
print(cores)

# Modo errado de utilizar append, não se pode utiliza-lo em qualquer lugar.
#curso.append('Mais dados...') # AttributeError
#print(curso)

cores.clear() # clear() ele limpa os dados da lista, não recebe nenhum parametro.
print(cores)

print(help(print)) # help pode se utilizar para ver mais detalhes das funções.
# DRY - Don't repeat yourself - Não repita você mesmo / Não repita seu código.

# Mas então, como definir funções?

"""
Em Python, a forma geral de definir uma função é:

def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao
    
Onde:

nome_da_funcao -> SEMPRE, com letras minúsculas, e se for nome composto, separado por underline (Snake Case)
parametros_de_entrada -> Opcionais, onde tendo mais de um, cada um separado por virgula, podendo ser opcionais ou não;
bloco_da_funcao -> Também chamado de corpo da função ou da implementação, é onde o processamento da função acontece.
Neste bloco, pode ter ou não retorno da função.

OBS: Veja que para definir uma função, utilizamos a palavra reservada 'def' informando ao Python que estamos definindo uma função
Também abrimos o bloco de código com o já conhecido dois pontos : que é utilizado em Python para definir blocos.

"""

# Definindo a primeira função
# Definição
def diz_oi():
    print('Oi!')

"""
OBS:
1 - Veja que, dentro das nossas funções podemos utilizar outras funções;
2 - Veja que nossa função só executa uma tarefa, ou seja, a única coisa que ela faz é dizer oi;
3 - Veja que esta função não recebe nenhum parâmetro de entrada;
4 - Veja que esta função não retorna nada;
"""

# Utilizando funções
# Chamada de Execução
diz_oi()

"""
ATENÇÃO:
Nunca esqueça de utilizar o parênteses ao executar uma função.

Exemplo:

# Errado:
diz_oi

# Certo
diz_oi()

# Errado
diz oi ()

"""

# Exemplo 2

def cantar_parabens():
    print('Parabéns pra você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print('Viva o aniversariante!')

cantar_parabens()
cantar_parabens() # pode se chamar a função quantas vezes quiser desta maneira

# pode se chamar com o range também.
for n in range(5):
    print(n)     # printa a sequencia de numeros.
    cantar_parabens()


# Em Python, podemos inclusive criar variáveis do tipo de uma função e executar esta função através da variável.
# Exemplo

# Essa variável canta vai receber a execução do metodo cantar parabens.
# pode-se fazer mas não é recomendado.
canta = cantar_parabens()

canta()




