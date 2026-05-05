# Shield Shatter
def shieldShatter(attacker, defender):
    print(f"{attacker.name} uses Shield Shatter!")

    damage = attacker.attack * 2

    if defender.defending:
        defender.defending = False
        print(f"{defender.name}'s guard is broken!")

    defender.cannot_defend = 1
    print(f"{defender.name} cannot defend next turn!")

    dealt = defender.take_damage(damage)

    print(f"It deals {dealt} damage to {defender.name}")


# Reset cooldowns
def tick_cooldowns(player):
    for k in list(player.cooldowns.keys()):
        if player.cooldowns[k] > 0:
            player.cooldowns[k] -= 1