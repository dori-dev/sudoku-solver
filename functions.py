"""Project functions
"""
from assets import puzzle, changed
from assets import characters, colors


def specify_solved_points():
    """Specify the points to be solved
    """
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                changed[i][j] = 1


def make_colors(color: str, text: str) -> str:
    """Colorizing the text

    Args:
        color (str): color name
        text (str): text

    Returns:
        str: text with color id in first and normalized color in end
    """
    return f"{colors[color]}{text}{colors['normal']}"


def draw():
    """draw the puzzle
    """
    print(make_colors('border', characters['start']))
    for i in range(9):
        for j in range(9):
            if j % 3 == 0:
                print(make_colors('border', "│"), end=" ")

            if changed[i][j]:
                print(make_colors('solve_number', puzzle[i][j]), end=" ")
            else:
                print(puzzle[i][j], end=" ")

        print(make_colors('border', "│"))
        if i == 8:
            print(make_colors('border', characters['end']))
        elif (i + 1) % 3 == 0:
            print(make_colors('border', characters['mid']))


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
    position = find_free()
    if not position:
        return True
    x = position[0]
    y = position[1]
    for n in range(1, 10):
        if is_valid(n, x, y):
            puzzle[x][y] = n
            if solve():
                return True
            puzzle[x][y] = 0
    return False
