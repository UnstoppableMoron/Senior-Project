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

# Goblin intro stuff
def goblin_choice():
    print("What do you do?")
    print("1. Follow the goblin")
    print("2. Continue on")
    return input("> ")

def goblin_camp_choice():
    print("What do you do?")
    print("1. Play it safe and back off")
    print("2. Try to sneak up on the orc")
    return input("> ")


# Solace town square stuff
def town_choice():
    print("What do you check out first?")
    print("1. Go to the tavern")
    print("2. Go to the store")
    print("3. Look at the billboard")
    return input("> ")

def shop_choice():   # Change this function name to fit whatever I name the shop
    print("Will you buy anything?")
    print("1. Buy the sheath (45 gold)")
    print("2. Buy the stone (60 gold)")
    print("3. Buy the ring (71 gold)")
    print("4. Don't buy anything")
    return input("> ")