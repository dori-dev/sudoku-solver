"""Project functions
"""
from assets import puzzle, guess


def draw():
    for j in puzzle:
        for i in j:
            print(i, end=" ")
        print("\n")


def find_free():
    pass


def is_valid():
    pass


def solve():
    return True
