import random
from utilities import choose_action, describe_intent
from abilities import shieldShatter, tick_cooldowns

def start_turn(character):
    character.defending = False
    if character.cannot_defend > 0:
        character.cannot_defend -= 1

def attack(attacker, defender):
    base_damage = attacker.attack

    if random.random() < 0.1:
        base_damage *= 2
        print(f"{attacker.name} lands a CRITICAL hit!")

    damage_dealt = defender.take_damage(base_damage)

    print(f"{attacker.name} deals {damage_dealt} damage to {defender.name}")
    print(f"{defender.name} HP: {defender.hp}")

def ability_menu(player, enemy):
    while True:
        print("\n===== ABILITIES =====")
        print("1. Break Guard Strike")
        print("0. Back")

        choice = input("> ")

        if choice == "1":
            if player.cooldowns.get("break_guard", 0) > 0:
                print("Ability is on cooldown!")
                return

            shieldShatter(player, enemy)

            player.cooldowns["break_guard"] = 3
            return

        elif choice == "0":
            return

        else:
            print("Invalid choice")

def combat(player, enemy):
    print("\n ===== BATTLE START =====")
    print(f"A {enemy.name} appears!")

    while player.is_alive() and enemy.is_alive():

        # PLAYER TURN
        start_turn(player)
        print("\n===== PLAYER TURN =====")
        describe_intent(enemy)
        tick_cooldowns(player)
        choice = choose_action()

        if choice == "1":
            attack(player, enemy)

        elif choice == "2":
            player.defend()
            print(f"{player.name} braces for impact!")

        elif choice == "3":
            ability_menu(player, enemy)

        else:
            print("Invalid choice!")
            continue

        # ENEMY TURN
        if enemy.is_alive():
            start_turn(enemy)
            print("\n===== ENEMY TURN =====")
            move = enemy.get_next_move()

        if move == "attack":
            attack(enemy, player)

        elif move == "defend":
            enemy.defend()
            print(f"{enemy.name} defends!")

        elif move == "heavyAttack":
            attack(enemy, player)  # modify for bonus damage later

        enemy.advance_move()
    if player.is_alive():
        print(f"You defeated the {enemy.name}!\n")
        print("===== VICTORY =====")
        return True
    
    else:
        print("You were defeated...\n")
        return False