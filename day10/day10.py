# https://adventofcode.com/2024/day/10

with open('input.txt') as f:
    data = f.read().splitlines()

# data = [
# '89010123',
# '78121874',
# '87430965',
# '96549874',
# '45678903',
# '32019012',
# '01329801',
# '10456732'
# ]

DIRECTIONS = [(0,1), (1,0), (0,-1), (-1,0)]
START, END, STEP = 0, 9, 1

map = [[int(h) for h in line] for line in data]

# Part One

def pos_in_map(y, x):
    return (y >= 0 and y < len(map)) and (x >= 0 and x < len(map[0]))

def find_trails(y, x):
    if map[y][x] == END:
        return {(y,x)}
    trails_ends = set()
    for dy, dx in DIRECTIONS:
        if pos_in_map(y+dy, x+dx) and map[y+dy][x+dx] == map[y][x] + STEP:
            trails_ends.update(find_trails(y+dy, x+dx))
    return trails_ends

sum = 0
for y, line in enumerate(map):
    for x, height in enumerate(line):
        if height is not START:
            continue
        trails_ends = find_trails(y, x)
        sum += len(trails_ends)
print(sum)

# Part Two

def find_trails2(y, x):
    if map[y][x] == END:
        return 1
    trails_ends = 0
    for dy, dx in DIRECTIONS:
        if pos_in_map(y+dy, x+dx) and map[y+dy][x+dx] == map[y][x] + STEP:
            trails_ends += find_trails2(y+dy, x+dx)
    return trails_ends

sum = 0
for y, line in enumerate(map):
    for x, height in enumerate(line):
        if height is not START:
            continue
        trails_ends = find_trails2(y, x)
        sum += trails_ends
print(sum)