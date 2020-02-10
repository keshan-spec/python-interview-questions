"""
Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with numbers in such a way that each column,
each row, and each of the nine 3 × 3 sub-grids that compose the grid all contain all of the numbers from 1 to 9 one time.

Sample
grid = [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
        ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
        ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
        ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
        ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
        ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
        ['.', '.', '.', '5', '.', '.', '.', '7', '.']]
Return True

grid = [['.', '.', '.', '.', '2', '.', '.', '9', '.'],
        ['.', '.', '.', '.', '6', '.', '.', '.', '.'],
        ['7', '1', '.', '.', '7', '5', '.', '.', '.'],
        ['.', '7', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '8', '3', '.', '.', '.'],
        ['.', '.', '8', '.', '.', '7', '.', '6', '.'],
        ['.', '.', '.', '.', '.', '2', '.', '.', '.'],
        ['.', '1', '.', '2', '.', '.', '.', '.', '.'],
        ['.', '2', '.', '.', '3', '.', '.', '.', '.']]
Return False

The given grid is not correct because there are two 1s in the second column.
Each column, each row, and each 3 × 3 subgrid can only contain the numbers 1 through 9 one time

"""

g = [[".",".",".","1","4",".",".","2","."],
         [".",".","6",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".","1",".",".",".",".",".","."],
         [".","6","7",".",".",".",".",".","9"],
         [".",".",".",".",".",".","8","1","."],
         [".","3",".",".",".",".",".",".","6"],
         [".",".",".",".",".","7",".",".","."],
         [".",".",".","5",".",".",".","7","."]]


def sudoko(grid):
    hmap = []
    # gets 3 rows
    mats_3x3x9 = [grid[3 * i:3 * i + 3] for i in range(3)]
    mats_9x3x3 = [
        [row_1x9[3 * i:3 * i + 3] for row_1x9 in rows_3x9]
        for i in range(3)
        for rows_3x9 in mats_3x3x9
    ]

    for mat_3x3 in mats_9x3x3:
        a = []
        [a.append(x) if x != '.' else 0 for mat_1x1 in mat_3x3 for x in mat_1x1]
        print(a)
        if len(set(a)) < len(a):
            return False

    for i, data in enumerate(grid):
        # columns
        for j in range(0, len(grid)):
            if grid[j][i] in hmap:
                return False
            elif grid[j][i] != '.':
                hmap.append(grid[j][i])
        hmap.clear()

        # rows
        for j in range(0, len(grid)):
            if grid[i][j] in hmap:
                return False
            elif grid[i][j] != '.':
                hmap.append(grid[i][j])
        hmap.clear()

    return True


print(sudoko(g))
