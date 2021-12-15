import os
from collections import defaultdict


def polymer_pair(s):
    return [s[i:i+2] for i in range(len(s)-1)]


def count_polymer(polymer, polymer_map):
    count = defaultdict(int)

    for poly in polymer_map:
        count[poly[0]] += polymer_map[poly]

    count[polymer[-1]] += 1

    return max(count.values()) - min(count.values())


def both_part(data):
    polymer = data[0]
    pair_insertion = dict((data[i].split(' -> ') for i in range(2, len(data))))

    polymer_map = defaultdict(int, dict([[poly, 1] for poly in polymer_pair(polymer)]))

    for _ in range(40):
        old_polymer_map = polymer_map.copy()

        for poly in [i for i in polymer_map if polymer_map[i] > 0]:
            polymer_map[poly] -= old_polymer_map[poly]

            for i in polymer_pair(f'{poly[0]}{pair_insertion[poly]}{poly[1]}'):
                polymer_map[i] += old_polymer_map[poly]

        if _ == 9:
            count_10 = count_polymer(polymer, polymer_map)

    count_40 = count_polymer(polymer, polymer_map)

    return count_10, count_40


def testcase():
    submarine_manual = open(os.path.join(os.path.dirname(__file__), "day-14-test.txt")).read()
    submarine_manual = submarine_manual.split('\n')

    assert both_part(submarine_manual) == (1588, 2188189693529)


if __name__ == "__main__":
    testcase()

    submarine_manual = open(os.path.join(os.path.dirname(__file__), "day-14-input.txt")).read()
    submarine_manual = submarine_manual.split('\n')

    print('Part 1: {0}\nPart 2: {1}'.format(*both_part(submarine_manual)))