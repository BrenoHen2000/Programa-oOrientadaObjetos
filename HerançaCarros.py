
#Crie uma classe base Veiculo com atributos marca e modelo. Crie classes filhas como Carro, Moto e Caminhao, cada uma com um método específico.

class veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca  
        self.modelo = modelo
      

    def mostrar_dados(self):
        print("--------------------------------------------")
        print(f"Marca: {self.marca} e modelo: {self.modelo}")

class moto (veiculo):
    def  empinar(self):
        print(f"a {self.marca} {self.modelo} esta espinando")

class carro (veiculo):
    def ligar_ar(self):
        print(f"o  {self.marca} {self.modelo} esta com o ar esta ligado")

class caminhao (veiculo):
    def bozinou(self):
        print(f"o  {self.marca} {self.modelo} bozinou")


titan = moto ("honda", "titan")
corolla = carro ("toyota", "corolla")
scania = caminhao ("scania", "R")

titan.mostrar_dados()
titan.empinar()

corolla.mostrar_dados()
corolla.ligar_ar()

scania.mostrar_dados ()
scania.bozinou()
