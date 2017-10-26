import numpy as np
from fuzzywuzzy import fuzz
from fuzzywuzzy import process


class HitPoints:
    def __init__(self, max_hp):
        # initialise the varying hp
        self.hp = max_hp

        # hold some stats in memory
        self.max_hp = max_hp
        self.bloodied = max_hp / 2.0
        self.death = self.bloodied * -1.0

    def take_pain(self, points):
        self.hp = self.hp - points

        if (self.hp < self.bloodied) & (self.hp > 0):
            return "You are bloodied"
        elif self.hp <= 0:
            return "Curl up and await the icy embrace of death"
        elif (self.hp <= self.death):
            return "The spark of your life is smothered in shite"

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

    def save_throw_res(self):
        if self.hp <= 0:
            self.hp = 1
        else:
            return "Congrats! not dead! . . . yet"

    def get_points(self):
        # print("Current Points : {}".format(self.hp))
        return self.hp


class Characters:
    # https://stackoverflow.com/questions/14795546/what-is-the-dfifference-between-instance-dict-and-class-dict
    class_dict = {}

    def __init__(self, char_name):
        self.char_dict = char_name

    def create_character(self, character_name, hp):
        self.char_dict[character_name] = HitPoints(hp)

    def get_characters(self):
        for i, name in self.char_dict.items():
            print(i, name.get_points())

    def perform_operation(self, char_name, method_string, val=None):
        # get list of function names from HP
        hp_names = dir(HitPoints(0))

        method = process.extractOne(method_string, hp_names)
        if val is not None:
            getattr(self.char_dict[char_name], method[0])(val)
        else:
            getattr(self.char_dict[char_name], method[0])







