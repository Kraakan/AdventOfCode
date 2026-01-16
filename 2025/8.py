import argparse
import curses
import sys

parser = argparse.ArgumentParser(description="Day 8 of Advent of Code 2025")
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

f = open("input_day8", "r")
inp = f.read().rstrip()
coords = inp.split('\n')
coords = list(map(lambda x: list(map(float, x.split(','))), coords))

def distance(p1: tuple, p2: tuple) -> float:
    return ((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2 + (p2[2]-p1[2])**2)#**(1/2) # It's not necessary to take the square root since we only care about which distance is shortest



if args.test:
    d_min = sys.float_info.max
    closest = (None, None)
    for i, coord1 in enumerate(coords):
        for j, coord2 in enumerate(coords):
            if coord1 != coord2:
                d = distance(coord1,coord2)
                closest = (i, j)
                if d < d_min:
                    d_min = d
            print('\r', d_min, end='')
    
    print('\n', closest)

if args.part_1 or args.part_2:
    from collections import deque
    try:
        f = open("output_day8", "r")
        connected = f.read().rstrip().split('\n')
        connected = list(map(lambda x: tuple(map(int, x.split(' '))), connected))
        
    except(FileNotFoundError):
        connected = deque([], maxlen=1000)
        for i, coord1 in enumerate(coords):
            for j, coord2 in enumerate(coords):
                added = False
                if i != j and (i, j) not in connected and (j, i) not in connected:
                    this_distance = distance(coord1, coord2)
                    for k, connection in enumerate(connected):
                        if distance(coords[connection[0]], coords[connection[1]]) > this_distance:
                            added = True
                            break
                    if added:
                        if len(connected) > 999:
                            longest_connection = connected.pop()
                        connected.insert(k, (i, j))
                    elif len(connected) < 1000:
                        connected.append((i, j))
                print('\r', 1000 * i + j, "/ 1000000 coordinates scanned.", end='')
        print('\nSaving connections...')
        with open("output_day8", "w") as f:
            for connection in connected:
                f.write(str(connection[0]) + ' ' + str(connection[1]) + '\n')

    circuits = []

    """for i, connection in enumerate(connected):
        in_larger_circuit = None
        point_1_string = str(connection[0])
        while len(point_1_string) < 3:
            point_1_string = '0' + point_1_string
        point_2_string = str(connection[1])
        while len(point_2_string) < 3:
            point_2_string = '0' + point_2_string
        check_clusters = False
        delete = None
        for j, circuit in enumerate(circuits):
            if point_1_string in circuit:
                in_larger_circuit = point_1_string
                if point_2_string not in circuit:
                    check_clusters = True
                break
            if point_2_string in circuit:
                in_larger_circuit = point_2_string
                if point_1_string not in circuit:
                    check_clusters = True
                break
        if not in_larger_circuit:
            circuits.append(' ' + point_1_string + ' ' + point_2_string)
        elif check_clusters:
            for k, circuit in enumerate(circuits): # j is still what it was when the previous loop encountered break
                if k != j:
                    if point_1_string in circuit or point_2_string in circuit:
                        delete = k
                        break
        if delete:
            circuits[j] += circuits[k]
            del(circuits[delete])
        elif point_1_string == in_larger_circuit:
            circuits[j] += ' ' +  point_2_string
        elif point_2_string == in_larger_circuit:
            circuits[j] += ' ' +  point_1_string
        print('\r', i, "connections checked, ", len(circuits), "circuits created.", end='')
    print()
    breakpoint()"""

    for i, connection in enumerate(connected):
        in_larger_circuit = None
        check_clusters = False
        delete = None
        for j, circuit in enumerate(circuits):
            if connection[0] in circuit:
                in_larger_circuit = connection[0]
                if connection[1] not in circuit:
                    check_clusters = True
                break
            if connection[1] in circuit:
                in_larger_circuit = connection[1]
                if connection[0] not in circuit:
                    check_clusters = True
                break
        if not in_larger_circuit:
            circuits.append(set([connection[0],connection[1]]))
        elif check_clusters:
            for k, circuit in enumerate(circuits): # j is still what it was when the previous loop encountered break
                if k != j:
                    if connection[0] in circuit or connection[1] in circuit:
                        delete = k
                        break
        if delete:
            circuits[j].update(circuits[k])
            del(circuits[delete])
        elif connection[0] == in_larger_circuit:
            circuits[j].add(connection[1])
        elif connection[1] == in_larger_circuit:
            circuits[j].add(connection[0])
        print('\r', i, "connections checked, ", len(circuits), "circuits created.", end='')
    print()


    max_3_circuit_lengths = deque([], maxlen=3)

    for circuit in circuits:
        in_top_3 = False
        length = len(circuit)
        for i, long_length in enumerate(max_3_circuit_lengths):
            if length > long_length:
                in_top_3 = True
                break
        if in_top_3:
            if len(max_3_circuit_lengths) > 2:
                max_3_circuit_lengths.pop()
            max_3_circuit_lengths.insert(i, length)
        elif len(max_3_circuit_lengths) < 3:
            max_3_circuit_lengths.append(length)
    print("Longest 3 circuits:", max_3_circuit_lengths)
    
    product = 1

    for c in max_3_circuit_lengths:
        product *= c
    
    print("Product:", product)

if args.part_2: # Longest connection necessary to connect everything
    last_connection = (None, None) # indexes for the coords list
    last_connection_distance = 0

    # First, measure the connection necessary to connect up all the circuits 
    shortest_distance = [sys.float_info.max] * 1000
    connection_points = [None] * len(circuits)
    connected_circuit = set()
    for i, circuit in enumerate(circuits):
        for coord_i in circuit:
            if coord_i not in connected_circuit:
                for j, other_circuit in enumerate(circuits):
                    for coord_j in other_circuit:
                        if coord_i != coord_j:
                            this_distance = distance(coords[coord_i], coords[coord_j])
                            if this_distance < shortest_distance[i]:
                                shortest_distance[coord_i] = this_distance
                                # save this coordinate
                                other_connected_circuit = other_circuit
                                connection_points[i] = (coord_i, coord_j)
        if connection_points[i]:
            if shortest_distance[connection_points[i][0]] > last_connection_distance:
                last_connection_distance = shortest_distance[connection_points[i][0]]
                last_connection = connection_points[i]

        connected_circuit.update(circuit, other_connected_circuit)


    # About fifty junction boxes still appear to be disconnected from our circuit.
    # We need to find their closest neighbors to determine which connection will be made last
    

    for i in range(1000):
        connected_j = None
        if i not in connected_circuit:
            for j in range(1000):
                if i != j:
                    this_distance = distance(coords[i], coords[j])
                    if this_distance < shortest_distance[i]:
                        shortest_distance[i] = this_distance
                        connected_j = j
            if shortest_distance[i] > last_connection_distance:
                last_connection_distance = shortest_distance[i]
                last_connection = (i, connected_j)
    import copy
    sorted_distances = copy.copy(shortest_distance)
    sorted_distances.sort(reverse=True)
    breakpoint()
    print(coords[last_connection[0]][0], '*', coords[last_connection[1]][0])
    print(coords[last_connection[0]][0] * coords[last_connection[1]][0])