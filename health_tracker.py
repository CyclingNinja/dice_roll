import numpy as np

class HitPoints():
    def __init__(self, max_hp):
        # initialise the varying hp
        self.hp = max_hp

        # hold some stats in memory
        self.max_hp = max_hp
        self.bloodied = max_hp / 2.0
        self.death = self.bloodied * -1.0


    def take_pain(self, points):
        self.hp = self.hp - points


    def heal_up(self, points):
        self.hp = self.hp + points

    def short_rest(self):
        pass

    def long_rest(self):
        pass

    def get_points(self):
        print("Current Points : {}".format(self.hp))