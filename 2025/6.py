import argparse

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
inp = f.read().rstrip()
rows = inp.split('\n')

# https://stackoverflow.com/questions/3845423/remove-empty-strings-from-a-list-of-strings
# str_list = list(filter(None, str_list))
grid = list(map(lambda x: x.split(' '), rows))

if args.test:
    for i, row in enumerate(grid):
        print("Row", str(i) + ':', row)