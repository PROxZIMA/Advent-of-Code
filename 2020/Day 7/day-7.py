import os


bags = dict()
colors = set()


def recurr(color):
    for k, v in bags.items():
        if color in list(x[1] for x in v):
            colors.add(k)
            recurr(k)


def part1(data):
    for line in data:
        key, values = line.split(' contain ')
        key, values = key[:-5], values[:-1].split(', ')

        for i in range(len(values)):
            if values[i][0] == '1':
                values[i] = (int(values[i][0]), values[i][2:-4])
            elif values[i][0] != 'n':
                values[i] = (int(values[i][0]), values[i][2:-5])
            else:
                values[i] = (0, values[i][3:-5])

        bags[key] = values

    recurr('shiny gold')

    return len(colors)


def part2(color):
    if color == 'other':
        return 0

    return sum((item[0] + item[0] * part2(item[1])) for item in bags[color])


def testcase():
    rules = open(os.path.join(os.path.dirname(__file__), "day-7-test.txt")).read()
    rules = rules.split('\n')

    assert part1(rules) == 4
    assert part2('shiny gold') == 32


if __name__ == "__main__":
    testcase()

    rules = open(os.path.join(os.path.dirname(__file__), "day-7-input.txt")).read()
    rules = rules.split('\n')

    bags = dict()
    colors = set()

    print(f"Part 1: {part1(rules)}")
    print(f"Part 2: {part2('shiny gold')}")