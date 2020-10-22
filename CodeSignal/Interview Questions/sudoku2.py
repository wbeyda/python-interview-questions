def sudoku2(grid):
    '''
     for row in grid:
        filtered_row = list(filter(('.').__ne__, row))
        if len(set(filtered_row)) != len(filtered_row):
            return False
    flipped = list(zip(*grid[::-1]))
    for col in flipped:
        filtered_col = list(filter(('.').__ne__, col))
        if len(set(filtered_col)) != len(filtered_col):
            return False
    return True
    '''
    l = list(range(1, 10))
    def checkInnerGrids(x, y):
        a = [grid[i][j] for i in range(x, x + 3) for j in range(y, y + 3) if grid[i][j] != '.']
        b = set([grid[i][j] for i in range(x, x + 3) for j in range(y, y + 3) if grid[i][j] != '.'])
        # print('a',a,'b',b,len(a) == len(b))
        return len(a) == len(b)

    def checkLinesColumns(i):
        a = set(j for j in grid[i] if j != '.')
        b = [j for j in grid[i] if j != '.']
        c = set([grid[x][i] for x in range(9) if grid[x][i] != '.'])
        d = [grid[x][i] for x in range(9) if grid[x][i] != '.']
        return len(a) == len(b) and len(c) == len(d)

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not checkInnerGrids(i, j):
                return False
    for i in range(9):
        if not checkLinesColumns(i):
            return False
    return True


if __name__ == '__main__':
    grid = [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
            ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
            ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
            ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
            ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
            ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
            ['.', '.', '.', '5', '.', '.', '.', '7', '.']]

    grid2 = [['.', '.', '.', '1', '1', '.', '.', '2', '.'],
            ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
            ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
            ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
            ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
            ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
            ['.', '.', '.', '5', '.', '.', '.', '7', '.']]

    grid3 = [[".",".",".",".",".",".",".",".","2"],
             [".",".",".",".",".",".","6",".","."],
             [".",".","1","4",".",".","8",".","."],
             [".",".",".",".",".",".",".",".","."],
             [".",".",".",".",".",".",".",".","."],
             [".",".",".",".","3",".",".",".","."],
             ["5",".","8","6",".",".",".",".","."],
             [".","9",".",".",".",".","4",".","."],
             [".",".",".",".","5",".",".",".","."]]

    assert sudoku2(grid) == True
    assert sudoku2(grid2) == False
    assert sudoku2(grid3) == True
