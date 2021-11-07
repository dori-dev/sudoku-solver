"""Project functions
"""
from assets import puzzle, guess
chars = ("|", "--")


def draw():
    print("┌───────┬───────┬───────┐")
    for i in range(9):
        for j in range(9):
            if j % 3 == 0:
                print("│ ", end="")
            print(f"{puzzle[i][j]} ", end="")
        
        print("│")
        if i == 8:
            print("└───────┴───────┴───────┘")
        elif (i + 1) % 3 == 0:
            print("├───────┼───────┼───────┤")





def find_free():
    pass


def is_valid():
    pass


def solve():
    return True
