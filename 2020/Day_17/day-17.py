import sys, os, time
from math import sin, cos, radians


def part1(data):
    pass


def part2(data):
    pass


def testcase():
    instructions = open(
        os.path.join(os.path.dirname(__file__), "day-17-test.txt")
    ).read()
    instructions = instructions.split("\n")

    # assert part1(instructions) == 112
    part1(instructions)
    # assert part2(instructions) == 286


if __name__ == "__main__":
    if len(sys.argv) > 1:
        testcase()

    instructions = open(
        os.path.join(os.path.dirname(__file__), "day-17-input.txt")
    ).read()
    instructions = instructions.split("\n")

    # print(f"Part 1: {part1(instructions)}")
    # print(f"Part 2: {part2(instructions)}")
