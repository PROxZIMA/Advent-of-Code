import sys, os, time


def is_lowest(i, j, data):
    point = data[i][j]
    neighbours = []

    if i - 1 >= 0:
        neighbours.append((i - 1, j))
    if i + 1 < len(data):
        neighbours.append((i + 1, j))
    if j - 1 >= 0:
        neighbours.append((i, j - 1))
    if j + 1 < len(data[i]):
        neighbours.append((i, j + 1))

    return set(neighbours), all(point < data[i][j] for i, j in neighbours)


def part1(data):
    total = 0
    lowest = []

    for i in range(len(data)):
        for j in range(len(data[i])):
            neighbours, is_low = is_lowest(i, j, data)
            if is_low:
                total += data[i][j] + 1
                lowest.append((i, j))

    return total, lowest


def lowPointNeighbours(x, y, data, seen=None):

    seen = seen or set()
    seen.add((x, y))

    neighbours, is_low = is_lowest(x, y, data)
    neighbours -= seen

    for i, j in neighbours:
        point = data[i][j]
        if point not in seen and point != 9:
            seen |= lowPointNeighbours(i, j, data, seen)

    return seen


def part2(data, lowest):
    visited_basins, basins, product = set(), set(), 1

    for x, y in lowest:
        if (x, y) not in visited_basins:
            basin = lowPointNeighbours(x, y, data)
            visited_basins |= basin
            basins.add(tuple(basin))

    top3Basins = sorted(basins, key=lambda x: len(x), reverse=True)[:3]

    for basin in top3Basins:
        product *= len(basin)

    return product


def testcase():
    heightmap = open(os.path.join(os.path.dirname(__file__), "day-9-test.txt")).read()
    heightmap = [list(map(int, list(line))) for line in heightmap.split("\n")]

    total, lowest = part1(heightmap)
    assert total == 15
    assert part2(heightmap, lowest) == 1134


if __name__ == "__main__":
    if len(sys.argv) > 1:
        testcase()

    heightmap = open(os.path.join(os.path.dirname(__file__), "day-9-input.txt")).read()
    heightmap = [list(map(int, list(line))) for line in heightmap.split("\n")]

    total, lowest = part1(heightmap)
    s = time.perf_counter()
    print(f"Part 1: {total}")
    print(f"Part 2: {part2(heightmap, lowest)}")
    print(f"> {os.path.basename(__file__)} {round(time.perf_counter() - s, 7)} secs\n")
