class Weapon:
    def __init__(self, name: str, damage: int) -> None:
        self.name = name
        self.damage = damage

longsword = Weapon(name = "Longsword", damage = 5)
dagger = Weapon(name = "Dagger", damage = 3)
warhammer = Weapon(name = "Warhammer", damage = 10)
battleaxe = Weapon(name = "Battleaxe", damage = 8)
spear = Weapon(name = "Spear", damage = 7)