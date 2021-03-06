import sys, os, time


def both_part(data):
    numbers = list(map(int, data.split(","))) + [0] * 30000000
    lastOccur = dict()

    for i in range(30000000):
        if numbers[i] in lastOccur:
            numbers[i + 1] = i - lastOccur[numbers[i]]

        lastOccur[numbers[i]] = i

    return numbers[2019], numbers[30000000 - 1]


def testcase():
    numbers = open(os.path.join(os.path.dirname(__file__), "day-15-test.txt")).read()

    assert both_part(numbers) == (436, 175594)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        testcase()

    numbers = open(os.path.join(os.path.dirname(__file__), "day-15-input.txt")).read()

    s = time.perf_counter()
    print("Part 1: {0}\nPart 2: {1}".format(*both_part(numbers)))
    print(f"> {os.path.basename(__file__)} {round(time.perf_counter() - s, 7)} secs\n")
