from Personagem import Characters

class warrior(Characters):
    def __init__(self,name):
        super().__init__(name,life=30,attack=15,defense=20)
    
    def especial_attack(self, alvo):
        dano = self.attack * 2
        print(f'{self.name} usou Golpe duplo!')
        alvo.receber_dano(dano)
        return dano