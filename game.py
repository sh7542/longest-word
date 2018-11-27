# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods

import random
import string
import requests

class Game:
    def __init__(self):
        self.grid = []
        for _ in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))


#    def is_valid(self, word):

#        if not word:
#            return False

#        letters = {}
#        for l in self.grid:
#            try:
#                letters[l] += 1
#            except KeyError:
#                letters[l] = 1

#        for i in word:
#            try:
#                if letters[i] == 0:
#                    return False
#                else:
#                    letters[i] -= 1
#            except KeyError:
#                return False

#        return True

    def is_valid(self, word):

        return self.__check_dictionary(word)

    def __check_dictionary(self, word):
        if not word:
            return False
        r = requests.get(f"https://wagon-dictionary.herokuapp.com/{word}")
        response = r.json()
        return response['found']
