from character import Hero, Enemy
from weapon import short_bow, iron_sword
from gamblingWeapons import d6

hero = Hero(name = "Hero", health = 100)
hero.equip(d6)
enemy = Enemy(name = "Enemy", health = 100, weapon = short_bow)

while True:
    hero.attack(enemy)
    enemy.attack(hero)

    print(f"Health of {hero.name}: {hero.health}")
    print(f"Health of {enemy.name}: {enemy.health}")

    input()