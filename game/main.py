import time, builtins, json
from characters import Player, Enemy, goblin, goblin1
from combat import combat
from utilities import goblin_action
# from options import goblin_choice_1, goblin_choice_2

# Typewriter effect
# def slow_print(*args, delay=0.02, sep=' ', end='\n', flush=True):
#     text = sep.join(str(arg) for arg in args) + end
#     for char in text:
#         builtins.print(char, end='', flush=True)
#         time.sleep(delay)

# print = slow_print

def gameLoop():
    playerName = input("Before we can begin, what is your name? ")
    

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
    goblin_choice = goblin_action() # Move this to options.py and make the import work somefuckinghow
    if goblin_choice == "1":
        print("After instructing your companions to watch the carriage, you run off in\nthe direction of the goblin. After several minutes of running, you find a small camp of\n goblins, seemingly lead by an orc. You don't stand much chance given the current circumstances,\n but your companions may be able to help you. On the other hand, if you can manage\n to get the drop on the orc somehow, you may be able to get this done yourself.")
    elif goblin_choice == "2":
        print("You continue on to your destination, the town with a cool name that I'll think of later.\nYou make it there after a couple days, and follow the address you were given to the workshop\n of the prestigious artificer Toralf. He welcomes your arrival, and is willing to forget the issue of the\nmissing crate. He pays you for your efforts, and you leave him to his creations. As you walk back out into town,\n you ")
            
if __name__ == "__main__":
    gameLoop()

# Shield Shatter doesn't fully work, and displaying of enemy intents is repeated multiple times. FIX IT FOR FUCKS SAKE