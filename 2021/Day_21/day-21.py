from collections import Counter
from functools import lru_cache
import sys, os, time


def part1(data):
    p1Pos = int(data[0].split(" ")[-1])
    p2Pos = int(data[1].split(" ")[-1])
    p1Score = p2Score = dice = 0
    p1Chance = True

    while p1Score < 1000 and p2Score < 1000:
        dice += 3

        if p1Chance:
            p1Pos += 3 * dice - 3
            p1Score += 10 if not (p1Pos % 10) else p1Pos % 10
        else:
            p2Pos += 3 * dice - 3
            p2Score += 10 if not (p2Pos % 10) else p2Pos % 10

        p1Chance = not p1Chance

    return dice * min(p1Score, p2Score)


def part2(data):
    p1Pos = int(data[0].split(" ")[-1])
    p2Pos = int(data[1].split(" ")[-1])

    # This die roll is repeated for every player's turn
    dice_rolls = Counter(
        i + j + k for i in (1, 2, 3) for j in (1, 2, 3) for k in (1, 2, 3)
    )

    @lru_cache(maxsize=None)
    def compute_wins(
        p1Pos: int, p1Score: int, p2Pos: int, p2Score: int
    ) -> tuple[int, int]:

        p1Wins = p2Wins = 0
        for roll, count in dice_rolls.items():
            _p1Pos = 10 if not ((p1Pos + roll) % 10) else (p1Pos + roll) % 10
            _p1Score = p1Score + _p1Pos

            if _p1Score >= 21:
                p1Wins += count
            else:
                _p2Wins, _p1Wins = compute_wins(p2Pos, p2Score, _p1Pos, _p1Score)
                p1Wins += _p1Wins * count
                p2Wins += _p2Wins * count

        return p1Wins, p2Wins

    return max(compute_wins(p1Pos, 0, p2Pos, 0))


def testcase():
    instructions = open(
        os.path.join(os.path.dirname(__file__), "day-21-test.txt")
    ).read()
    instructions = instructions.split("\n")

    assert part1(instructions) == 739785
    assert part2(instructions) == 444356092776315


if __name__ == "__main__":
    if len(sys.argv) > 1:
        testcase()

    instructions = open(
        os.path.join(os.path.dirname(__file__), "day-21-input.txt")
    ).read()
    instructions = instructions.split("\n")

    s = time.perf_counter()
    print(f"Part 1: {part1(instructions)}")
    print(f"Part 2: {part2(instructions)}")
    print(f"> {os.path.basename(__file__)} {round(time.perf_counter() - s, 7)} secs\n")
