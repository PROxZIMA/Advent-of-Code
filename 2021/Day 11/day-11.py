import os
from collections import deque
import numpy as np


def both_part(data):
    data = np.array(data)
    total_flashes, synchronizing, MAX = 0, 0, 10

    while data.any():
        stack = deque()

        for i in range(MAX):
            for j in range(MAX):
                data[i, j] += 1
                if data[i, j] > 9:
                    stack.append((i,j))

        original_stack = set(stack)

        while len(stack) > 0:
            i, j = stack.popleft()

            min_x = i-1 if i-1 >= 0 else 0
            min_y = j-1 if j-1 >= 0 else 0
            max_x = i+1 if i+1 < MAX else MAX-1
            max_y = j+1 if j+1 < MAX else MAX-1

            for x in range(min_x, max_x+1):
                for y in range(min_y, max_y+1):
                    if (x, y) not in original_stack:
                        data[x, y] += 1
                        if data[x, y] > 9:
                            original_stack.add((x, y))
                            stack.append((x,y))

            data[i, j] = 0

            if synchronizing < 100:
                total_flashes += 1

        synchronizing += 1

    return total_flashes, synchronizing


def testcase():
    layout = open(os.path.join(os.path.dirname(__file__), "day-11-test.txt")).read()
    layout = [list(map(int, list(line))) for line in layout.split('\n')]

    assert both_part(layout) == (1656, 195)


if __name__ == "__main__":
    testcase()

    layout = open(os.path.join(os.path.dirname(__file__), "day-11-input.txt")).read()
    layout = [list(map(int, list(line))) for line in layout.split('\n')]

    print('Part 1: {0}\nPart 2: {1}'.format(*both_part(layout)))
