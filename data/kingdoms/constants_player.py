RESOURCE_TYPES = ["food", "iron", "xp"]

RESOURCE_THEFT_THRESHOLD = 0.3

RESOURCE_THEFT_PER_UNIT = 0.5



PLAYER_BUILDING_BONUSES = {
    "library": {"tech_bonus": 5},
    "barracks": {"force_bonus": 4},
    "granary": {"pop_bonus": 3},
}

PLAYER_SIEGE_BONUSES = {
    "Scholars": {"pop_bonus": -1, "force_bonus": 1, "tech_bonus": 2},
    "Knights":  {"pop_bonus": 2, "force_bonus": 2, "tech_bonus": -2},
    "Trolls":   {"pop_bonus": 5, "force_bonus": -1, "tech_bonus": -2},
}



BUILDING_DESTROY_THRESHOLD = 500

BUILDING_DESTROY_REWARD = 100