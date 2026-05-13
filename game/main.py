import time, builtins, json
from characters import Player, Enemy, goblin, goblin1
from combat import combat
from utilities import goblin_choice, goblin_camp_choice, town_choice

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

    # Intro
    playerName = input("Before we can begin, what is your name? ")
    print(data["gameStart"]["intro"])

    # First tutorial combat 
    # Remember to add tutorial text prompts here
    player = Player(playerName)
    combat(player, goblin)
    if not player.is_alive():
        print("Game Over")

    player.hp = 100
    
    # Second tutorial combat
    # Remember to add tutorial text prompts here
    print(data["combatIntro2"]["intro"])

    player = Player(playerName)
    combat(player, goblin1)
    if not player.is_alive():
        print("Game Over")

    player.hp = 100

    for ability in list(player.cooldowns.keys()):
            player.cooldowns[ability] = max(0, player.cooldowns[ability] - 999)
            
    # Goblin choice
    print(data["goblinChoice"]["prompt"])

    goblin_option = goblin_choice()
    if goblin_option == "1":
        print(data["goblinChoice"]["choice1"])

        # goblin camp nonsense
        print(data["goblinCampChoice"]["prompt"])
        goblin_camp_option = goblin_camp_choice()
        if goblin_camp_option == "1":
            print(data["goblinCampChoice"]["choice1"])
        elif goblin_camp_option == "2":
            print(data["goblinCampChoice"]["choice2"])
            
    elif goblin_option == "2":
        print(data["goblinChoice"]["choice2"])

    # Town choice
    print(data["townChoice"]["prompt"])
    town_option = town_choice()
    if town_option == "1":
        print(data["townChoice"]["choice1"])
    elif town_option == "2":
        print(data["townChoice"]["choice2"])
    elif town_option == "3":
        print(data["townChoice"]["choice3"])

            
if __name__ == "__main__":
    gameLoop()

# Shield Shatter doesn't fully work, and displaying of enemy intents is repeated multiple times. FIX IT FOR FUCKS SAKE