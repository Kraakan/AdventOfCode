
f = open("input_day1", "r")

inp = f.read()
operations = inp.split('\n')
operations = list(filter(None, operations))

print(len(operations))

def rotate(start: int, directon: str, clicks: int) -> tuple:
    if directon == 'L':
        rotation_factor = -1
    elif directon == 'R':
        rotation_factor = 1
    else: return False
    zero_points = 0
    new_position = start + clicks * rotation_factor
    if new_position < 0:
        zero_points =  new_position // -100 # How many times the dial pointed at zero
        if start != 0:
            zero_points = zero_points + 1
        new_position = (new_position % -100 + 100) % 100
    elif new_position > 99:
        zero_points =  new_position // 100
        new_position = new_position % 100
    elif new_position == 0:
        zero_points = 1
    return new_position, zero_points

position = 50
zero_count = 0

for op in operations:
    direction = op[0]
    clicks = int(op[1:])
    position, zeroes = rotate(position, direction, clicks)
    zero_count = zero_count + zeroes
    print(zero_count, direction, clicks, position)

print(zero_count)