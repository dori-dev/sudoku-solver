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
        str: text with color_id in first and normalized color_id in end
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


def find_free() -> (bool, tuple):
    """Find the empty point in the table to be solved

    Returns:
        bool,postion: point postion if have free point, else False
    """
    for i in range(9):
        for j in range(9):
            if table[i][j] == 0:
                return (i, j)
    return False


def is_valid(num, x_pos, y_pos) -> bool:
    """check the point with x_pos & y_pos position and num value is valid to use in table

    Args:
        num (int): number
        x_pos (int): x postion
        y_pos (int): y postion

    Returns:
        bool: valid or not valid
    """
    for i in range(9):
        if num in (table[x_pos][i], table[i][y_pos]):
            return False

    x_square = (x_pos // 3) * 3
    y_square = (y_pos // 3) * 3

    for i in range(x_square, x_square+3):
        for j in range(y_square, y_square+3):
            if table[i][j] == num:
                return False
    return True


def solve():
    """solve the puzzle with recursive functions!

    Returns:
        bool: if number position correct True, and else False
    """
    position = find_free()
    if not position:
        return True
    x_pos = position[0]
    y_pos = position[1]
    for num in range(1, 10):
        if is_valid(num, x_pos, y_pos):
            table[x_pos][y_pos] = num
            if solve():
                return True
            table[x_pos][y_pos] = 0
    return False
