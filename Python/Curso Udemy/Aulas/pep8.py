"""
PEP8 - Python Enhancement Proposal

São propostas de melhorias para a linguagem Python

The Zen of Python

import this

A idéia da PEP8 é que possamos escrever código Python de forma
Pythônica.

-------------------------------------------------------------------------------------------------

[1] - Utilize Camel Case para nomes de classes;

# Exemplos de Classes e Suas Funções
class Calculadora:
    pass


class CalculadoraCientifica:
    pass

-------------------------------------------------------------------------------------------------

[2] - Utilize nomes em minúsculo, separados por underline para funções ou variávveis:
def soma() :
    pass

def soma_dois() :
    pass

-------------------------------------------------------------------------------------------------

Declaração de variável

numero = 4

numero_impar = 3

-------------------------------------------------------------------------------------------------

[3] - Utilize 4 espaços para identação!
"""

if 'a' in 'banana':
    print('Tem')

"""
[4] - Linhas em branco
- Separar funções e definições de classe com duas linhas em branco:
- Métodos dentro de uma classe devem ser separados com uma única linha em branco:

-------------------------------------------------------------------------------------------------

[5] - imports

- Imports devem ser sempre feitos em linhas separadas;

# Import Errado:
import sys, os

# Import Certo:
import sys
import os

# Não há problemas em utilizar:

#from types import StringType, ListType

# Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:

from types import (
 #   StringType
 #   ListType
 #   SetType
 #   OutroType
)

# Imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentários ou
#docstrings e antes de constantes ou variáveis globais.

-------------------------------------------------------------------------------------------------

"""








