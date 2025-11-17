from Personagem import Characters

class wizard(Characters):
    def __init__(self,name):
        super().__init__(name,life=30,attack=15,defense=20)
    
    def attack_special(self, alvo):
        dano = self.attack + 10
        print(f'{self.name} usou Bola de Fogo!')
        alvo.receber_dano(dano)
        return dano