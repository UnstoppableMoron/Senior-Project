import random
from characters import Enemy

def random_enemy():
    enemies = [
        Enemy("Goblin", 50, 10, 2),
        Enemy("Skeleton", 40, 12, 1),
        Enemy("Orc", 80, 12, 4),
    ]
    return random.choice(enemies)