import sys, os, time


def part1(data):
    horizontalPosition, depth = 0, 0

    for movement in data.splitlines():
        direction, value = movement.split()
        value = int(value)

        if direction == "forward":
            horizontalPosition += value
        elif direction == "down":
            depth += value
        elif direction == "up":
            depth -= value

    return horizontalPosition * depth


def part2(data):
    horizontalPosition, depth, aim = 0, 0, 0

    for movement in data.splitlines():
        direction, value = movement.split()
        value = int(value)

        if direction == "forward":
            horizontalPosition += value
            depth += aim * value
        elif direction == "down":
            aim += value
        elif direction == "up":
            aim -= value

    return horizontalPosition * depth


def testcase():
    course = open(os.path.join(os.path.dirname(__file__), "day-2-test.txt")).read()

    assert part1(course) == 150
    assert part2(course) == 900


if __name__ == "__main__":
    if len(sys.argv) > 1:
        testcase()

    course = open(os.path.join(os.path.dirname(__file__), "day-2-input.txt")).read()

    s = time.perf_counter()
    print(f"Part 1: {part1(course)}")
    print(f"Part 2: {part2(course)}")
    print(f"> {os.path.basename(__file__)} {round(time.perf_counter() - s, 7)} secs\n")
