
class Character:
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.defending = False

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        if self.defending:
            damage *= 0.5

        damage_taken = max(0, int(damage) - self.defense)
        self.hp -= damage_taken
        return damage_taken

    def defend(self):
        self.defending = True


# Player and enemy classes
class Player(Character):
    def __init__(self, name):
        super().__init__(name=name, hp=100, attack=15, defense=10)

class Enemy(Character):
    def __init__(self, name, hp, attack, defense):
        super().__init__(name, hp, attack, defense)


# Specific enemy classes
goblin = Enemy(name = "Goblin", hp = 45, attack = 15, defense = 5)
orc = Enemy(name = "Orc", hp = 80, attack = 24, defense = 12)