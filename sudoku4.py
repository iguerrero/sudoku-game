import random
from itertools import permutations as perm
import numpy as np

def sudokuGame():
    line = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    block =[]
    multi = perm(line)
    for p in multi:
        block.append(p)

    print(len(block))

sudokuGame()
