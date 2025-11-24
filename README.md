# 🎮 Sistema de RPG com Combate por Turnos

## 📋 Descrição

Um sistema de RPG (Role-Playing Game) interativo baseado em turnos, desenvolvido em Python, que permite aos jogadores selecionar diferentes classes de personagens com habilidades únicas, equipamentos específicos e participar de combates estratégicos contra adversários. O sistema implementa conceitos avançados de Programação Orientada a Objetos (POO).

---

## 🎯 Escopo

O projeto fornece:
- **Seleção de Classes**: 4 tipos de personagens (Guerreiro, Paladino, Mago, Arqueiro) com características únicas
- **Sistema de Combate**: Turnos alternados entre dois jogadores
- **Mecânicas de Jogo**: Ataque normal, ataque especial (com usos limitados), uso de poções
- **Equipamento Automático**: Cada personagem é equipado com arma e armadura pré-definidas
- **Progressão de Combate**: Sistema de vida, defesa, ataque e habilidades especiais
- **Interatividade**: Menu baseado em entrada do usuário

---

## ✅ Requisitos Funcionais

### RF1 - Seleção de Personagem
- **Descrição**: O jogador pode escolher entre 4 classes diferentes
- **Entrada**: Número (1-4) + Nome do personagem
- **Saída**: Instância de personagem criada com stats e equipamento configurado

### RF2 - Visualização de Estatísticas
- **Descrição**: Exibição de HP, ATK, DEF, equipamento e habilidade de cada classe antes da seleção
- **Localização**: Função `selecionar_personagem()` em `battle.py`

### RF3 - Sistema de Combate por Turnos
- **Descrição**: Dois jogadores alternam turnos em um combate
- **Ações disponíveis**:
  1. **Ataque Normal**: Calcula dano = (ATK + weapon_bonus) - defesa do alvo
  2. **Ataque Especial**: Habilidade única por classe (com usos limitados)
  3. **Usar Poção**: Recupera 30 HP (usos limitados)
- **Fim do Combate**: Quando um jogador atinge 0 HP

### RF4 - Cálculo de Dano
- **Descrição**: Dano é reduzido pela defesa do alvo
- **Fórmula**: `dano = ataque_total - defesa_alvo` (mínimo de 0)
- **Implementação**: Método `atacar()` em `Personagem.py`

### RF5 - Pontos de Vida (HP)
- **Descrição**: Controle de vida do personagem
- **Funcionalidades**:
  - Receber dano (máximo 0)
  - Recuperar HP via poção ou cura
  - Limite máximo de HP (configurado na classe)

### RF6 - Habilidades Especiais por Classe
- **Guerreiro**: Golpe Duplo (dano = ATK * 2 - DEF, 1 uso)
- **Paladino**: Golpe Sagrado (dano + 5, cura o personagem, 1 uso)
- **Mago**: Bola de Fogo (dano + 10, 2 usos)
- **Arqueiro**: Chuva de Flechas (dano * 3, 2 usos)

---

## ⚙️ Requisitos Não-Funcionais

### Linguagem de Programação
- **Python 3.x**: Linguagem interpretada, orientada a objetos

### Ambiente de Desenvolvimento
- **IDE**: Visual Studio Code (VS Code)
- **Editor Alternativo**: PyCharm, Sublime Text

### Dependências
- Python 3.6 ou superior (sem bibliotecas externas necessárias)
- Sistema Operacional: Windows, macOS, Linux

### Requisitos de Desempenho
- Execução imediata de cálculos
- Interface responsiva baseada em terminal

### Requisitos de Qualidade
- Código legível e bem estruturado
- Encapsulamento de dados privados
- Reutilização de código via herança

---

## 📚 Conceitos de Programação Orientada a Objetos Implementados

### 1️⃣ **ENCAPSULAMENTO**

#### Definição
Encapsulamento é a ocultação dos detalhes internos de uma classe, expondo apenas o que é necessário através de uma interface controlada.

#### Implementação no Código

**Arquivo: `Personagem.py`**

```python
class Characters():
    def __init__(self, name, life, attack, defense):
        # Atributos PRIVADOS (convenção __)
        self.__name = name              # ❌ Não pode ser acessado diretamente
        self.__life = life
        self.__max_life = life
        self.__attack = attack
        self.__defense = defense
        
        # Atributos PÚBLICOS
        self.weapon_bonus = 0           # ✅ Pode ser acessado diretamente
        self.armor_bonus = 0
```

**Vantagens:**
- Dados privados protegidos contra modificações indevidas
- `life`, `name`, `defense` só podem ser alterados via setters
- Garante consistência dos dados

**Exemplo de uso:**
```python
jogador = Warrior("Arthas")
# ❌ jogador.__life = 1000  # Erro! Não é permitido
# ✅ jogador.life = 50      # OK! Via setter
print(jogador.life)          # Acessa via getter (property)
```

---

### 2️⃣ **HERANÇA**

#### Definição
Herança permite que uma classe filha herde atributos e métodos de uma classe pai, promovendo reutilização de código.

#### Implementação no Código

**Classe Pai: `Personagem.py`**
```python
class Characters():  # Classe PAI
    def __init__(self, name, life, attack, defense):
        self.__name = name
        # ... outros atributos
    
    def atacar(self, alvo):
        # Lógica comum a todos os personagens
        dano = self.attack + getattr(self, 'weapon_bonus', 0) - alvo.defense
        return dano
```

**Classes Filhas:**

**`warrior.py`**
```python
class Warrior(Characters):  # Herda de Characters
    def __init__(self, name):
        super().__init__(name, life=50, attack=13, defense=13)
        # Atributos específicos do Guerreiro
        self.weapon_name = "Hemodrenario"
        self.weapon_bonus = 5
        self.special_name = "Golpe Duplo"
```

**`arqueiro.py`**
```python
class Archer(Characters):  # Herda de Characters
    def __init__(self, name):
        super().__init__(name, life=20, attack=10, defense=10)
        # Atributos específicos do Arqueiro
        self.weapon_name = "Furacão De Runaan"
        self.weapon_bonus = 8
        self.special_name = "Chuva de Flechas"
```

**Todos os personagens herdam:**
- ✅ `atacar(alvo)` - ataque normal
- ✅ `receber_dano(dano)` - receber dano
- ✅ `curar(quantidade)` - recuperar HP
- ✅ `usar_pocao()` - usar poção
- ✅ Propriedades: `name`, `life`, `attack`, `defense`, `max_life`

---

### 3️⃣ **SUPERCLASSES e `super()`**

#### Definição
`super()` permite que a classe filha acesse métodos e construtores da classe pai.

#### Implementação no Código

**Inicialização com `super()`:**

```python
# warrior.py
class Warrior(Characters):
    def __init__(self, name):
        # Chama o __init__ da classe PAI
        super().__init__(name, life=50, attack=13, defense=13)
        #                 ↑
        #          Inicializa atributos privados
        
        # Depois adiciona atributos específicos
        self.weapon_name = "Hemodrenario"
        self.weapon_bonus = 5
```

**Acesso a Métodos da Classe Pai:**

```python
# paladino.py
class Paladin(Characters):
    def special_attack(self, alvo):
        # Calcula dano do ataque especial
        dano = self.attack + self.weapon_bonus + 5 - alvo.defense
        
        # Chama método receber_dano() da classe pai
        alvo.receber_dano(dano)
        
        # Chama método curar() da classe pai
        cura = self.defense // 2
        self.curar(cura)  # Habilidade única do Paladino!
        
        return dano
```

---

### 4️⃣ **POLIMORFISMO**

#### Definição
Polimorfismo permite que diferentes classes respondam ao mesmo método de formas diferentes. A mesma interface (`special_attack()`) tem comportamentos distintos em cada classe filha.

#### Implementação no Código

**Método `special_attack()` em cada classe:**

```python
# warrior.py - Golpe Duplo (x2 dano)
def special_attack(self, alvo):
    if getattr(self, 'ability_uses', 0) <= 0:
        return 0
    self.ability_uses -= 1
    ataque_total = self.attack + self.weapon_bonus
    dano = ataque_total * 2 - alvo.defense  # ← MULTIPLICADOR
    return dano

# mago.py - Bola de Fogo (+10 dano)
def special_attack(self, alvo):
    if getattr(self, 'ability_uses', 0) <= 0:
        return 0
    self.ability_uses -= 1
    ataque_total = self.attack + self.weapon_bonus
    dano = ataque_total + 10 - alvo.defense  # ← BÔNUS FIXO
    return dano

# arqueiro.py - Chuva de Flechas (x3 dano)
def special_attack(self, alvo):
    if getattr(self, 'ability_uses', 0) <= 0:
        return 0
    self.ability_uses -= 1
    ataque_total = self.attack + self.weapon_bonus
    dano = ataque_total * 3 - alvo.defense  # ← MULTIPLICADOR MAIOR
    return dano

# paladino.py - Golpe Sagrado (+5 dano + CURA)
def special_attack(self, alvo):
    if getattr(self, 'ability_uses', 0) <= 0:
        return 0
    self.ability_uses -= 1
    ataque_total = self.attack + self.weapon_bonus
    dano = ataque_total + 5 - alvo.defense
    alvo.receber_dano(dano)
    cura = self.defense // 2
    self.curar(cura)  # ← EFEITO ÚNICO!
    return dano
```

**Polimorfismo em ação (em `battle.py`):**

```python
# Mesmo método, comportamentos diferentes!
if acao == "2":
    dano = atacante.special_attack(defensor)
    # Pode ser Guerreiro (x2), Mago (+10), Arqueiro (x3), Paladino (cura)
    # O Python automaticamente chama a versão correta da classe!
```

**Exemplo prático:**
```python
guerreiro = Warrior("Arthas")
mago = Wizard("Gandalf")

# Mesmo método, resultados diferentes
dano_guerreiro = guerreiro.special_attack(mago)  # Golpe Duplo (x2)
dano_mago = mago.special_attack(guerreiro)       # Bola de Fogo (+10)
```

---

## 🎮 Como Jogar

### Executar o Jogo
```bash
python battle.py
```

### Fluxo do Jogo

1. **Seleção de Personagem 1**
   - Escolha uma classe (1-4)
   - Defina um nome

2. **Seleção de Personagem 2**
   - Escolha outra classe (pode ser igual)
   - Defina um nome

3. **Combate**
   - Alternam turnos
   - Escolha ação: Ataque Normal (1), Especial (2) ou Poção (3)
   - Vença derrotando o adversário (reduzir HP para 0)

---

## 📊 Exemplo de Combate

```
=== ESCOLHA SUA CLASSE ===
1 - Guerreiro  |  HP:50 ATK:13 DEF:13  |  Arma:Hemodrenario  Armadura:Desespero eterno  Habilidade:Golpe Duplo
2 - Paladino   |  HP:25 ATK:14 DEF:15  |  Arma:Ruptor Divino  Armadura:Hooker Lamurico  Habilidade:Golpe Sagrado
3 - Mago       |  HP:15 ATK:22 DEF:10  |  Arma:Capuz Da Morte De Rabadon  Armadura:Zhonyas  Habilidade:Bola de Fogo
4 - Arqueiro   |  HP:20 ATK:10 DEF:10  |  Arma:Furacão De Runaan  Armadura:Arco-Escudo  Habilidade:Chuva de Flechas

Digite sua escolha (1-4): 1
Digite o nome do seu personagem: Arthas

=== Arthas vs Gandalf ===

--- Rodada 1 ---

Turno de Arthas: Vida 50/50  |  Inimigo Gandalf: 15/15
Escolha a ação:
1 - Ataque normal
2 - Ataque especial
3 - Usar poção
Opção: 1
Arthas atacou Gandalf causando 12 de dano!
```

---

## 📁 Estrutura de Arquivos

```
Projeto Logica-RPG/
│
├── Personagem.py          # Classe pai com métodos comuns
├── warrior.py             # Classe Guerreiro
├── paladino.py            # Classe Paladino
├── mago.py                # Classe Mago
├── arqueiro.py            # Classe Arqueiro
├── battle.py              # Sistema de combate e menu
├── teste_combate.py       # Script de testes
└── README.md              # Esta documentação
```

---

## 🔧 Autor

Desenvolvido como projeto educacional em POO (Programação Orientada a Objetos).

**Conceitos-Chave Cobertos:**
- ✅ Encapsulamento (atributos privados/públicos)
- ✅ Herança (classe pai `Characters` + 4 filhas)
- ✅ Superclasses (`super()`)
- ✅ Polimorfismo (método `special_attack()` sobrescrito)
- ✅ Properties (getters/setters)
- ✅ Composição (personagens com equipamento)

---

## 📝 Versão
v1.0 - Novembro 2025
