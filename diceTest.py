import random

def roll_dice():
    """Simulates rolling a six-sided die."""
    # random.randint(1, 6) returns a random integer N such that 1 <= N <= 6
    result = random.randint(1, 6)
    print(f"You rolled a {result}")

# Main program loop
while True:
    user_input = input("Press Enter to roll the die, or type 'exit' to quit: ")
    
    if user_input.lower() == 'exit':
        print("Exiting dice roller.")
        break
    else:
        roll_dice()