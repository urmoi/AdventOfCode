# https://adventofcode.com/2024/day/4

with open('input.txt') as f:
    data = f.read().splitlines()

DIRECTION = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

# Part One

XMAS = 'XMAS'

def check_xmas(y, x, w, d):
    if (y < 0 or y >= len(data)) or (x < 0 or x >= len(data[0])):
        return 0
    
    letter = data[y][x]
    if letter != XMAS[w]:
        return 0
    
    if w == len(XMAS)-1:
        return 1
    
    (dy, dx) = DIRECTION[d]
    return check_xmas(y+dy, x+dx, w+1, d)

sum = 0
for y, line in enumerate(data):
    for x, letter in enumerate(line):
        if letter == XMAS[0]:
            for d, (dy, dx) in enumerate(DIRECTION):
                sum += check_xmas(y+dy, x+dx, 1, d)
print(sum)

# Part Two

MAS = 'MAS'

def check_x_mas(y, x):
    dia = {
         1: '', # \ dy*dx = (-1*-1) or (1*1) = 1
        -1: ''  # / dy*dx = (-1*1) or (1*-1) = -1
    }
    for (dy, dx) in DIRECTION:
        i = dy*dx
        if i == 0: # not diagonal
            continue
        letter = data[y+dy][x+dx]
        if letter not in [MAS[0], MAS[-1]]:
            return 0
        if not dia[i]:
            dia[i] = letter
        else:
            if dia[i] == MAS[0] and letter != MAS[-1]:
                return 0
            elif dia[i] == MAS[-1] and letter != MAS[0]:
                return 0
    return 1

sum = 0
for y, line in enumerate(data):
    if y == 0 or y == len(data)-1:
        continue
    for x, letter in enumerate(line):
        if x == 0 or x == len(line)-1:
            continue
        if letter == MAS[1]:
            sum += check_x_mas(y, x)
print(sum)                