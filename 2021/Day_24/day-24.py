import os
import sys
import time


def both_part(data: list[str]):
    # div = [1, 1, 1, 26, 1, 26, 1, 1, 1, 26, 26, 26, 26, 26]
    # check = [10, 13, 13, -11, 11, -4, 12, 12, 15, -2, -5, -11, -13, -10]
    # add = [13, 10, 3, 1, 9, 3, 5, 1, 0, 13, 7, 15, 12, 8]
    maxi, mini = [9] * 14, [1] * 14
    cmds = [line.split() for line in data.splitlines()]

    stack = []
    for i in range(14):
        div, check, add = map(int, [cmds[i * 18 + x][-1] for x in [4, 5, 15]])
        if div == 1:
            stack.append((i, add))
        elif div == 26:
            j, add = stack.pop()
            maxi[i] = maxi[j] + add + check
            mini[i] = mini[j] + add + check
            if maxi[i] > 9:
                maxi[i], maxi[j] = 9, 9 + maxi[j] - maxi[i]
            if mini[i] < 1:
                mini[i], mini[j] = 1, 1 + mini[j] - mini[i]

    return "".join(map(str, maxi)), "".join(map(str, mini))


def testcase():
    monad = open(os.path.join(os.path.dirname(__file__), "day-24-test.txt")).read()

    assert both_part(monad) == ("69914999975369", "14911675311114")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        testcase()

    monad = open(os.path.join(os.path.dirname(__file__), "day-24-input.txt")).read()

    s = time.perf_counter()
    print("Part 1: {0}\nPart 2: {1}".format(*both_part(monad)))
    print(f"> {os.path.basename(__file__)} {round(time.perf_counter() - s, 7)} secs\n")
