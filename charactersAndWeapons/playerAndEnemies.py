from weapons import longsword, dagger, warhammer, battleaxe, spear
from game import playerName

class Player:
    def __init__(self, name: str, health: int):
        self.name = playerName
        self.health = 45
        self.health_max = 45
        self.weapon = longsword 
    
    def equip(self, weapon) -> None:
        self.weapon = weapon
        print(f"{self.name} equipped {self.weapon.name}!")

    def attack(self, enemy):
        enemy.health = enemy.health - Player.weapon.damage


class Goblin:
    def __init__(self, name: str, health: int):
        self.name = Goblin
        self.health = 10
        self.health_max = 10
        self.weapon = dagger