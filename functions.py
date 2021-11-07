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
    pass


def is_valid():
    pass


def solve():
    return True
