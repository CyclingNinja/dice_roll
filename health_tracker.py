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

        if self.hp < self.bloodied:
            return "You are bloodied"
        elif self.hp <= 0:
            return "Curl up and await the icy embrace of death"
        else:
            pass

    def heal_up(self, points):
        self.hp = self.hp + points

        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def short_rest(self):
        self.hp = self.hp + self.max_hp / 2.0

    def long_rest(self):
        self.hp = self.max_hp

    def get_points(self):
        print("Current Points : {}".format(self.hp))