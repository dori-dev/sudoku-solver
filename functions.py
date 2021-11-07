"""Project functions
"""
# Local imports
from assets import table, changed
from assets import characters, colors


def specify_solved_points():
    """Specify the points to be solved
    """
    for i in range(9):
        for j in range(9):
            if table[i][j] == 0:
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
    """draw the table in terminal
    """
    print(make_colors('border', characters['start']))
    for i in range(9):
        for j in range(9):
            if j % 3 == 0:
                print(make_colors('border', "│"), end=" ")

            if changed[i][j]:
                print(make_colors('solve_number', table[i][j]), end=" ")
            else:
                print(table[i][j], end=" ")

        print(make_colors('border', "│"))
        if i == 8:
            print(make_colors('border', characters['end']))
        elif (i + 1) % 3 == 0:
            print(make_colors('border', characters['center']))


def find_free() -> (bool, list):
    """Find the empty point in the table to be solved

    Returns:
        bool,postion: point postion if have free point, else False
    """
    for i in range(9):
        for j in range(9):
            if table[i][j] == 0:
                return [i, j]
    return False


def is_valid(n, x, y) -> bool:
    """check the point with x & y position and n value is valid to use in table

    Args:
        n (int): number
        x (int): x postion
        y (int): y postion

    Returns:
        bool: valid or not valid
    """
    for i in range(9):
        if n in (table[x][i], table[i][y]):
            return False

    x_square = (x // 3) * 3
    y_square = (y // 3) * 3

    for i in range(x_square, x_square+3):
        for j in range(y_square, y_square+3):
            if table[i][j] == n:
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
            table[x][y] = n
            if solve():
                return True
            table[x][y] = 0
    return False
