import sys, os, time


def both_parts(data, days):
    age_list = map(int, data.split(","))

    lanternfish = [0] * 9

    for age in age_list:
        lanternfish[age] += 1

    for _ in range(days):
        lanternfish.append(lanternfish.pop(0))
        lanternfish[6] += lanternfish[8]

    return sum(lanternfish)


def testcase():
    ages = open(os.path.join(os.path.dirname(__file__), "day-6-test.txt")).read()

    assert both_parts(ages, 80) == 5934
    assert both_parts(ages, 256) == 26984457539


if __name__ == "__main__":
    if len(sys.argv) > 1:
        testcase()

    ages = open(os.path.join(os.path.dirname(__file__), "day-6-input.txt")).read()

    s = time.perf_counter()
    print(f"Part 1: {both_parts(ages, 80)}")
    print(f"Part 2: {both_parts(ages, 256)}")
    print(f"> {os.path.basename(__file__)} {round(time.perf_counter() - s, 7)} secs\n")
