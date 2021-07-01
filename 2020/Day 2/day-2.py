import os
from itertools import combinations


def part1(data):
    total = 0

    for password in iter(data.splitlines()):
        length, char, passwd = password.split()

        mini, maxi = map(int, length.split('-'))
        char = char[0]

        if mini <= passwd.count(char) <= maxi:
            total += 1

    return total


def part2(data):
    total = 0

    for password in iter(data.splitlines()):
        length, char, passwd = password.split()

        mini, maxi = map(int, length.split('-'))
        mini -= 1
        maxi -= 1
        char = char[0]

        if (passwd[mini] == char) ^ (passwd[maxi] == char):
            total += 1

    return total


def testcase():
    passwords = open(os.path.join(os.path.dirname(__file__), "day-2-test.txt")).read()

    assert part1(passwords) == 2
    assert part2(passwords) == 1


if __name__ == "__main__":
    testcase()

    passwords = open(os.path.join(os.path.dirname(__file__), "day-2-input.txt")).read()

    print(f"Part 1: {part1(passwords)}")
    print(f"Part 2: {part2(passwords)}")