from Personagem import Characters

class archer(Characters):
    def __init__(self, name):
        # stats base
        super().__init__(name, life=30, attack=15, defense=8)
        # equipamento 
        self.weapon_name = "Flecha Explosiva"
        self.weapon_bonus = 5  
        self.pocao_uses = 1  

    def special_attack(self, alvo):
        ataque_total = self.attack + self.weapon_bonus
        dano = ataque_total + 5 - alvo.defense
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