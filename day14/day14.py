# https://adventofcode.com/2024/day/13

import re

with open('input.txt') as f:
    data = f.read().splitlines()

SPACE = (101, 103)
TIME = 100

robots = [tuple(map(int, re.findall(r"-?\d+", robot))) for robot in data]

def print_positions(positions):
    for y in range(SPACE[1]):
        _ = ''
        for x in range(SPACE[0]):
            count = positions.count((x, y))
            _ += f'{count}' if count else '.'
        print(_)

# Part One

def calc_positions(time):
    positions = list()
    for robot in robots:
        rx, ry, vx, vy = robot
        px = (rx + vx * time) % SPACE[0]
        py = (ry + vy * time) % SPACE[1]
        positions.append((px, py))
    return positions

def calc_safety_factor(positions):
    factor = 1
    for i in range(4):
        l, r = (0, SPACE[0]//2-1) if i<2 else (SPACE[0]//2+1, SPACE[0]-1)
        u, d = (0, SPACE[1]//2-1) if i%2 else (SPACE[1]//2+1, SPACE[1]-1)
        quadrant = [(px, py) for px, py in positions if l <= px <= r and u <= py <= d]
        factor *= len(quadrant)
    return factor

positions = calc_positions(TIME)
factor = calc_safety_factor(positions)
print(factor)

# Part Two

time = 0
while True:
    positions = calc_positions(time)
    if len(set(positions)) == len(positions):
        break
    time += 1
print(time)