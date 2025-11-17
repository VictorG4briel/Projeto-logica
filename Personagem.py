class Characters():
    def __init__(self,name,life,attack,defense):
        self.__name= name
        self.__life = life
        self.__max_life = life
        self.__attack = attack
        self.__defense = defense
        # bônus padrão
        self.weapon_bonus = 0
        self.armor_bonus = 0
        self.pocao_uses = 0

    #getters
    @property
    def name(self):
        return self.__name
    
    @property
    def life(self):
        return self.__life
    
    @property
    def attack(self):
        return self.__attack
    
    @property
    def defense(self):
        # retorna defesa base + bônus de armadura (se existir)
        return self.__defense + getattr(self, 'armor_bonus', 0)
    
    @property
    def max_life(self):
        return self.__max_life
    
    #Settres
    @name.setter
    def name(self,name):
        self.__name=name
    
    @life.setter
    def life(self,life):
        self.__life=life
    
    @attack.setter
    def attack(self,attack):
        self.__attack=attack

    @defense.setter
    def defense(self,defense):
        self.__defense=defense

    #Função de ataque 
    def atacar(self, alvo):
        bonus_arma=getattr(self,'weapon_bonus',0)
        ataque_total=self.attack + bonus_arma
        dano = ataque_total - alvo.defense
        if dano < 0:
            dano = 0
        alvo.receber_dano(dano)
        return dano
    #funçao de usar poção
    def usar_pocao(self,quantidade=30): 
        print(f'{self.name} usou uma poção!')
        return self.curar(quantidade)
    
    #função de curar
    def curar(self,quantidade):
        vida_anterior = self.life
        nova_vida=self.life + quantidade
        if (nova_vida > self.__max_life):
            nova_vida = self.__max_life
        self.life = nova_vida
        print(f'{self.name} recuperou {self.life - vida_anterior} HP (Vida: {self.life}/{self.max_life})')
        return self.life
    
    #função de receber dano
    def receber_dano(self, dano):
        self.__life -= dano
        if self.__life < 0:
            self.__life = 0 
    
   
    #Functions
    def __str__(self):
        return(
            f'Nome do Personagem: {self.__name}\n'
            f'Vida: {self.__life}/{self.__max_life}\n'
            f'Attack: {self.__attack}\n'
            f'Defesa: {self.defense}\n'
        )
    
    
#instances
if __name__ == "__main__":
    personagem = Characters('Victor', 20, 10, 30)
    print(personagem)