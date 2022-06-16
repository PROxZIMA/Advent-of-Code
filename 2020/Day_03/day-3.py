import sys, os, time


def part1(data):
    tree = 0
    row, col, l = 0, 0, len(data[0])

    while row < len(data):
        if data[row][col % l] == "#":
            tree += 1

        row += 1
        col += 3

    return tree


def part2(data):
    t1, t2, t3, t4, t5 = 0, 0, 0, 0, 0
    row, col, l = 0, 0, len(data[0])

    while row < len(data):
        if data[row][col % l] == "#":
            t1 += 1

        row += 1
        col += 1

    row, col = 0, 0

    while row < len(data):
        if data[row][col % l] == "#":
            t2 += 1

        row += 1
        col += 3

    row, col = 0, 0

    while row < len(data):
        if data[row][col % l] == "#":
            t3 += 1

        row += 1
        col += 5

    row, col = 0, 0

    while row < len(data):
        if data[row][col % l] == "#":
            t4 += 1

        row += 1
        col += 7

    row, col = 0, 0

    while row < len(data):
        if data[row][col % l] == "#":
            t5 += 1

        row += 2
        col += 1

    return t1 * t2 * t3 * t4 * t5


def testcase():
    trajectory = open(os.path.join(os.path.dirname(__file__), "day-3-test.txt")).read()
    trajectory = trajectory.split("\n")

    assert part1(trajectory) == 7
    assert part2(trajectory) == 336


if __name__ == "__main__":
    if len(sys.argv) > 1:
        testcase()

    trajectory = open(os.path.join(os.path.dirname(__file__), "day-3-input.txt")).read()
    trajectory = trajectory.split("\n")

    s = time.perf_counter()
    print(f"Part 1: {part1(trajectory)}")
    print(f"Part 2: {part2(trajectory)}")
    print(f"> {os.path.basename(__file__)} {round(time.perf_counter() - s, 7)} secs\n")
