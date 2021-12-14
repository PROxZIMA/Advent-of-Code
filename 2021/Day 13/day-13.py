import os


def both_part(data):
    dots = set()
    for i in range(len(data)):
        if not data[i]:
            break
        dots.add(tuple(map(int, data[i].split(','))))

    instructions_1 = 0

    for j in range(i + 1, len(data)):
        direction, num = data[j].split('=')
        direction = direction[-1]
        num = int(num)

        new_dots = dots.copy()

        for dot in dots:
            if direction == 'y':
                if dot[1] > num:
                    new_dots.remove(dot)
                    new_dots.add(tuple((dot[0], 2*num - dot[1])))
            else:
                if dot[0] > num:
                    new_dots.remove(dot)
                    new_dots.add(tuple((2*num - dot[0], dot[1])))

        dots = new_dots

        if j == i + 1:
            instructions_1 = len(dots)

    max_x, max_y = max(dots, key=lambda x: int(x[0])), max(dots, key=lambda x: int(x[1]))

    paper = [['.'] * (max_x[0]+1) for i in range((max_y[1]+1))]

    for dot in dots:
        x, y = dot
        paper[y][x] = '#'

    for p in paper:
        print(' '.join(p))

    return (instructions_1, len(dots))


def testcase():
    random_dots = open(os.path.join(os.path.dirname(__file__), "day-13-test.txt")).read()
    random_dots = random_dots.split('\n')

    assert both_part(random_dots) == (17, 16)


if __name__ == "__main__":
    testcase()

    random_dots = open(os.path.join(os.path.dirname(__file__), "day-13-input.txt")).read()
    random_dots = random_dots.split('\n')

    print('Part 1: {0}\nPart 2: {1}'.format(*both_part(random_dots)))