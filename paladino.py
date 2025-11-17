from Personagem import Characters

class Paladin(Characters):
    def __init__(self,name):
        super().__init__(name,life=20,attack=10,defense=30)
        # equipamento
        self.weapon_name = "Espada Sagrada"
        self.weapon_bonus = 3
        self.armor_name = "Armadura Divina"
        self.armor_bonus = 10
        self.pocao_uses = 2  
        self.ability_uses = 1
    
    def special_attack(self, alvo):
        if getattr(self, 'ability_uses', 0) <= 0:
            print(f'{self.name} não tem usos restantes da habilidade!')
            return 0
        self.ability_uses -= 1
        ataque_total = self.attack + self.weapon_bonus
        dano = ataque_total + 5 - alvo.defense
        if dano < 0:
            dano = 0
        alvo.receber_dano(dano)
        cura = self.defense // 2
        self.curar(cura)
    
        print(f'{self.name} usou Golpe Sagrado com {self.weapon_name}!')
        return dano