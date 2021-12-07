import os


def both_parts(data, days):
    age_list = map(int, data.split(','))

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
    testcase()

    ages = open(os.path.join(os.path.dirname(__file__), "day-6-input.txt")).read()

    print(f"Part 1: {both_parts(ages, 80)}")
    print(f"Part 2: {both_parts(ages, 256)}")