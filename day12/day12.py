# https://adventofcode.com/2024/day/12

with open('input.txt') as f:
    data = f.read().splitlines()

map = data

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# Part One

def pos_in_map(y, x):
    if y < 0 or y >= len(map):
        return False
    if x < 0 or x >= len(map[0]):
        return False
    return True

def add_fence(y, x, dy, dx):
    if not pos_in_map(y+dy, x+dx):
        return True
    if map[y+dy][x+dx] is not map[y][x]:
        return True
    return False

def neihbor_in_region_and_unvisited(y, x, dy, dx, visited):
    if not pos_in_map(y+dy, x+dx):
        return False
    if (y+dy, x+dx) in visited:
        return False
    if map[y+dy][x+dx] is not map[y][x]:
        return False
    return True

def discover_region(y, x, visited):
    visited.add((y, x))
    fences = 0
    pot_fences = 0
    area = 0
    for dy, dx in DIRECTIONS:
        pot_fences += 1 if add_fence(y, x, dy, dx) else 0

        if not neihbor_in_region_and_unvisited(y, x, dy, dx, visited):
            continue

        area_rec, fences_rec = discover_region(y+dy, x+dx, visited)
        area += area_rec
        fences += fences_rec
    return area+1, fences+pot_fences

visited_set = set()
price = 0
for y, line in enumerate(map):
    for x, pot in enumerate(line):
        if (y, x) in visited_set:
            continue
        area, fences = discover_region(y, x, visited_set)
        price += area*fences
print(price)

# Part Two

def neighbor_has_fence(y, x, dy, dx, ny, nx, visited):    
    if not pos_in_map(y+ny, x+nx):
        return False
    if map[y][x] != map[y+ny][x+nx]:
        return False
    if (y+ny, x+nx) not in visited.keys():
        return False
    if (dy, dx) in visited[(y+ny, x+nx)]:
        return True
    return False

def discover_region_sides(y, x, visited):
    visited[(y, x)] = set()
    fences = 0
    pot_fences = 0
    area = 1
    for dy, dx in DIRECTIONS:
        if add_fence(y, x, dy, dx):
            visited[(y, x)].add((dy, dx))
        neighbor_fences = [neighbor_has_fence(y, x, dy, dx, ny, nx, visited) for ny, nx in DIRECTIONS if abs(ny) != abs(dy)]
        if add_fence(y, x, dy, dx):
            if not any(neighbor_fences):
                pot_fences += 1
            if all(neighbor_fences): # if fence loops, triggers once per region if necessary
                pot_fences -= 1

        if not neihbor_in_region_and_unvisited(y, x, dy, dx, visited):
            continue

        area_rec, fences_rec = discover_region_sides(y+dy, x+dx, visited)
        area += area_rec
        fences += fences_rec
    return area, fences+pot_fences

visited_dict = dict()
price = 0
for y, line in enumerate(map):
    for x, pot in enumerate(line):
        if (y, x) in visited_dict.keys():
            continue
        area, fences = discover_region_sides(y, x, visited_dict)
        price += area*fences
print(price)
