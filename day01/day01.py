# https://adventofcode.com/2024/day/1

listA = list()
listB = list()

with open('input.txt') as f:
    data = f.read().splitlines()

for line in data:
    a, b = line.split()
    listA.append(int(a))
    listB.append(int(b))

listA.sort()
listB.sort()

# Part One

distance = 0

for a, b in zip(listA, listB):
    distance += abs(a - b)

print(distance)

# Part Two

similarity = 0

for a in listA:
    similarity += a * sum(1 for b in listB if a == b)

print(similarity)