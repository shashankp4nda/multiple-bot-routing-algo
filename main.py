# Shashank Panda :)
from msvcrt import getch
from time import sleep
import sys
import random
import math


# NOTE : axis
#    0-------------------> Y
#    |
#    |
#    |
#    |
#    |
#    |
#    V  X

# generating the environment
def generate(n, walls_v, walls_h):
    grid = [[' ' for i in range(n)] for i in range(n)]
    for i in walls_v:
        # walls_v format: (x_coordinate, start_y, end_y)
        for j in range(i[1], i[2]):
            grid[j][i[0]] = '|'
    for i in walls_h:
        # walls_v format: (y_coordinate, start_x, end_x)
        for j in range(i[1], i[2]):
            grid[i[0]][j] = '~'
    return grid


grid = generate(20, [(7, 0, 8), (12, 0, 8)], [(7, 0, 7), (7, 13, 20), (10, 0, 20)])

# starting positions: A, B, C, D
# Corresponding Destinations: W, X, Y, Z

grid[0][8] = 'A'
grid[0][9] = 'B'
grid[0][10] = 'C'
grid[0][11] = 'D'

grid[8][0] = 'W'
grid[9][0] = 'X'
grid[8][19] = 'Y'
grid[9][19] = 'Z'

# swap contents of two coordinates p1, p2 like (x, y)
def swap(p1, p2):
    grid[p1[0]][p1[1]], grid[p2[0]][p2[1]] = grid[p2[0]][p2[1]], grid[p1[0]][p1[1]]


def isWall(x, y):
    return True if grid[x][y] in ['~', '|', 'A', 'B', 'C', 'D', 'W', 'X', 'Y', 'Z'] else False


def boundCheck(x, y):
    if x >= 20 or y >= 20 or x < 0 or y < 0:
        return False
    return True


def neighbourhood(x, y):
    if not boundCheck(x, y):
        return []
    neighbours = []
    if (not isWall(x + 1, y)) and boundCheck(x + 1, y):
        neighbours.append((x + 1, y))
    if (not isWall(x, y + 1)) and boundCheck(x, y + 1):
        neighbours.append((x, y + 1))
    if (not isWall(x - 1, y)) and boundCheck(x - 1, y):
        neighbours.append((x - 1, y))
    if (not isWall(x, y - 1)) and boundCheck(x, y - 1):
        neighbours.append((x, y - 1))
    for i in neighbours:
        print(i)
    return neighbours


# Heuristic Function
def h(cell, goal):
    return abs(goal[0] - cell[0]) + abs(goal[1] - cell[1])


# A* Search
def Astar(cell, goal):
    min = h(cell, goal)
    next = cell
    for i in neighbourhood(cell[0], cell[1]):
        if h(i, goal) < min:
            min = h(i, goal)
            next = i
    return next


def display():
    for j in grid:
        for i in j:
            print(i, end=' ')
        print()


# Goal dictionary mapped with symbols
GoalDictSymbols = {'A': 'W', 'B': 'X', 'C': 'Z', 'D': 'Y'}
# Goal dictionary mapped with coordinates
GoalDict = {
    (0, 8): (8, 0),
    (0, 9): (9, 0),
    (0, 10): (9, 19),
    (0, 11): (8, 19)
}


# Path plot for a single state and single goal
def pathPlotSingle(state, goal):
    while h(state, goal) > 1:
        # swap(state, Astar(state, goal))
        new = Astar(state, goal)
        # grid[state[0]][state[1]], grid[new[0]][new[1]] = grid[new[0]][new[1]], grid[state[0]][state[1]]
        swap(state, new)
        state = new
        display()
        sleep(0.5)


# Path plot for all states and goals simultaneously
# states: [(Xa, Ya), (Xb, Yb), (Xc, Yc), (Xd, Yd)]
# goals: [(Xw, Yw), (Xx, Yx), (Xy, Yy), (Xz, Yz)]
def pathPlot(states, goals):
    cursors = states
    flag = 4
    while flag != 0:
        prev = [i for i in cursors]
        for i in range(len(cursors)):
            min = float("Inf")
            new = Astar(cursors[i], goals[i])
            swap(cursors[i], new)
            cursors[i] = new
        flag = 0
        for i in range(len(cursors)):
            if h(cursors[i], goals[i]) > 1:
                flag += 1
        # deadlock resolution---------
        for i in range(len(cursors)):
            if cursors[i] == prev[i] and h(cursors[i], goals[i]) > 1:
                n = neighbourhood(cursors[i][0], cursors[i][1])
                index = math.floor(random.random() * 10) % len(n)
                swap(cursors[i], n[index])
                cursors[i] = n[index]
        # -----------------------------
        print(cursors)
        print(prev)
        display()
        sleep(0.5)


def main():
    display()
    sleep(0.5)
    states, goals = [], []
    for i in GoalDict:
        states.append(i)
        goals.append(GoalDict[i])
    pathPlot(states, goals)
    # states = []
    # for i in GoalDict:
    #     states.append(i)
    # pathPlot([(8, 1), (9, 1), (8, 18), (9, 18)], states)


if __name__ == "__main__":
    main()

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ &,//%((((..,,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@  (((((##(#. .......@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@ .** |O...  *%/ *. .     .@@@@@@@@@@@R2D2@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@. *. #%##%.,/ .//..&%% %##  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@.*((###%%%&&&%&@@&&,.(#&%%%# ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@,  (&@@@@@@@@@&%@/,,....&&%.& /*@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@     .####%%%@........../(...#(#@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@   ,          ................,     .. @@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@    .  .((###%#%%%#%@@&.........,.    ......@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@    .          ................., .......,/..@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@    .      (@&&@  ..............,,......../.*@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@ .  .      @@@&#................,*,......&%#/.@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@%        .*&&.%  ...............,,(...../&&((.@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@        ./   #.................,(@,.....@&**.@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@      .#/(&#. ................,&/&,.....&,/@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@        ....................../&,@,,,,@%*/@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@.     %/**%...................%&# @@,,,.%%.@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@ /  .#&  *,.....................% @@,,,.&#.@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@ .  . #/,/#..........,.&..&@......@@@.,..%%.,@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@ ..   ..... ............&&&&......@@@,,,.# .,@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@. .   .......,*,........,.......@@@@.,,.....@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@  .,****,......,,,............@@@@.,,,....%@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@. ..,,**..,,/#/.........,,.@@@@@.,,,,..##..@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@*... ,,....,,.,,,/*/...,(@@@,,,,,,/*,**.*(.@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@   .  ........,,.(@@@@@@@@@@@,/,/,,,,,*.,.... @@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@   .  ., ..,((*... @@@@@@@@@@@.*#*,,,,,,........@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@   ../% .,* ..,,,,.(@@@@@@@@@@@,,/#%%##*,........  @@@@@@@@@@@@@@
# @@@@@@@@@@@@@     *.... .....,.,,,,@@@@@@@@@@@##(###*,,........... %@@@@@@@@@@@@
# @@@@@@@@@@@@@/.... . . ......,,,,,,,,@@@@@@@@@@@,,,,/*............ @@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@..    ........,,,,,,%@@@@@@@@@ ,,,,,,,,,..........@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@.......,,,,,,*/@@@@@@@@@@@@@@@&&@%@@ ..( @@@@@@@@@@@@@@@@@@@
