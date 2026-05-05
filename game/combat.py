import random
from utilities import choose_action

def start_turn(character):
    character.defending = False

def attack(attacker, defender):
    base_damage = attacker.attack

    if random.random() < 0.1:
        base_damage *= 2
        print(f"{attacker.name} lands a CRITICAL hit!")

    damage_dealt = defender.take_damage(base_damage)

    print(f"{attacker.name} deals {damage_dealt} damage to {defender.name}")
    print(f"{defender.name} HP: {defender.hp}")

def run_combat(player, enemy):
    print(f"\nA {enemy.name} appears!")

    while player.is_alive() and enemy.is_alive():

        # PLAYER TURN
        start_turn(player)
        choice = choose_action()

        if choice == "1":
            attack(player, enemy)

        elif choice == "2":
            player.defend()
            print(f"{player.name} braces for impact!")

        else:
            print("Invalid choice!")
            continue

        # ENEMY TURN
        if enemy.is_alive():
            start_turn(enemy)

            # simple AI
            if random.random() < 0.2:
                enemy.defend()
                print(f"{enemy.name} defends!")
            else:
                attack(enemy, player)

    if player.is_alive():
        print(f"You defeated the {enemy.name}!\n")
        return True
    else:
        print("You were defeated...\n")
        return False