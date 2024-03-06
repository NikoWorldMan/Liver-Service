#
# effects.py
# Status Effects class
#

"""
The "DOT" Deals damage every time it is triggered, usually at the end of a turn
The "STAT" Increases or decreases stat(s)
The "HIT" Triggers its effect when the target is hit
The ""
"""

from entity import Stats

class Triggers:
    ON_DAMAGE_TAKEN = "Take Damage"
    ON_DAMAGE_DEALT = "Deal Damage"
    ON_TURN_END = "End of Turn"

class EffectTypes:

    class DOT:
        def __init__(self, owner, triggers: Triggers) -> None:
            self.owner = owner
            self.triggers = triggers

        def trigger(self, target):
            target.change_health(self.owner.stat[Stats.ATTACK] * self.strength)

    class STAT:
        def __init__(self, stats: Stats, mult) -> None:
            self.amount = 1/((self.strength/3)+1) * mult
            self.stats = stats


class Effects:
    def __init__(self, name, duration, strength, effect_types: EffectTypes) -> None:

        self.effect_types = effect_types
        self.name = str(name)


        self.duration = duration
        self.strength = strength

    def effect_trigger(self, target):
        self.duration -= 1
        if self.duration < 1:
            target.buffs.remove(self)
        target.set_stats()


class Buff(Effects):
    def __init__(self, name, duration, strength, type: EffectTypes) -> None:
        super().__init__(name, duration, strength, type)

class Debuff(Effects):
    def __init__(self, name, duration, strength, type: EffectTypes) -> None:
        super().__init__(name, duration, strength, type)


