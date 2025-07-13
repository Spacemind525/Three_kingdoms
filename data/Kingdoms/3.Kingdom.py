

class Kingdom:
    def __init__(
            self,
            name: str,
            hp: 1000,
            defense: 50):
        self.name = name
        self.hp = hp
        self.defense = defense
        self.population = 100
        self.force = 10
        self.tech = 0
        self.food = 0
        self.iron = 0
        self.xp = 0
        self.siege_turns = 0
        self.garrison = 0
        self.buildings = []

    def grow(self):
        pop_bonus, force_bonus, tech_bonus = self.get_grow_bonus()
        self.population = int(self.population * (1 + pop_bonus / 100))
        self.force = int(self.force * (1 + force_bonus / 100))
        self.tech = int(self.tech * (1 + tech_bonus / 100))

    def get_grow_bonus(self):
        return 0, 0, 0