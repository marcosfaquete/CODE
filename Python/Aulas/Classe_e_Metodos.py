# Class
# Syntaxe
# Marca, Memoria Ram, Placa de Video

# INIT é chamado de construtor e ele permite criar a funcionalidade inicial que sua classe terá
# Self serve para que você acesse as propriedades ou métodos de uma instância

#Exemplo 1 Classes, remover o comentario para executar
"""
class Computador:
    def __init__(self, marca, memoria_ram, placa_de_video):
            self.marca = marca
            self.memoria_ram = memoria_ram      # Atributos dentro da classe
            self.placa_de_video = placa_de_video
    pass

computador1 = Computador('Asus','8gb','Nvidia')
computador2 = Computador('Dell','10gb','GeForce')
computador3 = Computador('Acer','16gb','ATM')
print(computador1.marca,computador1.memoria_ram,computador1.placa_de_video)
print(computador2.marca,computador2.memoria_ram,computador2.placa_de_video)
print(computador3.marca,computador3.memoria_ram,computador3.placa_de_video)

"""
#======================================================================================

# Exemplo 2 Chamando o Método

class Computador:
    def __init__(self,marca,memoria_ram,placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram      # Atributos dentro da classe
        self.placa_de_video = placa_de_video

    def Ligar(self):                # Definindo método Ligar
        print('Estou Ligando')      # Fazendo a Logica para ligar

    def Desligar(self):             # Método Desligar
        print('Estou Desligando')

    def ExibirInformacoesDesteComputador(self): # Criando um método que vai usar parametros
        print(self.marca, self.memoria_ram, self.placa_de_video)

computador1 = Computador('Asus','16gb','Nvidia')
computador1.Ligar()
computador1.Desligar()
computador1.ExibirInformacoesDesteComputador()
