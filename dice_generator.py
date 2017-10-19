import numpy as np

# begin the dice class
class DiceGen():
    def __init__(self, number, sides):
        self.sides = sides
        self.number = number

    def roll(self, prof=None, attr_mod=None):
        rolls = []
        tot_mod = 0

        for i in range(self.number):
            rolls.append(np.random.randint(1, self.sides + 1))

        print("Roll total : {}".format(rolls))

        if prof is not None:
            tot_mod = tot_mod + prof
        if attr_mod is not None:
            tot_mod = tot_mod + attr_mod
        print(("Mod total : {}".format(tot_mod)))

        return sum(rolls) + tot_mod



