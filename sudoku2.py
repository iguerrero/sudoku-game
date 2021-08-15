import random

def sudokuGame():

    sudoku = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    excluded = []

    cols = ([0, 1, 2], [3, 4, 5], [6, 7, 8])
    rows = ([0, 1, 2], [3, 4, 5], [6, 7, 8])

    for num in range(1, 10): # Numbers 1-9
        col = []
        row = []
        col.append(list(cols[0]))
        col.append(list(cols[1]))
        col.append(list(cols[2]))
        row.append(list(rows[0]))
        row.append(list(rows[1]))
        row.append(list(rows[2]))
        print(num) # Debugging

        for j in range(3): # 3 horizontal blocks, 3 rows each.
            for k in range(3): # 3 vertical blocks, 3 columns each.
                done = False
                while not done:
                    x_axis = random.choice(row[j]) # Why!!??
                    y_axis = random.choice(col[k])
                    coords = [x_axis, y_axis]

                    if coords not in excluded: # Exclude if already in use.
                        excluded.append(coords)
                        excluded.sort() # TOC
                        # print(excluded) # Debugging
                        sudoku[x_axis][y_axis] = num
                        col[k].remove(y_axis)
                        row[j].remove(x_axis)
                        done = True
                    # else:
                    #     continue

    print(sudoku)


sudokuGame()
