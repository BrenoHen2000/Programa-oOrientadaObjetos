#Crie a classe Carro com os atributos modelo, ano, velocidade. 
# Adicione os métodos: acelerar(): aumenta velocidade em 10. 
# frear(): diminui velocidade em 10, mas nunca abaixo de 0. 
# exibir_velocidade()

class Carro:
    def __init__(self, modelo, ano, velocidade):
        self.modelo = modelo
        self.ano = ano
        self.velocidade = velocidade

    def acelerar (self):
        self.velocidade += 10

    def frear(self):
        if self.velocidade != 0:
            self.velocidade -= 10
        else:
            print("carro esta parado")

    def exibir_velocidade(self):
        if self.velocidade != 0:
            print(f"a velocidade é {self.velocidade}")
        else:
            print("carro esta parado")

carro1 = Carro("fiesta", "2018", 0)
carro1.acelerar()
carro1.frear()
carro1.exibir_velocidade()
