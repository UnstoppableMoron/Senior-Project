from gamblingWeapons import d6, d12, d20, coin, roulette_gun

class Miniboss:
    def __init__(self, name: str, hp: int):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.weapon = d6

class Boss:
    def __init__(self, name: str, hp: int):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.weapon = d12
