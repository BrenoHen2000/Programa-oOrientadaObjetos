class Pet:
    def __init__ (self, nome, peso): #criamos os objetos
        self.nome = nome
        self.peso = peso

    def imprimir_pet (self):
        print(f'nome do pet:' ,  {self.nome})
        print(f'peso do pet:' ,  {self.peso})
    
    def AlimentarPet (self, comida):
        self.peso + comida

class abrigo:
    catalogo = []

    def AdicionarPet (self, pet):
        self.catalogo.append(pet)

    def ImprimirAbrigo (self):
        print('pets no abrigo')
        print('--------------')
        
        for pet in self.catalogo:
            pet.imprimir_pet()
            print('--------------')


abrigo1 = abrigo()

pet = Pet('jujubba', 10)
abrigo1.AdicionarPet(pet)

pet = Pet('zoio', 15)
abrigo1.AdicionarPet(pet)

pet = Pet('noia', 215428)
abrigo1.AdicionarPet(pet)

abrigo1.ImprimirAbrigo()