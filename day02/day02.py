# https://adventofcode.com/2024/day/2

with open('input.txt') as f:
    data = f.read().splitlines()
    data = [[int(num) for num in line.split(' ')] for line in data]

def is_report_safe(report):
    d = 0
    for i in range(len(report)-1):
        distance = report[i+1]-report[i]

        same_dir = d*distance >= 0 # The levels are either all increasing or all decreasing.
        ok_step = abs(distance) in [1,2,3] # Any two adjacent levels differ by at least one and at most three

        if not (same_dir and ok_step):
            return False
        d = distance
        if i == len(report)-2:
            return True

# Part One

counter = 0
for report in data:
    counter += 1 if is_report_safe(report) else 0
print(counter)

# Part Two

counter = 0
for report in data:
    if  is_safe := is_report_safe(report):
        counter += 1
    else:
        for i in range(len(report)):
            if is_report_safe(report[:i]+report[i+1:]):
                counter += 1
                break
print(counter)


