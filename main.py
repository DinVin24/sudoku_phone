
class Cell:
    def __init__(self, val, fix):
        self.val = val
        self.fix = fix



def read_puzzle(filename):
    s = [[Cell(0, False) for _ in range(10)] for _ in range(10)]
    with open(filename, "r") as file:
        for i, line in enumerate(file, start=1):
            line = list(map(int, line.strip().split()))
            for j in range(1, 10):
                s[i][j].val = line[j - 1]
                s[i][j].fix = s[i][j].val != 0
    return s

def is_valid(s, x, y, num):
    for i in range(1, 10):
        if s[x][i].val == num or s[i][y].val == num:
            return False

    box_row, box_col = (x - 1) // 3 * 3 + 1, (y - 1) // 3 * 3 + 1
    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            if s[i][j].val == num:
                return False

    return True

def solve_sudoku(s, x, y):
    if x > 9:
        return True
    if s[x][y].fix:
        if y == 9:
            return solve_sudoku(s, x + 1, 1)
        else:
            return solve_sudoku(s, x, y + 1)

    for num in range(1, 10):
        if is_valid(s, x, y, num):
            s[x][y].val = num
            if y == 9:
                if solve_sudoku(s, x + 1, 1):
                    return True
            else:
                if solve_sudoku(s, x, y + 1):
                    return True
            s[x][y].val = 0

    return False

def print_puzzle(s):
    for i in range(1, 10):
        for j in range(1, 10):
            print(s[i][j].val, end=' ')
        print()

#sudoku = read_puzzle("date.in")
#solve_sudoku(sudoku, 1, 1)
#print_puzzle(sudoku)
