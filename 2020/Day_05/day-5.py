import sys, os, time
from itertools import combinations


ids = []


def part1(data):
    row, col = 0, 0
    seat_id = 0

    for seat in data:
        row, col = int(seat[:7].replace("F", "0").replace("B", "1"), 2), int(
            seat[7:].replace("L", "0").replace("R", "1"), 2
        )

        id_ = row * 8 + col
        ids.append(id_)

        if seat_id < id_:
            seat_id = id_

    return seat_id


def part2(data):
    for i, j in combinations(ids, 2):
        if abs(i - j) == 2 and ((i + j) // 2 not in ids):
            return (i + j) // 2


def testcase():
    seats = open(os.path.join(os.path.dirname(__file__), "day-5-test.txt")).read()
    seats = seats.split("\n")

    assert part1(seats) == 820


if __name__ == "__main__":
    if len(sys.argv) > 1:
        testcase()

    seats = open(os.path.join(os.path.dirname(__file__), "day-5-input.txt")).read()
    seats = seats.split("\n")

    s = time.perf_counter()
    print(f"Part 1: {part1(seats)}")
    print(f"Part 2: {part2(seats)}")
    print(f"> {os.path.basename(__file__)} {round(time.perf_counter() - s, 7)} secs\n")
