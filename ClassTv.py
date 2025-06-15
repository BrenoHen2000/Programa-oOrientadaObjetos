class Tv:
    def __init__(self):
        self.canal = 1
        self.volume = 30
        self.volume_min = 0
        self.volume_max = 100
        self.canal_min = 1
        self.canal_max = 99
        self.ligada = False
#--------------------------------------------------------
    def ligar(self):
            self.ligada = True

    def desligar(self):
            self.ligada = False
#--------------------------------------------------------
    def mudar_canal_para_cima(self):
        if not self.ligada:
            return
            
        if self.canal < self.canal_max:
            self.canal += 1
        
    def mudar_canal_para_baixo (self):
        if not self.ligada:
            return
            
        if self.canal < self.canal_min:
            self.canal -= 1
#--------------------------------------------------------      
    def reduzir_volume (self):
        if not self.ligada:
            return
             
        if self.volume > self.volume_min:
            self.volume -= 10

    def aumentar_volume (self):
        if not self.ligada:
            return
            
        if self.volume < self.volume_max:
            self.volume += 10     
#--------------------------------------------------------      
#metodo string
    def __str__(self) -> str:
        return f'tv esta ligada {self.ligada} - canal {self.canal}'

#------testando metodo ligar ou desligar-----------------
minha_tv = Tv()
print("a tv esta ligada? ", minha_tv.ligada)

minha_tv.ligar()
print("a tv esta ligada agora? ", minha_tv.ligada)

#minha_tv.desligar() #coloquei em comentário para acionar a função de aumentar volume e tv
#print("a tv esta ligada agora? ", minha_tv.ligada)

#------testando metodo mudar canal -----------------
minha_tv.mudar_canal_para_baixo()
print(minha_tv.canal)


minha_tv.mudar_canal_para_cima()
print(minha_tv.canal)


#------testando metodo mudar volume -----------------
minha_tv.aumentar_volume()
print(minha_tv.volume)

minha_tv.reduzir_volume()
print(minha_tv.volume)
