from gamblingWeapons import d6

class Miniboss:
    def __init__(self, name: str, hp: int):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.weapon = d6

