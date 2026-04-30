class Weapon:
    def __init__(self, name: str, damage: int, value: int) -> None:
        self.name = name
        self.damage = damage
        self.value = value

longsword = Weapon(name = "Longsword", damage = 5, range = 5)
dagger = Weapon(name = "Dagger" damage = 4, range = 2)
warhammer = Weapon(name = "Warhammer" damage = 10, range = 3)
battleaxe = Weapon(name = "Battleaxe" damage = 8, range = 5)
spear = Weapon(name = "Spear", damage = 7, range = 7)