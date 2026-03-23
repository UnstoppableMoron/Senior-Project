import os

os.system("")

class HealthBar:
    symbol_remaining: str = "\u2588"

    def __init__(self, entity, length: int, is_colored: bool = True, color: str = "") -> None:
        self.entity = entity
        self.length = length
        self.max_value = entity.health_max
        self.current_value = entity.health

        self.is_colored = is_colored
        self.color = color