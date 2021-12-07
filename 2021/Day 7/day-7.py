import os
from math import ceil, floor


def part1(data):
    distance = sorted(map(int, data.split(',')))
    equi_distant = distance[len(distance) // 2]

    return sum(abs(equi_distant - i) for i in distance)


def part2(data):
    distance = list(map(int, data.split(',')))
    equi_distant = sum(distance) / len(distance)
    m1, m2 = ceil(equi_distant), floor(equi_distant)

    return min(
        sum((abs(m1 - i) * (abs(m1 - i) + 1)) // 2 for i in distance),
        sum((abs(m2 - i) * (abs(m2 - i) + 1)) // 2 for i in distance),
    )


def testcase():
    rules = open(os.path.join(os.path.dirname(__file__), "day-7-test.txt")).read()

    assert part1(rules) == 37
    assert part2(rules) == 168


if __name__ == "__main__":
    testcase()

    rules = open(os.path.join(os.path.dirname(__file__), "day-7-input.txt")).read()

    print(f"Part 1: {part1(rules)}")
    print(f"Part 2: {part2(rules)}")
