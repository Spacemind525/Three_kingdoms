from kingdoms import kingdom
from constants import MAX_TURNS
import random

class GameManager:
    def __init__(self):
        self.turn = 1
        self.kingdoms = []
        self.player_kingdom = player_kingdom
        self.initialize_kingdom()

    def initialize_kingdom(self):
        races = ["Scholars", "Knights", "Trolls"]
        for name in ["Red", "Blue", "Green"]:
            race = random.choice(races)
            is_ai = self.player_kingdom is not None and name != self.player_kingdom.name
            self.player_kingdom.append(kingdom(name=name, race=race, is_ai=is_ai))

    def play_turn(self):
        print(f"/n===== Turn {self.turn} =====")

        for kingdom in self.kingdoms:
            if kingdom.is_alive():
                kingdom.grow()
                kingdom.resolve_siege()
                if kingdom.is_ai():
                    self.process_ai_turn(kingdom)
                else:
                    self.process_player_turn(kingdom)
        self.turn += 1

    def process_ai_turn(self, kingdom):
        pass

    def process_player_turn(self, kingdom):
        pass


    def run(self):
        while self.turn <= MAX_TURNS and any(k.is_alive() for k in self.kingdoms):
            self.play_turn()

        if MAX_TURNS == self.turn:
            print(f"Game Over! /n Statistic of game: /n {self.kingdoms}")
        if any(k.is_alive() for k in self.kingdoms):
            print(f" Game Over! Winner: {self.k}")


