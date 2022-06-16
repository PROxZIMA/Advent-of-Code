import sys, os, time
from math import inf


def calcLocation(matrix: list) -> dict:
    location = {}

    for i in range(5):
        for j in range(5):
            location[matrix[i][j]] = [i + 5, j]

    return location


def part1(data):
    numbers = data[0].split(",")
    min_count = inf
    winPosition = {0: 5, 1: 5, 2: 5, 3: 5, 4: 5, 5: 5, 6: 5, 7: 5, 8: 5, 9: 5}

    for i in range(2, len(data), 6):
        matrix = [x.split() for x in data[i : i + 5]]
        location = calcLocation(matrix)
        bingo = winPosition.copy()
        count = 0

        for num in numbers:
            count += 1
            loc = location.get(num, [])

            if not loc:
                continue

            matrix[loc[0] - 5][loc[1]] = "0"

            for j in loc:
                bingo[j] -= 1

            if 0 in bingo.values() and count < min_count:
                min_count = count
                min_matrix = matrix
                break_point = num
                break

    return int(break_point) * sum(map(int, (j for i in min_matrix for j in i)))


def part2(data):
    numbers = data[0].split(",")
    max_count = -inf
    winPosition = {0: 5, 1: 5, 2: 5, 3: 5, 4: 5, 5: 5, 6: 5, 7: 5, 8: 5, 9: 5}

    for i in range(2, len(data), 6):
        matrix = [x.split() for x in data[i : i + 5]]
        location = calcLocation(matrix)
        bingo = winPosition.copy()
        count = 0

        for num in numbers:
            count += 1
            loc = location.get(num, [])

            if not loc:
                continue

            matrix[loc[0] - 5][loc[1]] = "0"

            for j in loc:
                bingo[j] -= 1

            if 0 in bingo.values():
                if count > max_count:
                    max_count = count
                    max_matrix = matrix
                    break_point = num
                break

    return int(break_point) * sum(map(int, (j for i in max_matrix for j in i)))


def testcase():
    board_input = open(os.path.join(os.path.dirname(__file__), "day-4-test.txt")).read()
    board_input = board_input.split("\n")

    assert part1(board_input) == 4512
    assert part2(board_input) == 1924


if __name__ == "__main__":
    if len(sys.argv) > 1:
        testcase()

    board_input = open(
        os.path.join(os.path.dirname(__file__), "day-4-input.txt")
    ).read()
    board_input = board_input.split("\n")

    s = time.perf_counter()
    print(f"Part 1: {part1(board_input)}")
    print(f"Part 2: {part2(board_input)}")
    print(f"> {os.path.basename(__file__)} {round(time.perf_counter() - s, 7)} secs\n")
