#Crie a classe ContaBancaria com atributos: titular, saldo. Implemente os métodos:

#depositar(valor); sacar(valor); exibir_saldo(); Valide se há saldo suficiente no saque.

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if  valor > 0:
            self.saldo += valor
            print(f"Deposito de {valor} realizado com sucesso")
        else:
            print("Deposito invalido")

    def sacar (self, valor):
        if valor < self.saldo:
            print (f"Saque de {valor} realizado com sucesso")
            self.saldo -= valor
        else:
            print("Saldo insuficiente")
    
    def exibirsaldo (self):
        print(f" o saldo de {self.titular} é {self.saldo}")

conta1 = ContaBancaria("Maria", 500)
conta1.depositar(100)
conta1.depositar(400)
conta1.sacar(1200)
conta1.exibirsaldo()


