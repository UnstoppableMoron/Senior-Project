import random

class Weapon:
    def __init__(self, name: str, damage: int, value: int) -> None:
        self.name = name
        self.damage = damage

d6 = Weapon(name = "dice", damage = random.randint(1, 6))