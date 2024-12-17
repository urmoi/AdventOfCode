# https://adventofcode.com/2024/day/16

with open('input.txt') as f:
    data = f.read().splitlines()

maze = data

START = 'S'
END = 'E'
WALL = '#'

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
START_DIR = 0

COST_STEP = 1
COST_ROT = 1000

# Part One

def find_pos(maze, find):
    ly = len(maze)
    lx = len(maze[0])
    for y in range(ly):
        for x in range(lx):
            if maze[y][x] == find:
                return (y, x)
    return (-1, -1)

def calc_cost(cost, ori, dir):
    cost += COST_STEP
    if abs(ori[0]) != abs(dir[0]):
        cost += COST_ROT
    return cost

def calc_heuristic(pos, dir, epos):
    dy = epos[0] - pos[0]
    dx = epos[1] - pos[1]
    ds = abs(dy) + abs(dx)

    dry = 0 if dir[0] * dy > 0 else 1
    drx = 0 if dir[1] * dx > 0 else 1
    dr = dry + drx

    h = ds * COST_STEP + dr * COST_ROT
    return h

def solve_maze(maze, start, end):

    start_node = (start, 0, 0, DIRECTIONS[START_DIR])

    frontier = set()
    visited = set()

    frontier.add(start_node)

    while True:
        node = min(frontier, key = lambda n: n[1] + n[2])
        pos, cost, heur, ori = node

        frontier.remove(node)
        visited.add(pos)

        if pos == end:
            return cost
        
        for dir in DIRECTIONS:
            next_pos = pos[0]+dir[0], pos[1]+dir[1]
            if next_pos in visited or maze[next_pos[0]][next_pos[1]] == WALL:
                continue
            next_node = (next_pos, calc_cost(cost, ori, dir), calc_heuristic(next_pos, dir, end), dir)
            frontier.add(next_node)
            
points = solve_maze(maze, find_pos(maze, START), find_pos(maze, END))
print(points)
    
# Part Two