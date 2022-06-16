import sys, os, time
from itertools import combinations


def part1(data):
    for i, j in combinations(data, 2):
        if i + j == 2020:
            return i * j


def part2(data):
    for i, j, k in combinations(data, 3):
        if i + j + k == 2020:
            return i * j * k


def testcase():
    expense = open(os.path.join(os.path.dirname(__file__), "day-1-test.txt")).read()
    expense = list(map(int, expense.split("\n")))

    assert part1(expense) == 514579
    assert part2(expense) == 241861950


if __name__ == "__main__":
    if len(sys.argv) > 1:
        testcase()

    expense = open(os.path.join(os.path.dirname(__file__), "day-1-input.txt")).read()
    expense = list(map(int, expense.split("\n")))

    s = time.perf_counter()
    print(f"Part 1: {part1(expense)}")
    print(f"Part 2: {part2(expense)}")
    print(f"> {os.path.basename(__file__)} {round(time.perf_counter() - s, 7)} secs\n")
