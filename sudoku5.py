import random
from itertools import permutations as pm
import numpy as np


def sudokuGame():
    sudoku_line = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    sudoku_clusters = []
    # a = [0,9]
    line = sudoku_line.copy()
    for i in range(3):
        if i > 0:
            for j in range(0,8,3):
                line.insert(j+3,line[j])
                line.pop(j)
        sudoku_clusters += arrangeLine(line)
    sudoku = np.array(sudoku_clusters)
    sudoku.reshape(9,9)
    print(sudoku)
    # sudokuT = sudoku.T
    # sudokuT.reshape(9,9)
    rand = sudoku_line.copy()
    rand = [x - 1 for x in rand]
    indexList =[]
    for k in pm(rand):

        indexList.append(k)
    index = random.choice(indexList)
    print(index)
    sudoku = sudoku[:, index]
    # sudoku = sudoku.T
    # index = [8, 0, 6, 1, 2, 7, 4, 3, 5]
    # sudoku = sudoku.T
    # sudoku = sudoku[:, index]

    # Rearrange columns according to index

    print(sudoku)


def arrangeLine(sudoku_line):
    sudoku_cluster = []
    for i in range(3):
        sudoku_cluster.append(sudoku_line[0:9])
        for j in range(3):
            sudoku_line.append(sudoku_line[0])
            sudoku_line.pop(0)
    return sudoku_cluster


sudokuGame()