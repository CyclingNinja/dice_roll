import numpy as np

class HitPoints():
    def __init__(self, hp):
        self.hp = hp

    def take_pain(self, points):
        self.hp = self.hp - points

    def heal_up(self, points):
        self.hp = self.hp + points

    