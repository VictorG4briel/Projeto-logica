from Personagem import Characters

class warrior(Characters):
    def __init__(self,name):
        super().__init__(name,life=30,attack=15,defense=20)
    # equipamento 
        self.armor_name = "Hemodrenario"
        self.armor_bonus = 8  
        self.pocao_uses = 1  
        
    def attack_special(self, alvo):
        dano = self.attack * 2
        print(f'{self.name} usou Golpe duplo!')
        alvo.receber_dano(dano)
        return dano