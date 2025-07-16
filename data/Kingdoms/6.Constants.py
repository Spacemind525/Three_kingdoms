CASTLE_INITIAL_HP = 1000
CASTLE_INITIAL_DEFENSE = 50
CASTLE_DEFENSE_LIMIT_PERCENT = 0.25

MAX_ATTACK_PERCENT = 0.6
MIN_ATTACK_PERCENT = 0.3
MAX_DEFENSE_PERCENT = 0.3

BONUSES = {
    "Scholars": {"pop_bonus": 2, "force_bonus": 3, "tech_bonus": 5},
    "Knights": {"pop_bonus": 3, "force_bonus": 5, "tech_bonus": 2},
    "Trolls": {"pop_bonus": 7, "force_bonus": 2, "tech_bonus": 1},
}

SIEGE_BONUSES = {
    "Scholars": {"pop_bonus": 2, "force_bonus": 3, "tech_bonus": 5},
    "Knights": {"pop_bonus": 3, "force_bonus": 5, "tech_bonus": 2},
    "Trolls": {"pop_bonus": 7, "force_bonus": 2, "tech_bonus": 1},
}

SIEGE_RESOURCE_PENALTY = 0.01

MAX_TURNS = 100
PROTECTION_TURNS_AFTER_ATTACK = 7
ATTACK_EXPIRE_TURN = 20
BONUS_AFTER_DESTROYING_RACE = {""}

RESOURCE_TYPES = ["food", "iron", "xp"]