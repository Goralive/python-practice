class Creature:
    def move(self):
        print("the creature moves")


class Dragon(Creature):
    def move(self):
        print("the dragon flies")


class Dragon:
    def __init__(self, damage):
        self.damage = damage

    # def __add__(self, other_dragon):
    #     total = self.damage + other_dragon.damage
    #     return total
    def move(self, is_flying: bool):
        print(f"Dragon is flying -> {is_flying}")


d1 = Dragon(50)
d2 = Dragon(33)
d3 = d1 + d2
print(f"Total dragons damage is -> {d3}")

dragon = Dragon(22)
creature = Creature()
dragon.move(True)
creature.move()
