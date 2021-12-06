import os


def part1(data):
    points = set()
    solution = set()

    for line in data:
        start, end = line.split(' -> ')
        start_x, start_y = map(int, start.split(','))
        end_x, end_y = map(int, end.split(','))

        if start_x == end_x:
            start_y, end_y = sorted((start_y, end_y))
            rng = set((start_x, i) for i in range(start_y, end_y + 1))
            solution.update(points.intersection(rng))
            points.update(rng)
        elif start_y == end_y:
            start_x, end_x = sorted((start_x, end_x))
            rng = set((i, start_y) for i in range(start_x, end_x + 1))
            solution.update(points.intersection(rng))
            points.update(rng)

    return len(solution)


def part2(data):
    points = set()
    solution = set()

    for line in data:
        start, end = line.split(' -> ')
        start_x, start_y = map(int, start.split(','))
        end_x, end_y = map(int, end.split(','))

        if start_x == end_x:
            start_y, end_y = sorted((start_y, end_y))
            rng = set((start_x, i) for i in range(start_y, end_y + 1))
        elif start_y == end_y:
            start_x, end_x = sorted((start_x, end_x))
            rng = set((i, start_y) for i in range(start_x, end_x + 1))
        elif end_y - start_y == end_x - start_x:
            start_x, end_x = sorted((start_x, end_x))
            start_y, end_y = sorted((start_y, end_y))
            rng = set(zip(range(start_x, end_x + 1), range(start_y, end_y + 1)))
        else:
            start_x, end_x = sorted((start_x, end_x), reverse=True)
            start_y, end_y = sorted((start_y, end_y))
            rng = set(zip(range(start_x, end_x - 1, -1), range(start_y, end_y + 1)))

        solution.update(points.intersection(rng))
        points.update(rng)

    return len(solution)


def testcase():
    vents_map = open(os.path.join(os.path.dirname(__file__), "day-5-test.txt")).read()
    vents_map = vents_map.split('\n')

    assert part1(vents_map) == 5
    assert part2(vents_map) == 12


if __name__ == "__main__":
    testcase()

    vents_map = open(os.path.join(os.path.dirname(__file__), "day-5-input.txt")).read()
    vents_map = vents_map.split('\n')

    print(f"Part 1: {part1(vents_map)}")
    print(f"Part 2: {part2(vents_map)}")