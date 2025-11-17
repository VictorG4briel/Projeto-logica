from Personagem import Characters

class Paladin(Characters):
    def __init__(self,name):
        super().__init__(name,life=30,attack=15,defense=20)
    
    def special_attack(self, alvo):
        dano = self.attack + 5
        cura = self.defense // 2
        
        print(f'{self.name} usou Golpe duplo!')
        alvo.receber_dano(dano)
        self.life = cura
        return dano