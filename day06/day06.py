# https://adventofcode.com/2024/day/6

with open('input.txt') as f:
    data = f.read().splitlines()

directions = [ # in clockwise direction, starting with up (x, y)
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1)
]

map = data.copy()

OBSTACLE = '#'
START = '^'
VISITED = 'X'

# Part One

def find_starting_pos(map):
    for y, line in enumerate(map):
        for x, cell in enumerate(line):
            if cell == START:
                return ((y, x,), directions[0])
    return ((0,0), directions[0]) # just for safty

guard_pos, guard_dir = find_starting_pos(map)

def pos_in_map(map, pos):
    y, x = pos
    if (y < 0 or y >= len(map)) or (x < 0 or x >= len(map[0])):
        return False
    return True

def guard_in_map(map, pos):
    return pos_in_map(map, pos)

def guard_can_move(map, pos, dir):
    y, x = pos
    dy, dx = dir
    y += dy
    x += dx
    if not pos_in_map(map, (y, x)):
        return True
    if map[y][x] == OBSTACLE:
        return False
    return True

def move_guard(map, pos, dir):
    y, x = pos
    map[y] = map[y][:x]+VISITED+map[y][x+1:]
    dy, dx = dir
    y += dy
    x += dx
    return (y, x)

def turn_guard(map, pos, dir):
    new_index = (directions.index(dir) + 1) % len(directions)
    return directions[new_index]

while guard_in_map(map, guard_pos):
    if guard_can_move(map, guard_pos, guard_dir):
        guard_pos = move_guard(map, guard_pos, guard_dir)
    else:
        guard_dir = turn_guard(map, guard_pos, guard_dir)

sum = sum([line.count(VISITED) for line in map])
print(sum)

# Part Two
# with #### marked code is just to imitate the task discription and for debuggung

NEW_OBSTACLE = 'O'

####
CROSSING = '+'
HORIZONTAL = '-'
VERTICAL = '|'
####

new_obstacle_pos = (0, 0)

move_set = dict()
for dir in directions:
    move_set[dir] = set()

def next_new_obstacle_pos(pos):
    y, x = pos
    x += 1
    if x >= len(map[y]):
        y += 1
        x = 0
    return (y, x)

def place_new_obstacle(map, pos):
    y, x = pos
    if map[y][x] in [START, OBSTACLE]:
        pos = next_new_obstacle_pos(pos)
    y, x = pos
    map[y] = map[y][:x]+NEW_OBSTACLE+map[y][x+1:]
    return map, (y, x)

def guard_is_looping(move_set, pos, dir):
    return pos in move_set[dir]

def guard_can_move2(map, pos, dir):
    y, x = pos
    dy, dx = dir
    y += dy
    x += dx
    if pos_in_map(map, (y, x)) and map[y][x] in [OBSTACLE, NEW_OBSTACLE]:
        return False
    return True

def move_guard2(map, move_set, pos, dir):
    y, x = pos
    move_set[dir].add(pos)

    ####
    if map[y][x] is not CROSSING:
        path = HORIZONTAL if dir[0] == 0 else VERTICAL
        if (map[y][x] is HORIZONTAL and path is VERTICAL) or (map[y][x] is VERTICAL and path is HORIZONTAL):
            path = CROSSING
        map[y] = map[y][:x]+path+map[y][x+1:]
    ####

    dy, dx = dir
    return (y+dy, x+dx)

def turn_guard2(map, pos, dir):
    y, x = pos
    new_index = (directions.index(dir) + 1) % len(directions)

    ####
    map[y] = map[y][:x]+CROSSING+map[y][x+1:]
    ####

    return directions[new_index]

sum = 0
while pos_in_map(map, new_obstacle_pos):
    map = data.copy()
    guard_pos, guard_dir = find_starting_pos(map)
    map, new_obstacle_pos = place_new_obstacle(map, new_obstacle_pos)

    while guard_in_map(map, guard_pos) and not guard_is_looping(move_set, guard_pos, guard_dir):
        if guard_can_move2(map, guard_pos, guard_dir):
            guard_pos = move_guard2(map, move_set, guard_pos, guard_dir)
        else:
            guard_dir = turn_guard2(map, guard_pos, guard_dir)

    new_obstacle_pos = next_new_obstacle_pos(new_obstacle_pos)

    for dir in directions:
        move_set[dir] = set()

    if guard_in_map(map, guard_pos):
        sum += 1
print(sum)