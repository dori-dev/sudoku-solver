"""Project functions
"""
from assets import puzzle, guess, characters


def draw():
    """draw the puzzle
    """
    print(characters["start"])
    for i in range(9):
        for j in range(9):
            if j % 3 == 0:
                print("│", end=" ")
            print(puzzle[i][j], end=" ")

        print("│")
        if i == 8:
            print(characters["end"])
        elif (i + 1) % 3 == 0:
            print(characters["mid"])


def find_free():
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                return [i, j]
    return False


def is_valid(n, x, y):
    for i in range(9):
        if n in (puzzle[x][i], puzzle[i][y]):
            return False

    x_square = (x // 3) * 3
    y_square = (y // 3) * 3

    for i in range(x_square, x_square+3):
        for j in range(y_square, y_square+3):
            if puzzle[i][j] == n:
                return False
    return True


def solve():
    pass
