class Wall:
    armor = 10
    height = 5
    depth = None
    volume = None
    width = None

    def __init__(self, depth, height, width):
        self.depth = depth
        self.height = height
        self.width = width
        self.volume = depth * height * width

    def get_cost(self):
        return self.armor * self.height

    def fortify(self):
        self.armor *= 2


def destroy_walls(wall_health):
    for w in wall_health:
        if w <= 0:
            wall_health.remove(w)
    return wall_health


def fight_soldiers(soldier_one, soldier_two):
    soldier_one_dps = get_soldier_dps(soldier_one)
    soldier_two_dps = get_soldier_dps(soldier_two)
    if soldier_one_dps > soldier_two_dps:
        return "soldier 1 wins"
    if soldier_two_dps > soldier_one_dps:
        return "soldier 2 wins"
    return "both soldiers die"


def get_soldier_dps(soldier):
    return soldier["damage"] * soldier["attacks_per_second"]
