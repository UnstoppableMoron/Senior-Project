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
with open("data/dialogue.json", "r") as file:
    data = json.load(file)

def gameLoop():
    playerName = input("Before we can begin, what is your name? ")
    print(data["gameStart"]["intro"])

    player = Player(playerName)
    combat(player, goblin)
    if not player.is_alive():
        print("Game Over")

    player.hp = 100
    
    print(data["combatIntro2"]["intro"])

    player = Player(playerName)
    combat(player, goblin1)
    if not player.is_alive():
        print("Game Over")

    player.hp = 100

    for ability in list(player.cooldowns.keys()):
            player.cooldowns[ability] = max(0, player.cooldowns[ability] - 999)
            
    print(data["goblinChoicePrompt"]["choice"])

    goblin_choice = goblin_action() # Move this to options.py and make the import work somefuckinghow
    if goblin_choice == "1":
        print(data["goblinChoice1"]["choice1"])
    elif goblin_choice == "2":
        print(data["goblinChoice2"]["choice2"])
            
if __name__ == "__main__":
    gameLoop()

# Shield Shatter doesn't fully work, and displaying of enemy intents is repeated multiple times. FIX IT FOR FUCKS SAKE