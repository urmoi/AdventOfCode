# https://adventofcode.com/2024/day/15

with open('input.txt') as f:
    data = f.read()

warehouse, instructions = data.split('\n\n')

warehouse = [line for line in warehouse.splitlines()]
instructions = ''.join(instructions.split('\n'))

ROBOT = '@'
BOX = 'O'
WALL = '#'
SPACE = '.'

DIRECTIONS = {
    '^': (-1, 0),
    '>': (0, 1),
    'v': (1, 0),
    '<': (0, -1)
}

def collect_pos_in_warehouse(item, warehouse):
    return [(y, x) for y, _ in enumerate(warehouse) for x, _ in enumerate(warehouse[y]) if warehouse[y][x] is item]

def next(pos, dir):
    dy, dx = DIRECTIONS[dir]
    y, x = pos
    return (y+dy, x+dx)

def prev(pos, dir):
    dy, dx = DIRECTIONS[dir]
    y, x = pos
    return (y-dy, x-dx)

# Part One

rpos = collect_pos_in_warehouse(ROBOT, warehouse)[0]
bpos = collect_pos_in_warehouse(BOX, warehouse)
wpos = collect_pos_in_warehouse(WALL, warehouse)

def move_box(pos, dir, bpos, wpos):
    if next(pos, dir) in wpos:
        return prev(pos, dir)

    if next(pos, dir) not in bpos:
        bpos[bpos.index(pos)] = next(pos, dir)
        return pos
    
    npos = move_box(next(pos, dir), dir, bpos, wpos)
    bpos[bpos.index(pos)] = npos
    return prev(npos, dir)

def move_robot(instructions, rpos, bpos, wpos):
    for dir in instructions:
        if next(rpos, dir) in wpos:
            pass
        elif next(rpos, dir) not in bpos:
            rpos = next(rpos, dir)
        else:
            rpos = move_box(next(rpos, dir), dir, bpos, wpos)

def calc_gps(bpos, step=1):
    return sum(x + 100*y for y, x in bpos[::step])

move_robot(instructions, rpos, bpos, wpos)
print(calc_gps(bpos))

# Part Two

def widen(pos):
    ret = []
    for y, x in pos:
        ret.append((y, 2*x))
        ret.append((y, 2*x+1))
    return ret

rpos = widen(collect_pos_in_warehouse(ROBOT, warehouse))[0]
bpos = widen(collect_pos_in_warehouse(BOX, warehouse))
wpos = widen(collect_pos_in_warehouse(WALL, warehouse))

def define_box(pos, bpos):
    index = bpos.index(pos)
    side = index % 2
    return bpos[index-side], bpos[index-side+1]

def find_boxes_to_move(pos, dir, bpos, wpos):
    lpos, rpos = define_box(pos, bpos)
    if next(lpos, dir) in wpos or next(rpos, dir) in wpos: # wall infront
        return {}
    box_ids = {bpos.index(lpos), bpos.index(rpos)}
    if DIRECTIONS[dir][0] == 0:
        check_next = [next(next(pos, dir), dir)]
    else:
        check_next = [next(lpos, dir), next(rpos, dir)]
    for next_box in check_next:
        if next_box in bpos:
            next_ids = find_boxes_to_move(next_box, dir, bpos, wpos)
            if not next_ids:
                return {}
            box_ids = box_ids.union(next_ids)
    return box_ids

def move_boxes(box_ids, dir, bpos):
    for id in box_ids:
        bpos[id] = next(bpos[id], dir)

def sim_robot2(instructions, rpos, bpos, wpos):
    for dir in instructions:
        if next(rpos, dir) in wpos:
            pass
        elif next(rpos, dir) not in bpos:
            rpos = next(rpos, dir)
        elif box_ids := find_boxes_to_move(next(rpos, dir), dir, bpos, wpos):
            move_boxes(box_ids, dir, bpos)
            rpos = next(rpos, dir)

sim_robot2(instructions, rpos, bpos, wpos)
print(calc_gps(bpos, 2))