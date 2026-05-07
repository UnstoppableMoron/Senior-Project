# Move all text from main.py into dialogue.json and print it out in the game

import json

# Open the JSON file
with open("data/dialogue.json", "r") as file:
    data = json.load(file)

# Print text from the JSON
print(data["gameStart"]["intro"])


# print("Perfect. Allow me to set the scene for you...")
#     print("You and two other adventurers have been tasked with escorting a carriage")
#     print("containing two crates of a precious cargo, the likes of which cannot")
#     print("afford to be damaged. You're about three days into your journey, with a couple")
#     print("more to go. As you begin to settle down for the night, you hear a slight rustling")
#     print("in a nearly bush. You stand between the camp and the bush, watching it warily, ")
#     print("as an angry looking goblin jumps out at you, brandishing a rusty knife.")