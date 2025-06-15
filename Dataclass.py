from dataclasses import dataclass

#Em Python, dataclass é um decorador (@dataclass) que simplifica a criação de classes usadas principalmente para armazenar dados — como um "atalho" para evitar escrever código repetitivo, como métodos __init__, __repr__, __eq__, etc.
@dataclass
class Cliente:
    nome: str
    email: str
    idade: int

    def exibir (self):
        print (f'nome: {self.nome} email: {self.email} idade = {self.idade}')

breno = Cliente (nome='breno', email='breno.zanoni', idade=25)
print (breno)
print("----------")
breno.exibir()

