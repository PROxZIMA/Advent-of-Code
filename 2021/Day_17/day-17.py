import sys, os, time, re
from collections import defaultdict
from itertools import product


def both_part(data):
    _, x1, x2, _, y1, y2 = re.split("=|\.\.|, ", data)
    x1, x2, y1, y2 = map(int, (x1, x2, y1, y2))
    y1, y2 = -y1, -y2

    path_data = defaultdict(lambda: defaultdict(set))

    start, infinite_x = 1, []

    while start < x2 + 1:
        sum_x = 0

        for Xv in range(start, x2 + 1):
            sum_x += Xv
            if x1 <= sum_x <= x2:
                seconds = Xv - start + 1

                if start == 1:
                    infinite_x.append((Xv, seconds))

                path_data[seconds]["Xv"].add(Xv)

            if sum_x > x2:
                break

        start += 1

    nNumberSum = {i: (i * (i + 1)) // 2 for i in range(6)}

    for Yv in range(y1 + 1):
        for i in range(1, 6):

            if y2 <= i * Yv + nNumberSum[i] <= y1 and Yv:
                path_data[2 * Yv + 1 + i]["Yv"].add(Yv)

            if y2 <= i * Yv + nNumberSum[i - 1] <= y1:
                path_data[i]["Yv"].add(-Yv)

    velocity, path_len = zip(*infinite_x)
    for i in path_data:
        if any(i >= x for x in path_len):
            path_data[i]["Xv"].update(velocity)

    sol = set()
    for i in path_data:
        sol.update(product(path_data[i]["Xv"], path_data[i]["Yv"]))

    return ((y1) * (y1 - 1)) // 2, len(sol)


def testcase():
    target_area = open(
        os.path.join(os.path.dirname(__file__), "day-17-test.txt")
    ).read()

    assert both_part(target_area) == (45, 112)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        testcase()

    target_area = open(
        os.path.join(os.path.dirname(__file__), "day-17-input.txt")
    ).read()

    s = time.perf_counter()
    print("Part 1: {0}\nPart 2: {1}".format(*both_part(target_area)))
    print(f"> {os.path.basename(__file__)} {round(time.perf_counter() - s, 7)} secs\n")
