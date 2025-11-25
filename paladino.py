from Personagem import Characters

class Paladin(Characters):
    def __init__(self,name):
        super().__init__(name,life=25,attack=14,defense=11)
        # equipamento
        self.weapon_name = "Ruptor Divino"
        self.weapon_bonus = 5
        self.armor_name = "Hooker Lamurico"
        self.armor_bonus = 6
        self.potion_uses = 2  
        self.ability_uses = 1
        self.special_name = "Golpe Sagrado"
    
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
        print(f'{self.name} usou Golpe Sagrado com {self.weapon_name} causando {dano}!')
        self.curar(cura)
        return dano
    