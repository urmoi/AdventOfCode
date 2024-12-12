# https://adventofcode.com/2024/day/11

with open('input.txt') as f:
    data = f.read().strip()

stones = [int(stone) for stone in data.split()]

# Part One

def alter_stones(stones):
    i = 0
    while True:
        stone = stones[i]
        if stone == 0:
            stones[i] = 1
        elif len(str(stone)) % 2 == 0:
            stones.insert(i, int(str(stone)[:len(str(stone))//2]))
            i += 1
            stones[i] = int(str(stone)[len(str(stone))//2:])
        else:
            stones[i] *= 2024
        i += 1
        if i >= len(stones):
            break
    return stones

stones1 = stones.copy()
for _ in range(25):
    stones1 = alter_stones(stones1)
print(len(stones1))
        
# Part Two

stone_dict = dict()

def alter_stones_rec(stone, n):
    if (stone, n) in stone_dict:
        return stone_dict[(stone, n)]

    if n == 0:
        stone_dict[(stone, n)] = 1
    elif stone == 0:
        stone_dict[(stone, n)] = alter_stones_rec(1, n-1)
    elif len(str(stone)) % 2 == 0:
        str_stone = str(stone)
        stone_l, stone_r = int(str_stone[:len(str_stone)//2]), int(str_stone[len(str_stone)//2:])
        stone_dict[(stone, n)] = alter_stones_rec(stone_l, n-1) + alter_stones_rec(stone_r, n-1)
    else:
        stone_dict[(stone, n)] = alter_stones_rec(stone*2024, n-1)

    return stone_dict[(stone, n)]
    
res = sum(alter_stones_rec(stone, 75) for stone in stones)
print(res)


