import os
import copy


def occu_seat(lis, r, c, para):
    surr = ''
    surr += lis[r - 1][c - 1] + lis[r - 1][c] + lis[r - 1][c + 1] + \
            lis[  r  ][c - 1]                 + lis[  r  ][c + 1] + \
            lis[r + 1][c - 1] + lis[r + 1][c] + lis[r + 1][c + 1]

    if para == 'no':
        return '#' not in surr
    else:
        return surr.count('#') >= 4


def total_occu(lis):
    total = 0
    for i in lis:
        for j in i:
            if j == '#':
                total += 1

    return total


def part1(data):
    temp_lay = copy.deepcopy(data)
    height, width = len(data) - 1, len(data[0]) - 1

    for row in range(1, height):
        for seat in range(1, width):

            if data[row][seat] == 'L' and occu_seat(data, row, seat, 'no'):
                temp_lay[row][seat] = '#'

            elif data[row][seat] == '#' and occu_seat(data, row, seat, 'four'):
                temp_lay[row][seat] = 'L'

    if temp_lay == data:
        return total_occu(temp_lay)
    else:
        return part1(temp_lay)


def occu_seat_alld(lis, r, c, para):
    height, width = len(lis) - 1, len(lis[0]) - 1
    surr = ''

    for i in range(c + 1, width):
        if lis[r][i] != '.':
            surr += lis[r][i]
            break

    for i, j in zip(range(r + 1, height), range(c + 1, width)):
        if lis[i][j] != '.':
            surr += lis[i][j]
            break

    for i in range(r + 1, height):
        if lis[i][c] != '.':
            surr += lis[i][c]
            break

    for i, j in zip(range(r + 1, height), range(c - 1, 0, -1)):
        if lis[i][j] != '.':
            surr += lis[i][j]
            break

    for i in range(c - 1, 0, -1):
        if lis[r][i] != '.':
            surr += lis[r][i]
            break

    for i, j in zip(range(r - 1, 0, -1), range(c - 1, 0, -1)):
        if lis[i][j] != '.':
            surr += lis[i][j]
            break

    for i in range(r - 1, 0, -1):
        if lis[i][c] != '.':
            surr += lis[i][c]
            break

    for i, j in zip(range(r - 1, 0, -1), range(c + 1, width)):
        if lis[i][j] != '.':
            surr += lis[i][j]
            break

    if para == 'no':
        return '#' not in surr
    else:
        return surr.count('#') >= 5


def part2(data):
    temp_lay = copy.deepcopy(data)
    height, width = len(data) - 1, len(data[0]) - 1

    for row in range(1, height):
        for seat in range(1, width):

            if data[row][seat] == 'L' and occu_seat_alld(data, row, seat, 'no'):
                temp_lay[row][seat] = '#'

            elif data[row][seat] == '#' and occu_seat_alld(data, row, seat, 'five'):
                temp_lay[row][seat] = 'L'

    if temp_lay == data:
        return total_occu(temp_lay)
    else:
        return part2(temp_lay)



def testcase():
    layout = open(os.path.join(os.path.dirname(__file__), "day-11-test.txt")).read()

    layout = [['0'] + list(i) + ['0'] for i in layout.split('\n')]
    layout.append(['0'] * len(layout[0]))
    layout.insert(0, ['0'] * len(layout[0]))

    assert part1(layout) == 37
    assert part2(layout) == 26


if __name__ == "__main__":
    testcase()

    layout = open(os.path.join(os.path.dirname(__file__), "day-11-input.txt")).read()

    layout = [['0'] + list(i) + ['0'] for i in layout.split('\n')]
    layout.append(['0'] * len(layout[0]))
    layout.insert(0, ['0'] * len(layout[0]))

    print(f"Part 1: {part1(layout)}")
    print(f"Part 2: {part2(layout)}")
