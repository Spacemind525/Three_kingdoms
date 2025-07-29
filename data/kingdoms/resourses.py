class ResourceManager:
    def __init__(self):
        self.resources = {
            food: 0,
            iron: 0,
            xp: 0,
        }

    def add(self, resource_type: str, amount: int) -> None:
        if resource_type in self.resources:
            self.resources[resource_type] += amount

    def consume(self, resource_type: str, amount: int) -> bool:
        if self.resources.get(resource_type, 0) >= amount:
            self.resources[resource_type] -= amount
            return True
        return False

    def get(self, resource_type: str) -> int:
        return self.resources.get(resource_type, 0)

    def has_enough(self, resource_type: str, amount: int) -> bool:
        return self.resources.get(resource_type, 0) >= amount

    def convert_to_growth(self, kingdom):
        food_growth = self.resources["food"] * 0.2
        iron_growth = self.resources["iron"] * 0.2
        xp_growth = self.resources["xp"] * 0.2

        kingdom.population += int(food_growth)

    def __str__(self):
        return f"Resources: {self.resources}"