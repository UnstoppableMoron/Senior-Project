from charactersAndWeapons.weapons import longsword, dagger, warhammer, battleaxe, spear
from charactersAndWeapons.playerAndEnemies import Player, Goblin, attack

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
        print("\n\n")
        print("The goblins plan to attack you.")
        action = input("What do you do?")

        if action.lower == "attack":
            attack(Player, Goblin)
        
        break


tutorialBattle()