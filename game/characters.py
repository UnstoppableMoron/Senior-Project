# Character class and functions
class Character:
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.defending = False
        self.cannot_defend = 0

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        if self.defending:
            damage *= 0.5

        damage_taken = max(0, int(damage) - self.defense)
        self.hp -= damage_taken
        return damage_taken

    def defend(self):
        if self.cannot_defend > 0:
            print(f"{self.name} tries to defend but is off balance!")
            self.defending = False
        else:
            self.defending = True
            print(f"{self.name} is defending!")


# Player and enemy classes
class Player(Character):
    def __init__(self, name):
        super().__init__(name=name, hp=100, attack=15, defense=10)
        self.energy = 3
        self.max_energy = 3
        self.cooldowns = {}
        self.abilities_unlocked = False


class Enemy(Character):
    def __init__(self, name, hp, attack, defense, moves):
        super().__init__(name, hp, attack, defense)
        self.moves = moves
        self.current_move_index = 0

    def get_next_move(self):
        return self.moves[self.current_move_index]

    def advance_move(self):
        self.current_move_index = (self.current_move_index + 1) % len(self.moves)


# Specific enemy classes
goblin = Enemy(name = "Goblin", hp = 40, attack = 15, defense = 5, moves = ["attack", "attack", "defend"])
goblin1 = Enemy(name = "Goblin 1", hp = 55, attack = 11, defense = 13, moves = ["defend", "defend", "defend"])
goblin2 = Enemy(name = "Goblin 2", hp = 30, attack = 18, defense = 8, moves = ["defend", "attack", "attack"])
goblin3 = Enemy(name = "Goblin 3", hp = 40, attack = 13, defense = 7, moves = ["attack", "attack", "defend"])
orc = Enemy(name = "Orc", hp = 80, attack = 24, defense = 8, moves = ["attack", "attack", "heavyAttack", "stun"])
royalGuard = Enemy(name = "Royal Guard", hp = 75, attack = 21, defense = 18, moves = ["attack", "attack", "defend"])
giantSpider = Enemy(name = "Giant Spider", hp = 60, attack = 17, defense = 13, moves = ["attack", "attack", "defend"])