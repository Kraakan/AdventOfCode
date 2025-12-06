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
    help="Count how many @ symbols are surrounded by less than 4 others."
    )
parser.add_argument(
    "--part_2",
    action='store_true',
    help=""
    )

args = parser.parse_args()

f = open("input_day4", "r")
inp = f.read().rstrip()
grid_map = inp.split('\n')

def make_next_map(grid: list) -> list:
    grid_height = len(grid_map)
    line_length = len(grid_map[0])
    new_grid = []
    removed_rolls = 0
    for i, line in enumerate(grid):
        new_line = ''
        for j, char in enumerate(line):
            if char == '@':
                search_string = ''
                search_top = i - 1
                if search_top < 0:
                    search_top = 0
                search_bottom = i + 1
                if search_bottom >= grid_height:
                    search_bottom = i
                search_left = j - 1
                if search_left < 0:
                    search_left = 0
                search_right = j + 1
                if search_right >= line_length:
                    search_right = j
                for y in range(search_top, search_bottom + 1):
                    search_string = search_string + grid[y][search_left:search_right + 1]
                if search_string.count('@') < 5: # I'm going to count the central roll as well, because it's easier that way
                    new_line = new_line + 'X'
                    removed_rolls = removed_rolls + 1
                else:
                    new_line = new_line + '@'
            else:
                new_line = new_line + '.'
        new_grid.append(new_line)
    return new_grid, removed_rolls

if args.test:
    grid_height = len(grid_map)
    line_length = len(grid_map[0])
    for line_i in range(grid_height):
        for char_i in range(line_length):
            if grid_map[line_i][char_i] == '@':
                rolls = 0
                search_y = line_i - 1
                search_x = char_i - 1
                while rolls < 5: # I'm going to count the central roll as well, because it's easier that way
                    if search_y < 0:
                        search_y = 0
                    if search_x >= line_length or search_x > char_i + 1:
                        search_x = char_i - 1
                        search_y = search_y + 1
                    if search_x < 0:
                        search_x = 0
                    if search_y >= grid_height or search_y > line_i + 1:
                        break
                    if grid_map[search_y][search_x] == '@':
                        rolls = rolls + 1
                    search_x = search_x + 1
                if rolls > 4:
                    print('@', end='')
                else:
                    print('X', end='')
            else:
                print('.', end='')
        print('')

if args.part_1:
    grid_height = len(grid_map)
    line_length = len(grid_map[0])
    accessible_rolls = 0
    for line_i in range(grid_height):
        for char_i in range(line_length):
            if grid_map[line_i][char_i] == '@':
                search_string = ''
                search_top = line_i - 1
                if search_top < 0:
                    search_top = 0
                search_bottom = line_i + 1
                if search_bottom >= grid_height:
                    search_bottom = line_i
                search_left = char_i - 1
                if search_left < 0:
                    search_left = 0
                search_right = char_i + 1
                if search_right >= line_length:
                    search_right = char_i
                for y in range(search_top, search_bottom + 1):
                    search_string = search_string + grid_map[y][search_left:search_right + 1]
                if search_string.count('@') < 5: # I'm going to count the central roll as well, because it's easier that way
                    accessible_rolls = accessible_rolls + 1
    print(accessible_rolls)

if args.part_2:
    import curses
    grid_height = len(grid_map)
    removed_each_round = []
    removed_this_round = 9999
    import copy
    current_map = copy.deepcopy(grid_map)
    grid_maps = [current_map]
    while removed_this_round > 0:
        current_map, removed_this_round = make_next_map(current_map)
        removed_each_round.append(removed_this_round)
        grid_maps.append(current_map)

    def draw_grid_with_curses(stdscr, grid, info):
        stdscr.clear()
        rows, cols = stdscr.getmaxyx()
        line_length = len(grid_map[0])
        if line_length > cols:
            line_length = cols
        yy = 0
        xx = line_length + 1
        for key in info:
            stdscr.move(yy, xx)
            for char in key:
                stdscr.move(yy, xx)
                stdscr.addstr(char)
                if xx < cols-1:
                    xx = xx + 1
                else:
                    xx = line_length + 1
                    yy = yy + 1
            yy = yy + 1
            xx = line_length + 1
            stdscr.move(yy, xx)
            for char in info[key]:
                stdscr.move(yy, xx)
                stdscr.addstr(char)
                if xx < cols-1:
                    xx = xx + 1
                else:
                    xx = line_length + 1
                    yy = yy + 1
            yy = yy + 1
            xx = line_length + 1
        

        stdscr.move(0, 0)
        for i, row in enumerate(grid):
            if i < rows-1:
                stdscr.move(i,0)
                stdscr.addstr(row[:cols - 1])

    def start(stdscr):
            top_of_drawn_map = 0
            rows, cols = stdscr.getmaxyx()
            day = 0
            removed = 0
            
            while True:
                info = {'round:': str(day),
                        'removed:': str(removed_each_round[day]),
                        'total:': str(str(sum(removed_each_round)))}
                map_on_screen = grid_maps[day][top_of_drawn_map:]
                draw_grid_with_curses(stdscr, map_on_screen, info)
                key = stdscr.getch()
                go = True
                n = None
                if key == 27: # Esc or Alt
                    # Don't wait for another key
                    # If it was Alt then curses has already sent the other key
                    # otherwise -1 is sent (Escape)
                    stdscr.nodelay(True)
                    n = stdscr.getch()
                    if n == -1 or key == ord('q'):
                        # Escape was pressed
                        go = False
                    # Return to delay
                    stdscr.nodelay(False)
                if not go:
                    break
                if key == ord('w') or key == curses.KEY_UP:
                    if top_of_drawn_map > 0:
                        top_of_drawn_map = top_of_drawn_map - 1
                if key == ord('s') or key == curses.KEY_DOWN:
                    if top_of_drawn_map < (grid_height - rows + 1):
                        top_of_drawn_map = top_of_drawn_map + 1
                if key == ord('a') or key == curses.KEY_LEFT:
                    if day > 0:
                        day = day - 1
                if key == ord('d') or key == curses.KEY_RIGHT:
                    if day < len(grid_maps) - 2:
                        day = day + 1

    curses.wrapper(start)