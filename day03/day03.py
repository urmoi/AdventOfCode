# https://adventofcode.com/2024/day/3
import re

with open('input.txt') as f:
    data = f.read()

## Part One

findings = re.findall(r"mul\(\d{1,3},\d{1,3}\)", data)
sum = 0
for find in findings:
    a, b = re.findall(r"\d{1,3}", find)
    sum += int(a) * int(b)
print(sum)

# Part Two

findings = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", data)
sum = 0
disabled = False
for find in findings:
    if find == 'don\'t()':
        disabled = True
    elif find == 'do()':
        disabled = False
    elif not disabled:
        a, b = re.findall(r"\d{1,3}", find)
        sum += int(a) * int(b)
print(sum)