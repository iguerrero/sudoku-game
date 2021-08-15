# Sudoku Game
import numpy as np
import random

sudoku_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def sudokuGame():
    sudoku = np.empty([9,9], dtype=np.int8)
    np.random.shuffle(sudoku_list)
    sudoku[0] += sudoku_list
    while len(sudoku) < 9:
        nextRow = []
        choices = sudoku_list
        while len(nextRow) < 9:
            randomNum = random.choice(choices)
            while not (checkRow(nextRow, randomNum) and checkCol(sudoku, nextRow, randomNum) and checkBlock(sudoku, nextRow, randomNum)):
                choices.remove(randomNum)
                # print(choices)
                randomNum = random.choice(choices)
            # print(randomNum)
            nextRow.append(randomNum)
        # print(nextRow)
        sudoku.append(nextRow)
    print(sudoku)


def checkRow(aNewRow, num):
    if num in aNewRow:
        return False
    else:
        return True


def checkCol(sudoku, aNewRow, num):
    l = len(aNewRow)
    # while l < 10:
    for row in sudoku:
        if row[l] == num:
            return False
    return True


def checkBlock(sudoku, aNewRow, num):
    r = len(sudoku)
    i = len(aNewRow)
    fr, tr = (r//3)*3, r
    fc, tc = (i//3)*3, (i//3)*3+3
    for row in sudoku[fr:tr]:
        if num in row[fc:tc]:
            return False
    return True


sudokuGame()

