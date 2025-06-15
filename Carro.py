class Carro:
    def __init__(self):
        self.ligado = False
        self.cor = ''
        self.modelo =  ''
        self.velocidade = 0

    
    def liga(self):
        self.ligado = True

    def desliga(self):
        self.ligado = False

    def acelera(self):
        self.velocidade += 10
        

    def desacelera (self):
            self.velocidade -= 10

Carro1 = Carro ()

Carro1.liga()
Carro1.acelera()
Carro1.acelera()

print (Carro1.ligado)
print (Carro1.velocidade)

