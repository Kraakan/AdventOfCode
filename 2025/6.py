import argparse
import numpy as np
import math

parser = argparse.ArgumentParser(description="Day 6 of Advent of Code 2025")
parser.add_argument(
    "--test",
    action='store_true',
    help="Testing my thinking."
    )
parser.add_argument(
    "--part_1",
    action='store_true',
    help="Part 1 answer."
    )
parser.add_argument(
    "--part_2",
    action='store_true',
    help="Part 2."
    )

args = parser.parse_args()

f = open("input_day6", "r")
inp = f.read()
rows = inp.split('\n')
rows = rows[:-1]

row_length = len(rows[0])
number_table = [''] * row_length
for i, row in enumerate(rows[:-1]):
    for j, c in enumerate(row):
        number_table[j] += c
for i in range(len(number_table)):
    try:
        number_table[i] = int(number_table[i])
    except:
        number_table[i] = None

operation_string = rows[-1]

if args.test:

    print(number_table)
    print(len(operation_string))


if args.part_1:
    
    # https://stackoverflow.com/questions/3845423/remove-empty-strings-from-a-list-of-strings
    # str_list = list(filter(None, str_list))
    grid = list(map(lambda x: x.split(' '), rows))
    grid = list(map(lambda x: list(filter(None, x)), grid))
    for i in range(4):
        grid[i] = list(map(int, grid[i]))
    operations = grid[-1]
    grid = np.array(grid[:-1])
    total_sum = 0
    for i, column in enumerate(grid.T):
        if operations[i] == '+':
            total_sum += sum(column)
        if operations[i] == '*':
            total_sum += math.prod(column)
    print(total_sum)

if args.part_2:
    total_sum = 0
    current_operation = None
    multiple = 1
    for i, row in enumerate(number_table):
        if operation_string[i] == '+':
            if current_operation == '*' and multiple > 1:
                total_sum += multiple
            current_operation = '+'
        if operation_string[i] == '*':
            if current_operation == '+':
                multiple = 1
            current_operation = '*'
        if not current_operation:
            for j in range(i, len(number_table)):
                if number_table[j] == '+' or number_table[j] == '*':
                    break
        if not number_table[i]:
            if current_operation == '*':
                if multiple > 1:
                    total_sum += multiple
                multiple = 1
        if current_operation == '+' and number_table[i]:
            total_sum += number_table[i]
        if current_operation == '*' and number_table[i]:
            multiple *= number_table[i]
        #breakpoint()
    if multiple > 1:
        print(multiple)
        total_sum += multiple
    print(total_sum)