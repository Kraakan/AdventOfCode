import argparse

parser = argparse.ArgumentParser(description="Day 2 of Advent of Code 2025")
parser.add_argument(
    "--test",
    action='store_true',
    help="Testing my thinking."
    )
parser.add_argument(
    "--part_1",
    action='store_true',
    help="Make the biggest number by picking two numbers."
    )
parser.add_argument(
    "--part_2",
    action='store_true',
    help="Make the biggest number by picking twelve numbers."
    )

args = parser.parse_args()

f = open("input_day3", "r")
inp = f.read().rstrip()
inp = inp.split('\n')

def make_biggest_number(number_string: str, digits=2) -> int:
    new_number_string = ''
    selected_digit_index = -1
    for i in range(digits):
        candidate_digit = 0
        candidate_digit_index = 0
        for j in range(selected_digit_index + 1, len(number_string) - digits + i + 1):
            this_digit = int(number_string[j])
            if this_digit > candidate_digit:
                #breakpoint()
                candidate_digit = this_digit
                candidate_digit_index = j
        selected_digit_index = candidate_digit_index
        new_number_string = new_number_string + str(candidate_digit)
    return int(new_number_string)

if args.test:
    for n in inp:
        print(n, make_biggest_number(n))

if args.part_1:
    max_joltage = 0
    for n in inp:
        max_joltage = max_joltage + make_biggest_number(n)
    print(max_joltage)

if args.part_2:
    max_joltage = 0
    for n in inp:
        max_joltage = max_joltage + make_biggest_number(n, digits=12)
    print(max_joltage)