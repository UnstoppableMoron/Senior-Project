from weapons import longsword, dagger, warhammer, battleaxe, spear
from game import playerName

class Player:
    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health
        self.health_max = health
        self.weapon = longsword
    
    def equip(self, weapon):
        self.weapon = weapon
        print(f"{self.name} equipped {self.weapon.name}!")

    def is_alive(self):
        return self.health > 0

    def attack(self, enemy):
        damage = self.weapon.damage
        enemy.health -= damage
        print(f"{self.name} deals {damage} damage to {enemy.name}!")

class Goblin:
    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health
        self.health_max = health
        self.weapon = dagger

    def is_alive(self):
        return self.health > 0

    def attack(self, enemy):
        damage = self.weapon.damage
        enemy.health -= damage
        print(f"{self.name} hits {enemy.name} for {damage} damage!")