import sys, os, time


def part1(data):
    counter = 0
    for i in range(1, len(data)):
        if data[i - 1] < data[i]:
            counter += 1
    return counter


def part2(data):
    counter = 0
    for i in range(1, len(data) - 2):
        if data[i - 1] < data[i + 2]:
            counter += 1
    return counter


def testcase():
    sweepReport = open(os.path.join(os.path.dirname(__file__), "day-1-test.txt")).read()
    sweepReport = list(map(int, sweepReport.split("\n")))

    assert part1(sweepReport) == 7
    assert part2(sweepReport) == 5


if __name__ == "__main__":
    if len(sys.argv) > 1:
        testcase()

    sweepReport = open(
        os.path.join(os.path.dirname(__file__), "day-1-input.txt")
    ).read()
    sweepReport = list(map(int, sweepReport.split("\n")))

    s = time.perf_counter()
    print(f"Part 1: {part1(sweepReport)}")
    print(f"Part 2: {part2(sweepReport)}")
    print(f"> {os.path.basename(__file__)} {round(time.perf_counter() - s, 7)} secs\n")
