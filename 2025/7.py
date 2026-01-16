import argparse
import curses

parser = argparse.ArgumentParser(description="Day 7 of Advent of Code 2025")
parser.add_argument(
    "--test",
    action='store_true',
    help="Testing my thinking."
    )
parser.add_argument(
    "--part_1",
    action='store_true',
    help=""
    )
parser.add_argument(
    "--part_2",
    action='store_true',
    help=""
    )

args = parser.parse_args()

f = open("input_day7", "r")
inp = f.read().rstrip()
grid_map = inp.split('\n')

def draw_grid_with_curses(stdscr, grid: list, start_y: int, laser_progress: int, grid2=None, answer=''):
    stdscr.clear()
    rows, cols = stdscr.getmaxyx()
    yy, xx = 0, 0
    for i, row in enumerate(grid[start_y:rows+start_y]):
        stdscr.move(i, 0)
        if i + start_y <= laser_progress and grid2 != None:
            row = grid2[i + start_y]
        for c in row[0:0+cols-1]:
            if c == 'S':
                stdscr.addstr(c, curses.color_pair(1))
            elif c == '^':
                stdscr.addstr(c, curses.color_pair(2))
            elif c == '|':
                stdscr.addstr(c, curses.color_pair(3))
            else:
                stdscr.addstr(c)
    stdscr.move(0, 0)
    stdscr.addstr(answer)

def show_solution(stdscr, grid_map, lazered_grid, answer=''):
    rows, cols = stdscr.getmaxyx()
    yy = 0
    xx = len(grid_map[0]) //2 - cols//2
    max_y = len(grid_map) - rows
    max_x = len(grid_map) # - cols  # Since the entire image fits in my terminal window, I'm going to use the left and right keys to progress the solution instead
    while True:
        draw_grid_with_curses(stdscr, grid_map, yy, xx, grid2=lazered_grid, answer=answer)
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
            if yy > 0:
                yy -= 1
        if key == ord('s') or key == curses.KEY_DOWN:
            if yy < (max_y + 1):
                yy += 1
        if key == ord('a') or key == curses.KEY_LEFT: # Since the entire image fits in my terminal window, I'm going to use the left and right keys to progress the solution instead
            if xx > 0:
                xx -= 1
        if key == ord('d') or key == curses.KEY_RIGHT:
            if xx < max_x - 2:
                xx += 1

def start(stdscr):
    curses.start_color()
    curses.use_default_colors()
    if curses.can_change_color():
        curses.init_color(curses.COLOR_YELLOW, 1000, 1000, 0)
    curses.init_pair(1, curses.COLOR_YELLOW, -1)
    curses.init_pair(2, curses.COLOR_RED, -1)
    curses.init_pair(3, curses.COLOR_GREEN, -1)

    if args.test:
        #for row in grid_map:
        #    print(len(row))
        show_solution(stdscr, grid_map, None)
        

    if args.part_1 or args.part_2:
        lasers_xs = [grid_map[0].find('S')]
        import copy
        lazered_grid = copy.copy(grid_map)
        answer = 0
        if args.part_2:
            laser_worlds = [0] * len(grid_map[0])
            laser_worlds[lasers_xs[0]] = 1
        for i, row in enumerate(grid_map):
            splitters_xs = [j for j in range(len(row)) if row.startswith('^', j)]
            new_lasers_xs = []
            for laser_x in lasers_xs:
                if laser_x in splitters_xs:
                    if args.part_1:
                        answer += 1
                    else:
                        laser_worlds[laser_x -1] += 1 * laser_worlds[laser_x]
                        laser_worlds[laser_x +1] += 1 * laser_worlds[laser_x]
                        laser_worlds[laser_x] = 0
                    if laser_x -1 not in new_lasers_xs:
                        new_lasers_xs += [laser_x -1]
                    if laser_x +1 not in new_lasers_xs:
                        new_lasers_xs += [laser_x +1]
                    lazered_grid[i] = lazered_grid[i][:laser_x -1] + '|^|' + row[laser_x +1:]
                else:
                    lazered_grid[i] = lazered_grid[i][:laser_x] + '|' + row[laser_x + 1:]
                    if laser_x not in new_lasers_xs or args.part_2:
                        new_lasers_xs += [laser_x]
            print('\r', i, "out of", len(grid_map), "lines lasered.", end='')
            lasers_xs = new_lasers_xs
        if args.part_2:
            answer = sum(laser_worlds)
        show_solution(stdscr, grid_map, lazered_grid, answer=str(answer))

curses.wrapper(start)