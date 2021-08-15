from random import choice
from itertools import permutations
import numpy as np

def sudokuGame():

    latA = latSqr(1)
    latB = latSqr(4)
    latC = latSqr(7)
    choices = []
    permuts = permutations([latA, latB, latC])
    for i in permuts:
        choices.append(i)
    order = choice(choices)
    print(order)

    a = [order[0][0], order [1][0], order[2][0]]
    b = [order[0][1], order [1][1], order[2][1]]
    c = [order[0][2], order [1][2], order[2][2]]

    lats = [[[a, b, c], [b, c, a], [c, a, b]], [[a, b, c], [c, a, b], [b, c, a]]]
    lat = choice(lats)
    grid_in = np.array(lat)
    grid_out = grid_in.reshape(9,9)

    print(grid_out)

        # a = random.choice(range(1,13))

def latSqr(x):
    choices =[]
    permuts = permutations([x, x + 1, x + 2])
    for i in permuts:
        choices.append(i)
    ord = choice(choices)
    a, b, c = ord
    lats = [[[a, b, c], [b, c, a], [c, a, b]],[[a, b, c], [c, a, b], [b, c, a]]]
    lat = choice(lats)

    return lat

sudokuGame()