import random

class Weapon:
    def __init__(self, name: str, damage: int) -> None:
        self.name = name
        self.damage = damage

d4 = Weapon(name = "d6", damage = random.randint(1, 4))
d6 = Weapon(name = "d6", damage = random.randint(1, 6))
d12 = Weapon(name = "d12", damage = random.randint(1, 12))
d20 = Weapon(name = "d20", damage = random.randint(1, 20))
coin = Weapon(name = "coin", damage = random.randint(0, 1))
roulette_gun = Weapon(name = "roulette gun", damage = random.randint(1, 6))