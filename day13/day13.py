# https://adventofcode.com/2024/day/13

# with open('input.txt') as f:
#     data = f.read()

with open('test.txt') as f:
    data = f.read()

TOKENS_A = 3
TOKENS_B = 1
LIMIT = 100

def create_machine_vals(info):

    def find_vals(line):
        return [int(n[2:]) for n in line.split(':')[1].strip().split(', ') if n[0] in ['X', 'Y']]
    
    info = info.splitlines()
    ax, ay = find_vals(info[0])
    bx, by = find_vals(info[1])
    px, py = find_vals(info[2])
    return { 'A': (ay, ax), 'B': (by, bx), 'P': (py, px) }

# Part One

def solve_rec(machine, pos, options, limitA, limitB, tokens):
    if pos[0] == machine['P'][0] and pos[1] == machine['P'][1]:
        return tokens
    if any(limit >= LIMIT for limit in [limitA, limitB]):
        return 0
    if pos[0] > machine['P'][0] or pos[1] > machine['P'][1]:
        return 0
    
    buttons = list()
    for b in options:
        p = (pos[0]+machine[b][0], pos[1]+machine[b][1])
        o = options if b == 'A' else ['B']
        t = TOKENS_A if b == 'A' else TOKENS_B
        lA = limitA + 1 if b == 'A' else 0
        lB = limitB +  1 if b == 'B' else 0
        buttons.append(solve_rec(machine, p, o, lA, lB, t))
        
    if any(buttons):
        tokens += min([token for token in buttons if token])
    else:
        tokens = 0
    return tokens

machines = [create_machine_vals(machine_info, 0) for machine_info in data.split('\n\n')]

tokens_spend = 0
for machine in machines:
    tokens = solve_rec(machine, (0, 0), ['A', 'B'], 0, 0, 0)
    tokens_spend += tokens
print(tokens_spend)

# Part Two
