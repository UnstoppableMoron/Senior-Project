import time, builtins
from characters import Player, Enemy, goblin, goblin1
from combat import combat
from utilities import goblin_action, goblin_choice
from options import goblin_choice_1, goblin_choice_2

# Typewriter effect
# def slow_print(*args, delay=0.02, sep=' ', end='\n', flush=True):
#     text = sep.join(str(arg) for arg in args) + end
#     for char in text:
#         builtins.print(char, end='', flush=True)
#         time.sleep(delay)

# print = slow_print

def gameLoop():
    playerName = input("Before we can begin, what is your name? ")
    print("Perfect. Allow me to set the scene for you...")
    print("You and two other adventurers have been tasked with escorting a carriage")
    print("containing two crates of a precious cargo, the likes of which cannot")
    print("afford to be damaged. You're about three days into your journey, with a couple")
    print("more to go. As you begin to settle down for the night, you hear a slight rustling")
    print("in a nearly bush. You stand between the camp and the bush, watching it warily, ")
    print("as an angry looking goblin jumps out at you, brandishing a rusty knife.")

    player = Player(playerName)
    combat(player, goblin)
    if not player.is_alive():
        print("Game Over")

    player.hp = 100
    
    print("\n\nThe goblin goes down without much fight, but it makes you wonder why it")
    print("might have attacked you alone, and whether there are more lurking about.")
    print("As you hear a frantic rustling from behind you, you turn around just in time to")
    print("witness an abnormally large goblin making off with a crate of your precious cargo.")
    print("You try to chase it down, but are intercepted by another goblin,")
    print("this one also significantly larger than normal.")

    player = Player(playerName)
    combat(player, goblin1)
    if not player.is_alive():
        print("Game Over")

    player.hp = 100

    for ability in list(player.cooldowns.keys()):
            player.cooldowns[ability] = max(0, player.cooldowns[ability] - 999)

    print("\n\nAfter taking out the goblin, you look around frantically, but to no avail.\nThe goblin that stole one of your crates is nowhere to be seen. If you continue to your\ndestination without it, you risk not being paid for your efforts, but following the\ngoblin may result in your untimely death.")
    goblin_action() # Move this to options.py and make the import work somefuckinghow
    if goblin_choice == "1":
        goblin_choice_1()
    elif goblin_choice == "2":
        goblin_choice_2()
            
if __name__ == "__main__":
    gameLoop()

# Shield Shatter doesn't fully work, and displaying of enemy intents is repeated multiple times. FIX IT FOR FUCKS SAKE