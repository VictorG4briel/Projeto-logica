class Characters():
    def __init__(self,name,life,attack,defense):
        self.__name= name
        self.__life = life
        self.__attack = attack
        self.__defense = defense

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
        return self.__defense
    
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
        dano = self.__attack - alvo.defense
        if dano < 0:
            dano = 0
        alvo.receber_dano(dano)
        return dano
    
    #função de receber dano
    def receber_dano(self, dano):
        self.__life -= dano
        if self.__life < 0:
            self.__life = 0 
    #Functions
    def __str__(self):
        return(
            f'Nome do Personagem:{self.__name}\n'
            f'Vida:{self.__life}\n'
            f'Attack:{self.__attack}\n'
            f'Defesa:{self.__defense}\n'
        )
    
    
#instances
personagem = Characters('Victor',20,10,30)

#Exit
print(personagem)