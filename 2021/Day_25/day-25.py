import os
import sys
import time


def isStagnant(pos, nextLoc, seacuType):
    return {
        nextLoc(*loc)
        if (nextLoc(*loc) not in pos and seacuType == seacu)
        else loc: seacu
        for loc, seacu in pos.items()
    }


def part1(data: list[str]):
    r, c = len(data), len(data[0])
    pos = {(x, y): data[x][y] for y in range(c) for x in range(r) if data[x][y] != "."}

    i = 1
    while True:
        newPos = pos.copy()
        pos = isStagnant(pos, lambda x, y: (x, (y + 1) % c), ">")
        pos = isStagnant(pos, lambda x, y: ((x + 1) % r, y), "v")
        if newPos == pos:
            return i
        i += 1


def testcase():
    map = open(os.path.join(os.path.dirname(__file__), "day-25-test.txt")).read()
    map = map.splitlines()

    assert part1(map) == 58


if __name__ == "__main__":
    if len(sys.argv) > 0:
        testcase()

    map = open(os.path.join(os.path.dirname(__file__), "day-25-input.txt")).read()
    map = map.splitlines()

    s = time.perf_counter()
    print(f"Part 1: {part1(map)}")
    print(f"> {os.path.basename(__file__)} {round(time.perf_counter() - s, 7)} secs\n")
