# https://adventofcode.com/2024/day/13

with open('input.txt') as f:
    data = f.read()

TOKENS_A = 3
TOKENS_B = 1
LIMIT = 100

def create_machine_vals(info, error):

    def find_vals(line):
        return [int(n[2:]) for n in line.split(':')[1].strip().split(', ') if n[0] in ['X', 'Y']]
    
    info = info.splitlines()
    ax, ay = find_vals(info[0])
    bx, by = find_vals(info[1])
    px, py = find_vals(info[2])
    return { 'A': (ay, ax), 'B': (by, bx), 'P': (py+error, px+error) }

# Part One

def solve_rec(machine, pos, options, limitA, limitB, tokens):
    ay, ax = machine['A']
    by, bx = machine['B']
    py, px = machine['P']
    y, x = pos

    if y == py and x == px:
        return tokens
    if any(limit >= LIMIT for limit in [limitA, limitB]):
        return 0
    if y > py or x > px:
        return 0
    
    buttons = list()
    if 'A' in options:
        buttons.append(solve_rec(machine, (y+ay, x+ax), options, limitA+1, limitB, TOKENS_A))
    buttons.append(solve_rec(machine, (y+by, x+bx), ['B'], limitA, limitB+1, TOKENS_B))
        
    if any(buttons):
        return tokens + min([token for token in buttons if token])
    return 0

machines = [create_machine_vals(machine_info, 0) for machine_info in data.split('\n\n')]

tokens = 0
for machine in machines:
    tokens += solve_rec(machine, (0, 0), ['A', 'B'], 0, 0, 0)
print(tokens)

# Part Two

# ca * ax + cb * bx = px
# ca * ay + cb * by = py

# ca * ax * by + cb * bx * by = px * by
# ca * ay * bx + cb * by * bx = py * bx

# ca * ax * by - ca * ay * bx = px * by - py * bx
# ca * (ax * by - ay * bx) = px * by - py * bx
# ca = (px * by - py * bx) / (ax * by - ay * bx)

# cb = (py - ca * ay) / by

def solve(machine):
    ay, ax = machine['A']
    by, bx = machine['B']
    py, px = machine['P']

    ca = (px * by - py * bx) / (ax * by - ay * bx)
    cb = (py - ca * ay) / by

    if ca.is_integer() and cb.is_integer():
        return int(ca) * TOKENS_A + int(cb) * TOKENS_B
    return 0

        
error = 10000000000000

machines = [create_machine_vals(machine_info, error) for machine_info in data.split('\n\n')]

tokens = 0
for machine in machines:
    tokens += solve(machine)
print(tokens)