from character import Hero, Enemy
from weapon import short_bow, iron_sword
import random

class Weapon:
    def __init__(self, name: str, damage: int) -> None:
        self.name = name
        self.damage = damage
d4 = Weapon(name = "d4", damage = random.randint(1, 4))
d6 = Weapon(name = "d6", damage = random.randint(1, 6))

hero = Hero(name = "Hero", health = 100)
enemy = Enemy(name = "Enemy", health = 100)

hero.equip(d6)
enemy.equip(d4)

while True:
    hero.attack(enemy)
    enemy.attack(hero)
    d6 = Weapon(name = "d6", damage = random.randint(1, 6))
    hero.equip(d6)
    d4 = Weapon(name = "d4", damage = random.randint(1, 4))
    enemy.equip(d4)

    print(f"Health of {hero.name}: {hero.health}")
    print(f"Health of {enemy.name}: {enemy.health}")

    input()

    if hero.health == 0:
        print("Game Over")
        break

    elif enemy.health == 0:
        print("Victory")
        break