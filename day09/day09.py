# https://adventofcode.com/2024/day/9

with open('input.txt') as f:
    data = f.read().strip()

SPACE = '.'

# Part One

def create_file_blocks(data, id=0, is_data=True):
    blocks = list()
    for digit in data:
        blocks += [id if is_data else SPACE for _ in range(int(digit))]
        id += int(is_data)
        is_data = not is_data
    return blocks

def free_space(blocks, i=0):
    j = len(blocks)-1
    for i in range(i, len(blocks)):
        while blocks[j] == SPACE:
            j -= 1
        if i >= j:
            break

        if blocks[i] == SPACE:
            blocks[i], blocks[j] = blocks[j], blocks[i]
    return blocks
    
def checksum(blocks):
    sum = 0
    for i, id in enumerate(blocks):
        if id == SPACE:
            break
        sum += i * id
    return sum

blocks = create_file_blocks(data)
blocks = free_space(blocks)
sum = checksum(blocks)
print(sum)

# Part Two

def create_file_blocks2(data, id=0, is_data=True):
    blocks = list()
    for digit in data:
        block = (id if is_data else SPACE, int(digit))
        blocks.append(block)
        id += int(is_data)
        is_data = not is_data
    return blocks

def free_space2(blocks, i=0):
    max_id = max([int(id) for id, _ in blocks if id != SPACE])
    for id in range(max_id, 0, -1):
        j = blocks.index([block for block in blocks if block[0] == id][0])
        for i in range(0, j):
            if blocks[i][0] != SPACE:
                continue

            file = blocks[j]
            space = blocks[i]
            if file[1] <= space[1]:
                blocks[j] = (SPACE, blocks[j][1])
                if file[1] == space[1]:
                    blocks[i] = file
                else:
                    blocks[i] = (SPACE, space[1]-file[1])
                    blocks.insert(i, file)
                break
    return blocks

def checksum2(blocks):    
    sum = 0
    index = 0
    for id, length in blocks:
        for _ in range(length):
            if id != SPACE:
                sum += index * id
            index += 1
    return sum

blocks = create_file_blocks2(data)
blocks = free_space2(blocks)
sum = checksum2(blocks)
print(sum)