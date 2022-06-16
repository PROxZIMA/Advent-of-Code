import functools
import os
import time

boilerplate = """import os
import sys
import time


def part1(data: list[str]):
    pass


def part2(data: list[str]):
    pass


def both_part(data: list[str]):
    pass


def testcase():
    instructions = open(
        os.path.join(os.path.dirname(__file__), "day-{}-test.txt")
    ).read()
    instructions = instructions.split("\\n")

    part1(instructions)
    # assert part1(instructions) ==
    # assert part2(instructions) ==
    # assert both_part(instructions) == (, )


if __name__ == "__main__":
    if len(sys.argv) > 1:
        testcase()

    instructions = open(
        os.path.join(os.path.dirname(__file__), "day-{}-input.txt")
    ).read()
    instructions = instructions.split("\\n")

    s = time.perf_counter()
    # print(f'Part 1: {{part1(instructions)}}')
    # print(f'Part 2: {{part2(instructions)}}')
    # print('Part 1: {{0}}\\nPart 2: {{1}}'.format(*both_part(instructions)))
    print(f"> {{os.path.basename(__file__)}} {{round(time.perf_counter() - s, 7)}} secs")
"""


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        print(
            f"> {os.path.basename(__file__)} {round(time.perf_counter() - start_time, 7)} secs"
        )
        return value

    return wrapper


def main():
    year = "2022"
    os.makedirs(year)
    os.chdir(f"{os.path.dirname(__file__)}/{year}")

    for i in range(1, 26):
        dirs = f"Day_{i:02}"
        os.makedirs(dirs)
        open(f"{dirs}/day-{i}-input.txt", "w").close()
        open(f"{dirs}/day-{i}-test.txt", "w").close()
        open(f"{dirs}/day-{i}.py", "w").write(boilerplate.format(i, i))


if __name__ == "__main__":
    main()
