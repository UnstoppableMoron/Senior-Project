from character import Hero, Enemy
from weapon import short_bow, iron_sword
import random

class Weapon:
    def __init__(self, name: str, damage: int) -> None:
        self.name = name
        self.damage = damage

hero = Hero(name = "Hero", health = 100)
enemy = Enemy(name = "Enemy", health = 100, weapon = "d4")

hero.equip(iron_sword)
enemy.equip(short_bow)

while True:
    hero.attack(enemy)
    enemy.attack(hero)
    
    print(f"Health of {hero.name}: {hero.health}")
    print(f"Health of {enemy.name}: {enemy.health}")

    input()

    if hero.health == 0:
        print("Game Over")
        break

    elif enemy.health == 0:
        print("Victory")
        break