# Crie uma classe Retangulo que receba largura e altura. Adicione métodos para calcular área e perímetro.

class Retangulo():
    def __init__(self, largura, altura):
        self.altura = altura
        self.largura = largura 
    
    def area(self):
        return self.largura * self.altura

retangulo1 = Retangulo(4,2)
print(retangulo1.area())