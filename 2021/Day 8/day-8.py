import os


def part1(data):
    total = 0
    check_set = {2, 3, 4, 7}

    for instruction in data:
        signal, output = instruction.split(' | ')
        output = output.split(' ')

        for out in output:
            if len(out) in check_set:
                total += 1

    return total


def part2(data):
    total = 0
    check_set = {2: 1, 3: 7, 4: 4, 7: 8}

    for instruction in data:
        signal, output = instruction.split(' | ')
        signal, output = signal.split(' '), output.split(' ')
        seven_bit_set = {}

        for sig in signal:
            seven_bit_set[check_set.get(len(sig), -1)] = set(sig) if len(sig) in check_set else None

        for sig in signal:
            if len(sig) == 6:
                if len(set(sig) - seven_bit_set[1]) == 5:
                    seven_bit_set[6] = set(sig)
                elif len(set(sig) - seven_bit_set[4]) == 2:
                    seven_bit_set[9] = set(sig)
                else:
                    seven_bit_set[0] = set(sig)
            elif len(sig) == 5:
                if len(set(sig) - seven_bit_set[1]) == 3:
                    seven_bit_set[3] = set(sig)
                elif len(set(sig) - seven_bit_set[4]) == 3:
                    seven_bit_set[2] = set(sig)
                else:
                    seven_bit_set[5] = set(sig)

        output_sol = ''
        for out in output:
            if len(out) in check_set:
                output_sol += str(check_set[len(out)])
            else:
                for k, v in seven_bit_set.items():
                    if set(out) == v:
                        output_sol += str(k)
                        break

        total += int(output_sol)

    return total


def testcase():
    signal_output = open(os.path.join(os.path.dirname(__file__), "day-8-test.txt")).read().split('\n')

    assert part1(signal_output) == 26
    assert part2(signal_output) == 61229


if __name__ == "__main__":
    testcase()

    signal_output = open(os.path.join(os.path.dirname(__file__), "day-8-input.txt")).read().split('\n')

    print(f"Part 1: {part1(signal_output)}")
    print(f"Part 2: {part2(signal_output)}")