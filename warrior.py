from Personagem import Characters

class Warrior(Characters):
    def __init__(self,name):
        super().__init__(name,life=30,attack=15,defense=13)
        # equipamento 
        self.weapon_name = "Hemodrenario"
        self.weapon_bonus = 5
        self.armor_name = "Desespero eterno"
        self.armor_bonus = 8  
        self.pocao_uses = 1  
        self.ability_uses = 1
        self.special_name = "Golpe Duplo"
        
    def special_attack(self, alvo):
        if getattr(self, 'ability_uses', 0) <= 0:
            print(f'{self.name} não tem usos restantes da habilidade!')
            return 0
        self.ability_uses -= 1
        ataque_total = self.attack + self.weapon_bonus
        dano = ataque_total * 2 - alvo.defense
        if dano < 0:
            dano = 0
        print(f'{self.name} usou Golpe Duplo com {self.weapon_name} causando {dano}!')    
        alvo.receber_dano(dano)
        return dano
    
    