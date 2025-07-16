Three Kingdoms — Strategy Game
A turn-based strategy game featuring two gameplay modes:

Auto-play: where three AI-controlled kingdoms make decisions and engage in strategic combat.

Manual mode: where the player selects a race and makes turn-based decisions such as development, production, or military action.

Kingdom Types and Their Bonuses
Each kingdom has unique characteristics reflected in growth rates per turn:

Scholars

Population growth: +2%

Military strength: +3%

Technological progress: +5%

Description: High technological potential, low population growth, and strong defense.

Knights

Population growth: +3%

Military strength: +5%

Technological progress: +2%

Description: Well-equipped, moderate growth, balanced development.

Trolls

Population growth: +7%

Military strength: +2%

Technological progress: +1%

Description: Massive population growth, weak technology and moderate strength.

Castle Attributes (Shared by All Kingdoms)
Health: 1000

Defense: 50 (can block damage, but not more than 25% of total castle HP)

Castle HP can be increased using either population or technology points.

A garrison can be formed using up to 30% of the kingdom’s population, with the following mechanics:

Exchange rate favors the defenders at 1 : 1.2

Attackers gain more tech during battle at 1 : 1.3 rate

Example Battle Calculation:
If an enemy sends 200 troops with 75 military strength and defenders have 600 population:


damage = 200 + 75 - 50 = 225  
max_garrison = 30% of 600 = 180  
battle_damage = 225 - 180 = 45  
castle_health = 1000 - 45 = 955
Core Resources
Population

Military Force

Technological Progress

The game advances year by year (turn-based). Every 10–25 turns, AI kingdoms attack the weakest one.
However:

A kingdom can't be attacked if it was attacked within the last 7 turns, unless it initiated an attack itself.

A siege can last up to 20 turns, after which the attacking army dies from exhaustion.

The third (non-involved) kingdom may only attack the aggressor, not the defender.

Attack and Defense Mechanics
During an attack, the kingdom can allocate 10%–60% of its population.

Garrison loses military power and defense points over time.

During a siege, only 30% of the population can defend; the rest continue producing resources.

Reinforcements (up to 10% of the population) can be sent every 10 turns.

Repairing a castle during peacetime is more efficient than under siege:

In siege: 2%–10% of invested resources may be lost randomly.

Repairs are 15% less effective during a siege.

Elimination Bonus
If a kingdom is destroyed:

Aggressor receives +6% to all resource growth for 10 turns.

The remaining kingdom gets +500 HP to its castle.

Player Mode
The player can:

Choose one of the three races

Play manually by issuing commands

Extract resources:

Food

Iron

Experience

Attack, defend, build structures, or develop technology.

A centralized game controller module will manage all game logic and include imported modules.

Sieges & City Effects
During a siege, race-specific bonuses apply:

Scholars

Population growth: –1%

Military growth: +1%

Tech growth: +2%

Knights

Population growth: +2%

Military force: +2%

Tech progress: –2%

Trolls

Population growth: +5%

Military force: –1%

Tech progress: –2%

Note: No stat can drop below 0%. If that happens, an additional –1% penalty applies to all growth rates.

Planned Features
Construction system:

Build houses, barracks, farms, and mines

Each building affects growth rates of related resources

Buildings can be destroyed during siege (especially if castle HP drops below 50%)

Castle walls upgrades

Increases garrison capacity

Siege weapons:

Built with technology

Reduce battle losses during an assault

