from Personagem import Characters
from warrior import Warrior
from mago import Wizard
from paladino import Paladin
from arqueiro import Archer


def selecionar_personagem():
    classes = [
        ("1", "Guerreiro", Warrior),
        ("2", "Paladino", Paladin),
        ("3", "Mago", Wizard),
        ("4", "Arqueiro", Archer),
    ]

    print("\n=== ESCOLHA SUA CLASSE ===")
    for esc, label, cls in classes:
        temp = cls("__stats__")
        weapon = getattr(temp, 'weapon_name', '—')
        armor = getattr(temp, 'armor_name', '—')
        ability = getattr(temp,'special_name', '—')
        print(f"{esc} - {label}  |  HP:{temp.life} ATK:{temp.attack} DEF:{temp.defense}  |  Arma:{weapon}  Armadura:{armor}  Habilidade:{ability}")

    escolha = input("Digite sua escolha (1-4): ")
    nome = input("Digite o nome do seu personagem: ")

    opcoes = {"1": Warrior, "2": Paladin, "3": Wizard, "4": Archer}
    cls = opcoes.get(escolha)
    if cls is None:
        print("Opção inválida, tente novamente.")
        return selecionar_personagem()
    return cls(nome)


def luta(p1, p2):
    print(f"\n=== {p1.name} vs {p2.name} ===")
    rodada = 1

    while p1.life > 0 and p2.life > 0:
        print(f"\n--- Rodada {rodada} ---")
        for atacante, defensor in ((p1, p2), (p2, p1)):
            if atacante.life <= 0 or defensor.life <= 0:
                break

            print(f"\nTurno de {atacante.name}: Vida {atacante.life}/{atacante.max_life}  |  Inimigo {defensor.name}: {defensor.life}/{defensor.max_life}")
            print("Escolha a ação:")
            print("1 - Ataque normal")
            print("2 - Ataque especial")
            print("3 - Usar poção")
            acao = input("Opção: ").strip()

            if acao == "1":
                dano = atacante.atacar(defensor)
                print(f"{atacante.name} atacou {defensor.name} causando {dano} de dano!")
            elif acao == "2":
                dano = atacante.special_attack(defensor)
            elif acao == "3":
                sucesso = atacante.usar_pocao()
                if not sucesso:
                    print(f"{atacante.name} não possui mais a poção.")
            else:
                print("Ação inválida — turno perdido.")

            if defensor.life <= 0:
                print(f"\n🎉 {atacante.name} VENCEU! {defensor.name} foi derrotado.")
                return

        rodada += 1

    if p1.life > 0:
        print(f"\n🎉 {p1.name} VENCEU!")
    else:
        print(f"\n🎉 {p2.name} VENCEU!")


if __name__ == "__main__":
    print("BEM-VINDO AO JOGO DE RPG!")
    jogador1 = selecionar_personagem()
    jogador2 = selecionar_personagem()
    print(f"\n{jogador1.name} foi criado com sucesso!")
    print(f"\n{jogador2.name} foi criado com sucesso!")
    input("\nPressione Enter para começar a luta...")
    luta(jogador1, jogador2)
    
