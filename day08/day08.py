# https://adventofcode.com/2024/day/8

with open('input.txt') as f:
    data = f.read().splitlines()


antennas = dict()
for y, line in enumerate(data):
    for x, point in enumerate(line):
        if point.isdigit() or point.isalpha():
            if point not in antennas:
                antennas[point] = set()
            antennas[point].add((y, x))

def calc_anti_pos(pos_y, pos_x, nei_y, nei_x):
    # new = pos - dif = pos - (nei - pos) = pos + pos - nei = 2 * pos - nei
    y = 2 * pos_y - nei_y
    x = 2 * pos_x - nei_x
    return (y, x)

def pos_in_map(y, x):
    return (y >= 0 and y < len(data)) and (x >= 0 and x < len(data[0]))

# Part One

antinodes = set()

for antenna, positions in antennas.items():
    for pos in positions:
        for nei in positions.difference({pos}):
            anti_pos = calc_anti_pos(*pos, *nei)
            if pos_in_map(*anti_pos):
                antinodes.add(anti_pos)

for antenna, positions in antennas.items():
    antinodes = antinodes.difference(positions)

sum = len(antinodes)
print(sum)

# Part Two

antinodes = set()

for antenna, positions in antennas.items():
    for pos in positions:
        for nei in positions.difference({pos}):
            a, b = pos, nei
            while pos_in_map(*a):
                antinodes.add(a)
                anti_pos = calc_anti_pos(*a, *b)
                a, b = anti_pos, a

sum = len(antinodes)
print(sum)