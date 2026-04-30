from weapons import longsword, dagger, warhammer, battleaxe

class Player:
    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health
        self.health_max = health
        self.weapon = longsword 
    
    def equip(self, weapon) -> None:
        self.weapon = weapon
        print(f"{self.name} equipped {self.weapon.name}!")