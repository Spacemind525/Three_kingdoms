

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

    def take_damage(self,raw_damage: int) -> int:
        blocked = min(raw_damage,(self.hp * 0.25), self.defense)
        real_damage = raw_damage - blocked
        self.hp = max(0, self.hp - real_damage)
        return real_damage

    def get_grow_bonus(self):
        return 0, 0, 0

    def is_alive(self):
        return self.hp > 0

    def can_attack(self):
        return (
            self.population >= 300 and
            current_turn => 5 and
            current_turn - enemy.last_attacked_turn >= 7
        )

class ScholarsKingdom(Kingdom):
    def get_grow_bonus(self):
        pop_bonus, force_bonus, tech_bonus = 2, 3, 5
        if self.siege_turns > 0:
            pop_bonus -= 1
            force_bonus += 1
            tech_bonus += 2


class KnightsKingdom(Kingdom):
    def get_grow_bonus(self):
        pop_bonus, force_bonus, tech_bonus = 3, 5, 2
        if self.siege_turns > 0:
            pop_bonus += 2
            force_bonus += 2
            tech_bonus -= 2


class TrollsKingdom(Kingdom):
    def get_grow_bonus(self):
        pop_bonus, force_bonus, tech_bonus = 7, 2, 1
        if self.siege_turns > 0:
            pop_bonus += 5
            force_bonus -= 1
            tech_bonus -= 2
