class Pessoa:
    def __init__ (self):
        self.idade = 25
        self.nome = "breno"

    def apresentar(self):
        return (f'Ola, meu nome é {self.nome} e tenho {self.idade}')    
    
    def set_nome (self, nome):
        self.nome = nome

    def set_idade (self, idade):
        self.idade = idade


pessoa1 = Pessoa()
print(f'Ola, meu nome é {pessoa1.nome} e tenho {pessoa1.idade} anos')    

pessoa1.set_nome (nome = "luiz")
pessoa1.set_idade (idade = 3251)

print(f'Ola, meu nome é {pessoa1.nome} e tenho {pessoa1.idade} anos')

