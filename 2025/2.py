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
    help="Add together all the numbers in the input ranges that are a sequence of digits repeated twice."
    )
parser.add_argument(
    "--part_2",
    action='store_true',
    help="Add together all the numbers in the input ranges that are any repeating sequence if digits."
    )

args = parser.parse_args()

f = open("input_day2", "r")
inp = f.read().rstrip()
inp = inp.split(',')
for i in range(len(inp)):
    inp[i] = tuple(map(int, inp[i].split('-')))

def number_is_repeated_twice(number: int) -> bool:
    number_string = str(number)
    if len(number_string) % 2 != 0:
        return False
    half_length = len(number_string) // 2
    if number_string[:half_length] == number_string[half_length:]:
        return True
    return False

def number_is_repeated(number: int, prime_list: list) -> bool:
    number_string = str(number)
    number_length = len(number_string)
    repetitions_to_test = []
    for prime in prime_list:
        if prime > number_length:
            break
        if number_length % prime == 0:
            repetitions_to_test.append(prime)
    for repetition in repetitions_to_test:
        sliced_number_string = str(number)
        segment_length = number_length//repetition
        first_segment = sliced_number_string[:segment_length]
        equal = True
        while len(sliced_number_string) > 0 and equal:
            if sliced_number_string[:segment_length] == first_segment: # This will trigger redundantly the first time, but I think itäs worth it.
                sliced_number_string = sliced_number_string[segment_length:]
            else:
                equal = False
                break
        if equal:
            return True
    return False

if args.test:
    for n in inp:
        print(n, number_is_repeated_twice(n[0]), number_is_repeated_twice(n[1]))

if args.part_1:
    sum_of_invalid_ids = 0
    for r in inp:
        for n in range(r[0], r[1]+1):
            if number_is_repeated_twice(n):
                sum_of_invalid_ids = sum_of_invalid_ids + n
    print(sum_of_invalid_ids)

if args.part_2:
    primes_string = open("primes.txt", "r").read()
    prime_list = list(map(int, primes_string.split()))
    sum_of_invalid_ids = 0
    for r in inp:
        for n in range(r[0], r[1]+1):
            if number_is_repeated(n, prime_list):
                sum_of_invalid_ids = sum_of_invalid_ids + n
    print(sum_of_invalid_ids)