import sys, os, time


def part1(data):
    depart = int(data[0])
    buses = [int(n) for n in data[1].split(",") if n != "x"]
    bus_id = min(buses, key=lambda x: depart - depart % x + x)

    return (bus_id - depart % bus_id) * bus_id


def nextStop(start, step, nxt_bus, remainder):
    end = step * nxt_bus

    for val in range(start, end, step):
        if not (val + remainder) % nxt_bus:
            break

    return val, end


def part2(data):
    buses = [(int(y), x) for x, y in enumerate(data[1].split(",")) if y != "x"]

    start, step = 0, 1
    for bus, delay in sorted(buses):
        start, step = nextStop(start, step, bus, delay)

    return start


def testcase():
    notes = open(os.path.join(os.path.dirname(__file__), "day-13-test.txt")).read()
    notes = notes.split("\n")

    assert part1(notes) == 295
    assert part2(notes) == 1068781


if __name__ == "__main__":
    if len(sys.argv) > 1:
        testcase()

    notes = open(os.path.join(os.path.dirname(__file__), "day-13-input.txt")).read()
    notes = notes.split("\n")

    s = time.perf_counter()
    print(f"Part 1: {part1(notes)}")
    print(f"Part 2: {part2(notes)}")
    print(f"> {os.path.basename(__file__)} {round(time.perf_counter() - s, 7)} secs\n")
