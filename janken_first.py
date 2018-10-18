import numpy as np
import random


def pair_to_int(te1, te2):
    if te1 == te2:
        return 0
    elif te == "g" and te_com == "c":
        return 1
    elif te == "c" and te_com == "p":
        return 1
    elif te == "p" and te_com == "g":
        return 1
    else:
        return 2


def int_to_te(te, n):
    if te == "g":
        return ["g", "p", "c"][n]
    elif te == "c":
        return ["c", "g", "p"][n]
    else:
        return ["p", "c", "g"][n]


class Game:
    def __init__(self):
        self.win = 0
        self.lose = 0
        self.draw = 0

    def play(self, te, te_com):
        val = pair_to_int(te, te_com)
        if val == 0:
            self.draw += 1
        elif val == 1:
            self.win += 1
        else:
            self.lose += 1
        print("w:", self.win, "l:", self.lose, "d:", self.draw)


class AI:
    def __init__(self):
        self.log = np.ones((3, 3, 3))
        self.te = list()

    def think(self):
        if len(self.te) >= 3:
            val1 = pair_to_int(self.te[-3], self.te[-2])
            val2 = pair_to_int(self.te[-2], self.te[-1])
            sum = np.sum(self.log[val1, val2])
            p = self.log[val1, val2] / sum
            r = random.random()
            if r < p[0]:
                return int_to_te(self.te[-1], 1)
            elif r < p[0] + p[1]:
                return int_to_te(self.te[-1], 0)
            else:
                return int_to_te(self.te[-1], 2)
        return random.choice(["g", "c", "p"])

    def feed(self, te):
        self.te.append(te)
        if len(self.te) >= 4:
            val1 = pair_to_int(self.te[-4], self.te[-3])
            val2 = pair_to_int(self.te[-3], self.te[-2])
            val3 = pair_to_int(self.te[-2], self.te[-1])
            print(self.te[-4:])
            print([val1, val2, val3])
            self.log[val1, val2, val3] += 1
        print(self.te)
        print(self.log)


game = Game()
com = AI()
while True:
    te = input()
    if te == "g" or te == "c" or te == "p":
        te_com = com.think()
        print("com:", te_com)
        game.play(te, te_com)
        com.feed(te)
    elif te == "q":
        exit(0)
