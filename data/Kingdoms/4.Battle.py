import random
from Kingdoms import Kingdom

def attack(attacker: Kingdom, defender: Kingdom):
    #Attacker preparing to attack
    sent_percent = random.uniform(0.3, 0.6)
    sent_people = int(attacker.population * sent_percent)
    attacker.population -= sent_people
    attacker.force -= int(sent_people * 0.1)

    #calculation Damage
    damage = ((sent_people + attacker.force) - (defender.defense + defender.force * 0.50))
    def_percent = random.uniform(0.1, 0.4)
    max_garrison = int(defender.population * def_percent)
    battle = damage - max_garrison

    if battle > 0:
        total_damage = defender.take_damage(battle)
    else:
        total_damage = 0

    #increase Tech
    attacker.tech += int(damage * 1.3)
    defender.tech += int(damage * 0.6)
