import sys, os, time


def part1(data_):
    total = 0
    d = ""

    for line in iter(data_.splitlines()):
        if line != "":
            d += line + ""

        else:
            total += len(set(list(d)))
            d = ""

    return total


def part2(data_):
    total = 0
    d = ""

    for line in iter(data_.splitlines()):
        if line != "":
            d += line + " "

        else:
            common = 0
            for char in "abcdefghijklmnopqrstuvwxyz":
                if all(char in ans for ans in d.split()):
                    common += 1

            total += common
            d = ""

    return total


def testcase():
    trajectory = open(os.path.join(os.path.dirname(__file__), "day-6-test.txt")).read()

    assert part1(trajectory) == 11
    assert part2(trajectory) == 6


if __name__ == "__main__":
    if len(sys.argv) > 1:
        testcase()

    trajectory = open(os.path.join(os.path.dirname(__file__), "day-6-input.txt")).read()

    s = time.perf_counter()
    print(f"Part 1: {part1(trajectory)}")
    print(f"Part 2: {part2(trajectory)}")
    print(f"> {os.path.basename(__file__)} {round(time.perf_counter() - s, 7)} secs\n")
