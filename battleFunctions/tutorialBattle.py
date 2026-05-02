from charactersAndWeapons.weapons import longsword, dagger, warhammer, battleaxe, spear
from charactersAndWeapons.playerAndEnemies import Player, Goblin

def tutorialBattle():
    while True:
        enemy = Goblin
        print("Combat in this world is simple. You will be able to see the actions an enemy will take, ")
        print("and will be given the option to attack, defend, or use an item, if applicable.")
        print("Enemies may simply attack or defend, but they may also use an item or attempt to ")
        print("apply a buff to themselves or a debuff to you. We'll use this battle as a method of testing that. ")

        print("Now, you can type 'attack', 'defend', or 'item' to determine what you do. ")
        print("You don't currently have any items, but you will soon enough. ")
        print("For now, just try attacking or defending. ")
        print("\n")

        if action.lower() == "attack":
            attack(Player, Goblin)
        player = Player("Hero", 45)
        enemy = Goblin("Goblin", 10)

        print("The goblin plans to attack you.")

        while player.is_alive() and enemy.is_alive():
            action = input("What do you do? (attack/defend): ")

        if action.lower() == "attack":
            player.attack(enemy)

            if enemy.is_alive():
                enemy.attack(player)

        elif action.lower() == "defend":
            print("You brace for the attack! (not implemented yet)")

        else:
            print("Invalid action.")

        print(f"{player.name}: {player.health} HP")
        print(f"{enemy.name}: {enemy.health} HP")

        if player.is_alive():
            print("You win!")
        else:
            print("You lost...")


tutorialBattle()