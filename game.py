# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods

import random
import string

class Game:
    def __init__(self):
        self.grid = []
        for _ in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))


    def is_valid(self, word):

        if not word:
            return False

        letters = {}
        for l in self.grid:
            try:
                letters[l] += 1
            except KeyError:
                letters[l] = 1

        for i in word:
            try:
                if letters[i] == 0:
                    return False
                else:
                    letters[i] -= 1
            except KeyError:
                return False

        return True
