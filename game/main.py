from characters import Player, Enemy, goblin
from combat import run_combat

def gameLoop():
    playerName = input("Before we can begin, what is your name? ")
    print("Perfect. Allow me to set the scene for you...")
    print("You and two other adventurers have been tasked with escorting a carriage")
    print("full of precious cargo, the likes of which cannot afford to be damaged.")
    print("You're about three days into your journey, with a couple more to go.")
    print("As you begin to settle down for the night, you hear a slight rustling in")
    print("a nearly bush. You stand between the camp and the bush, watching it warily, ")
    print("as two angry looking goblins jump out at you, brandishing rusty knives.")

    while True:
        player = Player(playerName)
        run_combat(player, goblin)
        if not player.is_alive():
                print("Game Over")
                break
        
        if not goblin.is_alive():
             break

        player.hp = 100


if __name__ == "__main__":
    gameLoop()