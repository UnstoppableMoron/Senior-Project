# Move all text from main.py into dialogue.json and print it out in the game
import time, builtins, json
from game.characters import Player, Enemy, goblin, goblin1
from game.combat import combat
from game.utilities import goblin_choice, town_choice

goblin_option = goblin_choice()
if goblin_option == "1":
    print(data["goblinChoice"]["choice1"])
elif goblin_option == "2":
    print(data["goblinChoice"]["choice2"])