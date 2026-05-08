# Move all text from main.py into dialogue.json and print it out in the game

import json

# Open the JSON file
with open("data/dialogue.json", "r") as file:
    data = json.load(file)

# Print text from the JSON
print(data["gameStart"]["intro"])
