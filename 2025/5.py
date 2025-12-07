import argparse

parser = argparse.ArgumentParser(description="As the \
                                 forklifts break through the wall, the Elves are \
                                 delighted to discover that there was a cafeteria on \
                                 the other side after all.You can hear a commotion \
                                 coming from the kitchen. \"At this rate, we won't have \
                                 any time left to put the wreaths up in the dining hall!\" \
                                 Resolute in your quest, you investigate.\"If only we \
                                 hadn't switched to the new inventory management system \
                                 right before Christmas!\" another Elf exclaims. You ask \
                                 what's going on.The Elves in the kitchen explain the \
                                 situation: because of their complicated new inventory \
                                 management system, they can't figure out which of their \
                                 ingredients are fresh and which are spoiled. When you \
                                 ask how it works, they give you a copy of their \
                                 database (your puzzle input).The database operates on \
                                 ingredient IDs. It consists of a list of fresh \
                                 ingredient ID ranges, a blank line, and a list of \
                                 available ingredient IDs. ")
parser.add_argument(
    "--test",
    action='store_true',
    help="Testing my thinking."
    )
parser.add_argument(
    "--part_1",
    action='store_true',
    help="Check if ids (second part of the input) are within any of the ranges provided (in the first part of the input)."
    )
parser.add_argument(
    "--part_2",
    action='store_true',
    help="Count all ids that are within any of the ranges provided (in the first part of the input)."
    )
parser.add_argument(
    "--slow",
    action='store_true',
    help="Slow solution for part 2."
    )

args = parser.parse_args()

f = open("input_day5", "r")
inp = f.read().rstrip()

ranges, ids = inp.split('\n\n')
ranges = ranges.split('\n')
ids = ids.split('\n')

ids = list(map(int, ids))
ranges = list(map(lambda x: tuple(map(int, x.split('-'))), ranges))

if args.test:
    test_input =[(3,5),
    (10,14),
    (16,20),
    (12,18)]
    print(type(ranges[0]), type(ranges[0][1]))
    redundant_range_ids = []
    combined_range_ids = []
    new_range_list = []
    preserved_range_list = []
    import copy
    input_list = copy.deepcopy(ranges)
    for i, fresh_range in enumerate(input_list):
        if i not in redundant_range_ids and i not in combined_range_ids:
            preserved = True
            for j, second_fresh_range in enumerate(input_list):
                if j not in preserved_range_list and j not in redundant_range_ids \
                and j not in combined_range_ids and i != j:
                    if fresh_range[0] == second_fresh_range[0]:
                        if fresh_range[1] >= second_fresh_range[1]: # range1 contains range2 (range2 redundant)
                            redundant_range_ids.append(j)
                            new_range_list.append(fresh_range)
                            preserved = False
                            break
                    elif fresh_range[0] < second_fresh_range[0]:
                        if fresh_range[1] >= second_fresh_range[1]: # range1 contains range2 (range2 redundant)
                            redundant_range_ids.append(j)
                            new_range_list.append(fresh_range)
                            preserved = False
                            break
                        if fresh_range[1] >= second_fresh_range[0]: # ranges overlap (range1[bottom] - range2[top])
                            combined_range_ids = combined_range_ids + [i,j]
                            new_range_list.append((fresh_range[0], second_fresh_range[1]))
                            preserved = False
                            break
                    else: #fresh_range[0] > second_fresh_range[0]
                        if fresh_range[1] <= second_fresh_range[1]: # range2 contains range1 (range1 redundant)
                            redundant_range_ids.append(i)
                            new_range_list.append(second_fresh_range)
                            preserved = False
                            break
                        elif fresh_range[1] <= second_fresh_range[1]:# ranges overlap (range2[bottom] - range1[top])
                            combined_range_ids = combined_range_ids + [i,j]
                            new_range_list.append((second_fresh_range[0], fresh_range[1]))
                            preserved = False
                            break
            if preserved:
                new_range_list.append(fresh_range)
                preserved_range_list.append(i)
    print(len(new_range_list), len(preserved_range_list))

if args.part_1:
    fresh_count = 0
    for id in ids:
        for fresh_range in ranges:
            lower = fresh_range[0]
            upper = fresh_range[1]
            if id in range(lower, upper):
                fresh_count = fresh_count + 1
                print(fresh_count, end='\r')
                break
    print()

if args.slow:
    print("Calculating lower and upper bound for ids to be checked.")
    lower_bound = 999999999999999
    upper_bound = 0
    for fresh_range in ranges:
        lower = fresh_range[0]
        upper = fresh_range[1]
        if lower < lower_bound:
            lower_bound = lower
        if upper > upper_bound:
            upper_bound = upper
            print("Lower bound:", lower_bound, "Upper bound:", upper_bound, end='\r')
    print('\nCounting all ids between', lower_bound, str(upper_bound) + ':')
    fresh_count = 0
    for id in range(lower_bound, upper_bound):
        for fresh_range in ranges:
            lower = int(fresh_range[0])
            upper = int(fresh_range[1])
            if id in range(lower, upper):
                fresh_count = fresh_count + 1
                print('\r', fresh_count, end='')
                break
    print()

def combine_ranges(input_list: list) -> tuple:
    return_list = []
    used_j = []
    for i, fresh_range in enumerate(input_list):
        used_i = False
        if i not in used_j:
            preserved = True
            combined = False
            for j in range(i+1, len(input_list)):
                if j not in used_j:
                    if fresh_range[1] >= input_list[j][0]:
                        if fresh_range[0] <= input_list[j][1]:
                            combined = True
                    if input_list[j][1] >= fresh_range[0]:
                        if input_list[j][0] <= fresh_range[1]:
                            combined = True
                    if (fresh_range[0] >= input_list[j][0] and fresh_range[1] <= input_list[j][1]) or \
                    (input_list[j][0] >= fresh_range[0] and input_list[j][1] <= fresh_range[1]):
                        combined = True
                    if combined:
                        new_range = (min(fresh_range[0], input_list[j][0]), max(fresh_range[1], input_list[j][1]))
                        return_list.append(new_range)
                        used_j.append(j)
                        preserved = False
                        used_i = True
                        break
                if used_i:
                    break
            #breakpoint()
            if preserved:
                return_list.append(fresh_range)
    return (return_list, len(input_list))

if args.part_2:
    print("Combining overlapping ranges.")
    input_ranges = ranges
    prev_length = len(input_ranges) + 1
    iterations = 0
    while prev_length > len(input_ranges):
        iterations += 1
        input_ranges, prev_length = combine_ranges(input_ranges)
        num_ranges = len(input_ranges)
        print('\r', iterations, "iterations made.", num_ranges, "ranges remain.", end='')
    print()
    print("If the list is fully optimized now, the answer is the (inclusive) sum of all the ranges.")
    range_sum = 0
    for i, r in enumerate(input_ranges):
        range_sum = range_sum + r[1] - r[0] + 1
        #print('\r', str((i/num_ranges)*100)[:4], "% counted. Sum:", range_sum, end='')
    print('\n', "Sum =", range_sum)