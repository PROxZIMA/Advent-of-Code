import os
from math import sin, cos, radians


def part1(data):
    angle, x, y = 0, 0, 0

    for inst in data:
        act, mag = inst[0], int(inst[1:])

        if act == 'L':
            angle += mag

        elif act == 'R':
            angle -= mag

        elif act == 'F':
            x += mag * cos(radians(angle))
            y += mag * sin(radians(angle))

        else :
            delta = {'N': (0, +mag) , 'S': (0, -mag) , 'E': (mag, 0) ,  'W': (-mag, 0)}
            x += delta[act][0]
            y += delta[act][1]

    return int(abs(x) + abs(y))


def part2(data):
    x, y, wx, wy = 0, 0, 10, 1

    for inst in data:
        act, mag = inst[0], int(inst[1:])

        if act == 'L':
            wx0, wy0, rad_ang = wx, wy, radians(mag)

            wx = round(wx0 * cos(rad_ang) - wy0 * sin(rad_ang))
            wy = round(wx0 * sin(rad_ang) + wy0 * cos(rad_ang))

        elif act == 'R':
            wx0, wy0, rad_ang = wx, wy, radians(-mag)

            wx = round(wx0 * cos(rad_ang) - wy0 * sin(rad_ang))
            wy = round(wx0 * sin(rad_ang) + wy0 * cos(rad_ang))

        elif act == 'F':
            x += wx * mag
            y += wy * mag

        else :
            delta = {'N': (0, +mag) , 'S': (0, -mag) , 'E': (mag, 0) ,  'W': (-mag, 0)}
            wx += delta[act][0]
            wy += delta[act][1]

    return int(abs(x) + abs(y))


def testcase():
    instructions = open(os.path.join(os.path.dirname(__file__), "day-12-test.txt")).read()
    instructions = instructions.split('\n')

    assert part1(instructions) == 25
    assert part2(instructions) == 286


if __name__ == "__main__":
    testcase()

    instructions = open(os.path.join(os.path.dirname(__file__), "day-12-input.txt")).read()
    instructions = instructions.split('\n')

    print(f"Part 1: {part1(instructions)}")
    print(f"Part 2: {part2(instructions)}")