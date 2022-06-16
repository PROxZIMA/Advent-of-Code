import sys, os, time, heapq
from math import inf


def isInsideGrid(x: int, y: int, row: int, col: int) -> bool:
    return 0 <= x < row and 0 <= y < col


def isGoal(x: int, y: int, row: int, col: int) -> bool:
    return x == row - 1 and y == col - 1


def dijkstra(grid: dict, row: int, col: int) -> int:
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    d = [[inf] * col for _ in range(row)]
    Q: list = [(0, 0, 0)]

    while Q:
        dist, x, y = heapq.heappop(Q)

        if not isInsideGrid(x, y, row, col):
            continue

        cost = grid[x][y] + dist

        if d[x][y] <= cost:
            continue
        d[x][y] = cost

        if isGoal(x, y, row, col):
            break

        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            heapq.heappush(Q, (d[x][y], xx, yy))

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
                extended_grid[i][m * len_x + j] = (
                    extended_grid[i][(m - 1) * len_x + j] % 9 + 1
                )

            for n in range(1, extend_param):
                for m in range(extend_param):
                    extended_grid[n * len_y + i][m * len_y + j] = (
                        extended_grid[(n - 1) * len_y + i][m * len_y + j] % 9 + 1
                    )

    p1 = dijkstra(extended_grid, len_x, len_y)
    p2 = dijkstra(extended_grid, len_x * extend_param, len_y * extend_param)

    return p1, p2


def testcase():
    risk_level = open(os.path.join(os.path.dirname(__file__), "day-15-test.txt")).read()
    risk_level = risk_level.split("\n")

    assert both_part(risk_level) == (40, 315)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        testcase()

    risk_level = open(
        os.path.join(os.path.dirname(__file__), "day-15-input.txt")
    ).read()
    risk_level = risk_level.split("\n")

    s = time.perf_counter()
    print("Part 1: {0}\nPart 2: {1}".format(*both_part(risk_level)))
    print(f"> {os.path.basename(__file__)} {round(time.perf_counter() - s, 7)} secs\n")
