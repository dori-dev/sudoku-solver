from functions import specify_solved_points, solve, draw

specify_solved_points()
if solve():
    draw()
else:
    print('I can\'t solve it!')
