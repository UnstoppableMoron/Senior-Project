import json
from characters import Player, Enemy, goblin, goblin1
from combat import combat
from utilities import goblin_choice, town_choice

with open("data/dialogue.json", "r") as file:
    data = json.load(file)

print(data["goblinChoice"]["prompt"])

goblin_option = goblin_choice()
if goblin_option == "1":
    print(data["goblinChoice"]["choice1"])
    print(data["goblinCampChoice"]["prompt"])

elif goblin_option == "2":
    print(data["goblinChoice"]["choice2"])