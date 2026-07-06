class Character:
    def __init__(self, health, damage, speed):
        self.health = health
        self.damage = damage
        self.speed = speed

    def take_damage(self, amount):
        self.health -= amount


class Warrior(Character):
    def __init__(self, health, damage, speed):
        super().__init__(health, damage, speed)
        self.toughness_modifier = 0.90

    def take_damage(self, amount):
        modified_amount = amount * self.toughness_modifier
        super().take_damage(modified_amount)


warrior = Warrior(100, 50, 10)
print(f"Initial health: {warrior.health}")
warrior.take_damage(40)
print(f"Health after damage: {warrior.health}")