def get_coordinate(starting_point, inp):
    direction = inp[0]
    distance = int(inp[1:])

    wire_x = starting_point[0]
    wire_y = starting_point[1]
    total_dist = starting_point[2]

    for i in range(distance):
        total_dist += 1
        if direction == "U":
            wire_y += 1
        elif direction == "D":
            wire_y -= 1
        elif direction == "R":
            wire_x += 1
        elif direction == "L":
            wire_x -= 1
        return (wire_x, wire_y, total_dist)


def get_all_coordinates(input):
    results = []
    point = (0,0,0)

    for inp in input:
        point = get_coordinate(point, inp)
        results.append(point)

    return results

def get_subset_coordinates(coords, input):
    results = []
    point = (0,0,0)

    for inp in input:
        point = get_coordinate(point, inp)
        if any(point[0] == ko and point[1] == vo for (ko,vo,_) in coords):
            results.append(point)

    return results


def solve(input1, input2):
    coords1 = get_all_coordinates(input1)
    # coords2 = get_all_coordinates(input2)

    crossing_points = get_subset_coordinates(coords1, input2)

    manhattan_point = min(crossing_points, key=lambda t: abs(t[0]) + abs(t[1]))
    print(abs(manhattan_point[0]) + abs(manhattan_point[1]))

    signal_distance = min(crossing_points, key=lambda t: t[2])
    print(signal_distance)
    return signal_distance


def main():
    with open("test.txt", encoding='utf-8') as f:
        input1 = f.readline().split(',')
        input2 = f.readline().split(',')
        solve(input1, input2)


if __name__ == "__main__":
    main()
