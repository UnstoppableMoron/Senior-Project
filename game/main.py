from characters import Player, Enemy, goblin, goblin1
from combat import combat

def gameLoop():
    playerName = input("Before we can begin, what is your name? ")
    print("Perfect. Allow me to set the scene for you...")
    print("You and two other adventurers have been tasked with escorting a carriage")
    print("full of precious cargo, the likes of which cannot afford to be damaged.")
    print("You're about three days into your journey, with a couple more to go.")
    print("As you begin to settle down for the night, you hear a slight rustling in")
    print("a nearly bush. You stand between the camp and the bush, watching it warily, ")
    print("as an angry looking goblin jumps out at you, brandishing a rusty knife.")

    player = Player(playerName)
    while True:
        combat(player, goblin)
        if not player.is_alive():
            print("Game Over")
            break
        
        if not goblin.is_alive():
            break

        player.hp = 100
    
    print("\n\nThe goblin goes down without much fight, but it makes you wonder why it")
    print("might have attacked you alone, and whether there are more lurking about.")
    print("As you hear a frantic rustling from behind you, you turn around just in time to")
    print("witness an abnormally large goblin making off with a crate of your precious cargo.")
    print("You try to chase it down, but are intercepted by another goblin,")
    print("this one also significantly larger than normal.")

    player = Player(playerName)
    while True:
        combat(player, goblin1)
        player.abilities_unlocked = True
        if not player.is_alive():
            print("Game Over")
            break
        
        if not goblin1.is_alive():
            break

        player.hp = 100

        for ability in list(player.cooldowns.keys()):
            player.cooldowns[ability] = max(0, player.cooldowns[ability] - 999)

if __name__ == "__main__":
    gameLoop()

# Shield Shatter doesn't fully work, and displaying of enemy intents is repeated multiple times. FIX IT FOR FUCKS SAKE