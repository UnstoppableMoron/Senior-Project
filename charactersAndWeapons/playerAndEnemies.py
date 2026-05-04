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

class enemy:
    def __init__(self, name: str, health: int, weapon: str):
        self.name = name
        self.health = health
        self.health_max = health
        self.weapon = dagger

    def is_alive(self):
        return self.health > 0

    def attack(self, Player):
        damage = self.weapon.damage
        Player.health -= damage
        print(f"{self.name} hits {Player.name} for {damage} damage!")