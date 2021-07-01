import os
from numpy import transpose, array
from collections import defaultdict


def incre(val1, val2):
    return val1, val2 + 1


def both_part(data):
    rules, my_tik, nby_tik = data
    all_ranges = set()
    fields = dict()

    # Making dictionary of class/field names and their respective ranges
    for elem in rules.split('\n'):
        field, rng = elem.split(': ')

        rng = rng.split(' or ')
        r1 = range(*incre(*map(int, rng[0].split('-'))))
        r2 = range(*incre(*map(int, rng[1].split('-'))))

        fields[field] = {*r1, *r2}
        all_ranges.update((*r1, *r2))

    my_tik = list(map(int, my_tik[13:].split(',')))

    # 2x2 list of nearby tickers with int elements
    nby_tik = [list(map(int, i.split(','))) for i in nby_tik.split('\n')[1:]]

    errorSum = 0
    error_ticket = []

    # Calculating all values not in any range
    for ticket in nby_tik:
        error = [x for x in ticket if x not in all_ranges]
        errorSum += sum(error)
        if len(error):
            error_ticket.append(ticket)

    # Removing tickets with invalid values
    for i in error_ticket:
        nby_tik.remove(i)

    nby_tik = [set(i) for i in array(nby_tik).transpose()]

    # Dictionary of all the fields that can hold a specific columns
    final_ans = defaultdict(set)
    for values, j in zip(nby_tik, range(20)):
        for field, rng in fields.items():
            if not len(values - rng):
                final_ans[field].add(j)

    final_ans = sorted(final_ans.items(), key = lambda x: len(x[1]), reverse = True)

    # Arranging fields for each column
    final_ans = [(j, *(k - final_ans[i + 1][1])) for i, (j, k) in enumerate(final_ans[:-1])] + [final_ans[-1]]

    total = 1
    for k, v in final_ans:
        if k[:6] == 'depart':
            total *= my_tik[v]

    return errorSum, total


def testcase():
    document = open(os.path.join(os.path.dirname(__file__), "day-16-test.txt")).read()
    document = document.split('\n\n')

    assert both_part(document) == (71, 1)


if __name__ == "__main__":
    testcase()

    document = open(os.path.join(os.path.dirname(__file__), "day-16-input.txt")).read()
    document = document.split('\n\n')

    print('Part 1: {0}\nPart 2: {1}'.format(*both_part(document)))