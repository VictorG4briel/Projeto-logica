from Personagem import Characters

class archer(Characters):
    def __init__(self,name):
        super().__init__(name,life=30,attack=15,defense=20)
    
    def special_attack(self, alvo):
        dano = self.attack * + 5
        print(f'{self.name} usou Chuva de Flechas!')
        alvo.receber_dano(dano)
        return dano