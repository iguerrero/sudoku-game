# Sudoku Game
import numpy as np
import random

def sudokuGame():
    sudoku_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    sudoku = []
    random.shuffle(sudoku_list)
    newSudoku = sudoku_list.copy()##
    sudoku.append(newSudoku)
    print(sudoku)# First Sudoku row.
    while len(sudoku) < 9:
        choices = sudoku_list.copy()
        nextRow = []
        while len(nextRow) < 9 and len(choices) > 0:
            random.shuffle(sudoku_list)  ##
            randomNum = random.choice(choices)
            while not (checkRow(nextRow, randomNum) and checkCol(sudoku, nextRow, randomNum) and checkBlock(sudoku, nextRow, randomNum) and checkLast(sudoku, randomNum)):
                choices.remove(randomNum)
                if len(choices) > 0:
                    randomNum = random.choice(choices)
                print(randomNum)
            nextRow.append(randomNum)
            print(nextRow)
        sudoku.append(nextRow)
        print(sudoku)
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

def checkLast(sudoku, num):
    r = len(sudoku)
    # i = len(aNewRow)
    fr, tr = (r//3)*3, r
    # fc, tc = (i//3)*3, (i//3)*3+3
    if (1 < r > 4) or (4 < r > 7) or (7 < r >= 9):
        for row in sudoku[fr:tr]:
            a = 0
            if num in row[6:9]:
                a += 1
            if a == 0:
                return False
    return True

sudokuGame()

