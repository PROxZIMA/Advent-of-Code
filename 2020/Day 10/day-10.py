import os


def both_part(data):
    diff1, diff3, pac_of_1, arrange = 0, 0, 0, 1

    for i in range(1, len(data)):
        if data[i] - data[i - 1] == 1:
            diff1 += 1
            pac_of_1 += 1
        else:
            diff3 += 1
            arrange *= (7 if pac_of_1 == 4 else 4 if pac_of_1 == 3 else 2 if pac_of_1 == 2 else 1)
            pac_of_1 = 0

    return (diff1 * diff3, arrange)


def testcase():
    joltage = open(os.path.join(os.path.dirname(__file__), "day-10-test.txt")).read()
    joltage = [0] + (joltage := sorted(map(int, joltage.split('\n')))) + [joltage[-1] + 3]

    assert both_part(joltage) == (220, 19208)


if __name__ == "__main__":
    testcase()

    joltage = open(os.path.join(os.path.dirname(__file__), "day-10-input.txt")).read()
    joltage = [0] + (joltage := sorted(map(int, joltage.split('\n')))) + [joltage[-1] + 3]

    print('Part 1: {0}\nPart 2: {1}'.format(*both_part(joltage)))