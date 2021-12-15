import os
from math import inf


class Cell:
    def __init__(self, x, y, d) -> None:
        self.x = x
        self.y = y
        self.d = d

    def __repr__(self) -> str:
        return f'{self.x}_{self.y}_{self.d}'


def isInsideGrid(x: int, y: int, row: int, col: int) -> bool:
    return 0 <= x < row and 0 <= y < col


def dijkstra(grid: dict, row: int, col: int) -> int:
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    d = [[inf] * col for _ in range(row)]
    Q: list[Cell] = []

    d[0][0] = grid[0][0]
    Q.append(Cell(0, 0, 0))

    while len(Q):
        u = min(Q, key=lambda c: c.d)
        Q.remove(u)

        for i in range(4):
            x = u.x + dx[i]
            y = u.y + dy[i]

            if not isInsideGrid(x, y, row, col):
                continue

            if d[x][y] > d[u.x][u.y] + grid[x][y]:

                if d[x][y] != inf:
                    Q.remove(Cell(x, y, d[x][y]))

                d[x][y] = d[u.x][u.y] + grid[x][y]
                Q.append(Cell(x, y, d[x][y]))

    return d[row - 1][col - 1] - d[0][0]


def both_part(data):
    len_x, len_y = len(data[0]), len(data)
    grid = [tuple(map(int, tuple(i))) for i in data]
    extend_param = 5
    extended_grid = [[0] * (len_x * extend_param) for _ in range(len_y * extend_param)]

    for i in range(len_x):
        for j in range(len_y):
            extended_grid[i][j] = grid[i][j]

            for m in range(1, extend_param):
                extended_grid[i][m * len_x + j] = extended_grid[i][(m - 1) * len_x + j] % 9 + 1

            for n in range(1, extend_param):
                for m in range(extend_param):
                    extended_grid[n * len_y + i][m * len_y + j] = extended_grid[(n - 1) * len_y + i][m * len_y + j] % 9 + 1


    p1 = dijkstra(extended_grid, len_x, len_y)
    p2 = dijkstra(extended_grid, len_x * extend_param, len_y * extend_param)

    return p1, p2


def testcase():
    risk_level = open(os.path.join(os.path.dirname(__file__), "day-15-test.txt")).read()
    risk_level = risk_level.split('\n')

    assert both_part(risk_level) == (40, 315)


if __name__ == "__main__":
    testcase()

    risk_level = open(os.path.join(os.path.dirname(__file__), "day-15-input.txt")).read()
    risk_level = risk_level.split('\n')

    print('Part 1: {0}\nPart 2: {1}'.format(*both_part(risk_level)))