import os
from itertools import combinations
import timeit


def part1(data, n):
    for val in range(n, len(data)):
        if data[val] not in [a+b for a, b in combinations(data[val-n:val], 2)]:
            return data[val]


def part2(data, n):
    i, i_start, acc = 0, 0, 0

    while True:
        acc += data[i]

        if acc > n:
            while True:
                if acc <= n:
                    break
                acc -= data[i_start]
                i_start += 1

        if acc == n:
            lis = data[i_start : i + 1]
            return max(lis) + min(lis)

        i += 1


def testcase():
    cypher = open(os.path.join(os.path.dirname(__file__), "day-9-test.txt")).read()
    cypher = list(map(int, cypher.split('\n')))

    assert (p1 := part1(cypher, 5)) == 127
    assert part2(cypher, p1) == 62


if __name__ == "__main__":
    # testcase()

    cypher = open(os.path.join(os.path.dirname(__file__), "day-9-input.txt")).read()
    cypher = list(map(int, cypher.split('\n')))

    print(f"Part 1: {(p1 := part1(cypher, 25))}")
    print(f"Part 2: {part2(cypher, p1)}")
    # print(timeit.timeit("part2(cypher, p1)", setup="from __main__ import part2, cypher, p1", number=100000))
