# Crie uma classe Pessoa com os atributos nome e idade. Em seguida, crie um método apresentar que imprime "Olá, meu nome é X e tenho Y anos."

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def apresentar(self):
        print (f"Olá, meu nome é {self.nome} e tenho {self.idade} anos")
    
pessoa1 = Pessoa("maria", idade=20)
pessoa2 = Pessoa(nome="joao", idade=25)

pessoa1.apresentar()
pessoa2.apresentar()

