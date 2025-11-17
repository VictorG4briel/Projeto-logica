from Personagem import Characters

class archer(Characters):
    def __init__(self, name):
        # stats base
        super().__init__(name, life=20, attack=7, defense=10)
        # equipamento 
        self.weapon_name = "Furacão De Runaan"
        self.weapon_bonus = 5  
        self.pocao_uses = 1  
        self.ability_uses = 1

    def special_attack(self, alvo):
        if getattr(self, 'ability_uses', 0) <= 0:
            print(f'{self.name} não tem usos restantes da habilidade!')
            return 0
        self.ability_uses -= 1
        ataque_total = self.attack + self.weapon_bonus
        dano = ataque_total * 3 - alvo.defense
        if dano < 0:
            dano = 0
        print(f'{self.name} usou Chuva de Flechas com {self.weapon_name}!')
        alvo.receber_dano(dano)
        return dano

    def usar_pocao(self, quantidade=30):
        if getattr(self, 'pocao_uses', 0) <= 0:
            print(f'{self.name} não tem poções restantes!')
            return False
        self.pocao_uses -= 1

        self.curar(quantidade)
        print(f'{self.name} usou uma poção. Poções restantes: {self.pocao_uses}')
        return True