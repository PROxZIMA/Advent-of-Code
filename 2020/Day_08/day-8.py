import sys, os, time


def part1(data):
    i, accu, path = 0, 0, []

    while i < len(data):
        inst = data[i]
        opt, val = inst[:3], int(inst[4:])

        if i in path:
            return accu
        elif opt == "acc":
            accu += val
            path.append(i)
            i += 1
        elif opt == "jmp":
            path.append(i)
            i += val
        else:
            path.append(i)
            i += 1

    return accu, True


def part2(data):
    for i in range(len(data)):
        inst = data[i]
        opt, val = inst[:3], int(inst[4:])
        copy = data[:]

        if opt == "acc":
            continue
        elif opt == "jmp":
            copy[i] = f"nop {val}"
        else:
            copy[i] = f"jmp {val}"

        ans = part1(copy)
        if isinstance(ans, tuple):
            return ans[0]


def testcase():
    boot_code = open(os.path.join(os.path.dirname(__file__), "day-8-test.txt")).read()
    boot_code = boot_code.split("\n")

    assert part1(boot_code) == 5
    assert part2(boot_code) == 8


if __name__ == "__main__":
    if len(sys.argv) > 1:
        testcase()

    boot_code = open(os.path.join(os.path.dirname(__file__), "day-8-input.txt")).read()
    boot_code = boot_code.split("\n")

    s = time.perf_counter()
    print(f"Part 1: {part1(boot_code)}")
    print(f"Part 2: {part2(boot_code)}")
    print(f"> {os.path.basename(__file__)} {round(time.perf_counter() - s, 7)} secs\n")
