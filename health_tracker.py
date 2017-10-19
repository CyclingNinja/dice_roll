import numpy as np

class HitPoints():
    def __init__(self, total_hp):
        self.hp = total_hp
        self.total_hp = total_hp


    def take_pain(self, points):
        self.hp = self.hp - points

    def heal_up(self, points):
        self.hp = self.hp + points

    def short_rest(self):
        pass

    def long_rest(self):
        pass