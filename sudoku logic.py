grid = [    [3, 0, 6, 5, 0, 8, 4, 0, 0],
            [5, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 8, 7, 0, 0, 0, 0, 3, 1],
            [0, 0, 3, 0, 1, 0, 0, 8, 0],
            [9, 0, 0, 8, 6, 3, 0, 0, 5],
            [0, 5, 0, 0, 9, 0, 6, 0, 0],
            [1, 3, 0, 0, 0, 0, 2, 5, 0],
            [0, 0, 0, 0, 0, 0, 0, 7, 4],
            [0, 0, 5, 2, 0, 6, 3, 0, 0]]

l=[0,0]

def print_grid(arr):
    for i in range(9):
        for j in range(9):
            print(grid[i][j],end=" ")
        print("")


def check_location_is_safe(sudoku, i,j,e):
        rowOk = all([e != sudoku[i][x] for x in range(9)])
        if rowOk:
            columnOk = all([e != sudoku[x][j] for x in range(9)])
            if columnOk:
                secTopX, secTopY = 3 * (i // 3), 3 * (j // 3)
                for x in range(secTopX, secTopX + 3):
                    for y in range(secTopY, secTopY + 3):
                        if sudoku[x][y] == e:
                            return False
                return True
        return False

def find_empty_location(arr):
    for row in range(9):
        for col in range(9):
            if (arr[row][col] == 0):
                return row,col
    return -1,-1


def solve_sudoku(sudoku,i=0,j=0):
    i, j = find_empty_location(sudoku)
    if i == -1:
        return True
    for e in range(1, 10):
        if check_location_is_safe(sudoku, i, j, e):
            sudoku[i][j] = e
            if solve_sudoku(sudoku, i, j):
                return True
            sudoku[i][j] = 0
    return False

if __name__ == "__main__":
    if (solve_sudoku(grid)):
        print_grid(grid)
    else:
        print("No solution exists")