# https://adventofcode.com/2024/day/7

with open('input.txt') as f:
    data = f.read().splitlines()


# data = [
#     '190: 10 19',
#     '3267: 81 40 27',
#     '83: 17 5',
#     '156: 15 6',
#     '7290: 6 8 6 15',
#     '161011: 16 10 13',
#     '192: 17 8 14',
#     '21037: 9 7 18 13',
#     '292: 11 6 16 20'
# ]

equations = []
for equation in data:
    test, numbers = equation.split(':')
    test = int(test)
    numbers = [int(number) for number in numbers.split()]
    equations.append((test, numbers))

# Part One

OPERATORS = {0: 'sum', 1: 'mul'}

def equation_is_correct(test, numbers, op_seq):
    value = numbers[0]
    for op, number in zip(op_seq, numbers[1:]):
        if op == '0':
            value += number
        elif op == '1':
            value *= number

        if value > test:
            return False
    return value == test

def operation_check(test, numbers):
    n_bit = (len(numbers)-1)
    f_bit = f'0{n_bit}b'
    n = len(OPERATORS) ** n_bit

    for op_n in range(n): # loop over every operation combination
        op_seq = f'{op_n:{f_bit}}' # generate bit from number
        if equation_is_correct(test, numbers, op_seq):
            return True
    return False

sum = 0
for test, numbers in equations:
    if operation_check(test, numbers):
        sum += test
print(sum)

# Part Two

def equation_is_correct2(test, numbers, op_seq):
    value = numbers[0]
    for op, number in zip(op_seq, numbers[1:]):
        if op == '0':
            value += number
        elif op == '1':
            value *= number
        elif op == '2':
            value = int(f'{value}{number}')

        if value > test:
            return False
    return value == test

def operation_check2(test, numbers):
    n_bit = (len(numbers)-1)
    f_bit = f'0{n_bit}b'
    n = len(OPERATORS) ** n_bit

    for cat in range(n): # loop over every cat combunation (first loop is without cat)
        for op_n in range(n): # loop over every operation combination
            op_seq = f'{op_n:{f_bit}}' # generate bit from number
            op_cat = f'{cat:{f_bit}}' # 1 is position of cat_op

            for i, c in enumerate(op_cat):
                if c == '1':
                    op_seq = op_seq[:i]+'2'+op_seq[i+1:]

            if equation_is_correct2(test, numbers, op_seq):
                return True
    return False

sum = 0
for test, numbers in equations:
    if operation_check2(test, numbers):
        sum += test
print(sum)