import sys, os, time


def part1(data):
    bit_length = len(data[0])
    gamma_rate = [0] * bit_length
    mask = 0xFF if bit_length < 8 else 0xFFFF

    for binary in data:
        bits = tuple(map(int, binary))
        for i in range(bit_length):
            gamma_rate[i] += 1 if bits[i] else -1

    gamma_rate = "".join(map(lambda x: "1" if x > 0 else "0", gamma_rate))
    gamma_rate = int(gamma_rate, 2)

    epsilon_rate = bin(gamma_rate ^ mask)[-bit_length:]
    epsilon_rate = int(epsilon_rate, 2)

    return gamma_rate * epsilon_rate


def part2(data):
    bit_length = len(data[0])

    oxygen_data = data[:]
    for i in range(bit_length):
        bit_count = 0
        for binary in oxygen_data:
            bit_count += 1 if binary[i] == "1" else -1

        winner_bit = "1" if bit_count >= 0 else "0"

        j = 0
        while len(oxygen_data) > 1 and j < len(oxygen_data):
            if oxygen_data[j][i] != winner_bit:
                del oxygen_data[j]
            else:
                j += 1

    co2_data = data[:]
    for i in range(bit_length):
        bit_count = 0
        for binary in co2_data:
            bit_count += 1 if binary[i] == "1" else -1

        winner_bit = "1" if bit_count < 0 else "0"

        j = 0
        while len(co2_data) > 1 and j < len(co2_data):
            if co2_data[j][i] != winner_bit:
                del co2_data[j]
            else:
                j += 1

    oxygen_generator_rating = int(oxygen_data[0], 2)
    co2_scrubber_rating = int(co2_data[0], 2)

    return oxygen_generator_rating * co2_scrubber_rating


def testcase():
    diagnostic_report = open(
        os.path.join(os.path.dirname(__file__), "day-3-test.txt")
    ).read()
    diagnostic_report = diagnostic_report.split("\n")

    assert part1(diagnostic_report) == 198
    assert part2(diagnostic_report) == 230


if __name__ == "__main__":
    if len(sys.argv) > 1:
        testcase()

    diagnostic_report = open(
        os.path.join(os.path.dirname(__file__), "day-3-input.txt")
    ).read()
    diagnostic_report = diagnostic_report.split("\n")

    s = time.perf_counter()
    print(f"Part 1: {part1(diagnostic_report)}")
    print(f"Part 2: {part2(diagnostic_report)}")
    print(f"> {os.path.basename(__file__)} {round(time.perf_counter() - s, 7)} secs\n")
