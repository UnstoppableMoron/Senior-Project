# Helper functions

# Combat functions
def choose_action():
    print("What do you do?")
    print("1. Attack")
    print("2. Defend")
    print("3. Abilities")
    return input("> ")

def describe_intent(enemy):
    move = enemy.get_next_move()
    if move == "attack":
        print(f"{enemy.name} readies an attack!")
    elif move == "defend":
        print(f"{enemy.name} braces defensively!")
    elif move == "heavyAttack":
        print(f"{enemy.name} winds up for a powerful strike!")
    elif move == "stun":
        print(f"{enemy.name} is stunned!")

# World functions

# Intro goblin choice
def goblin_action():
    print("What do you do?")
    print("1. Continue on")
    print("2. Follow the goblin")
    return input("> ")

def town_choice():
    print("What do you check out first?")
    print("1. Go to the tavern")
    print("2. Go to the store")
    print("3. Look at the wanted poster")
    return input("> ")