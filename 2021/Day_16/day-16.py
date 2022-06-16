import sys, os, time
from math import prod


OPERATORS = [
    sum,
    prod,
    min,
    max,
    None,
    lambda x: x[0] > x[1],
    lambda x: x[0] < x[1],
    lambda x: x[0] == x[1],
]


def getVersion(packet, window=0):
    return int(packet[window : window + 3], 2)


def getTypeID(packet, window=0):
    return int(packet[window + 3 : window + 6], 2)


def getLenTypeID(packet, window=0):
    return int(packet[window + 6])


def getLiteralValue(packet, window=0):
    curr = ""
    for i in range(window + 6, len(packet), 5):
        curr += packet[i + 1 : i + 5]
        if packet[i] == "0":
            return int(curr, 2)


def isLiteral(packet, window=0):
    return getTypeID(packet, window) == 4


def getEndOfLiteral(packet, window=0):
    for i in range(window + 6, len(packet), 5):
        if packet[i] == "0":
            return i + 5

    return -1


def helper(packet, window=0):
    versionSum = getVersion(packet, window)

    if isLiteral(packet, window):
        end = getEndOfLiteral(packet, window)
        return end, versionSum, getLiteralValue(packet, window)

    results = []
    initialWindow = window
    end = -1

    if getLenTypeID(packet, window) == 0:
        bitLen15 = int(packet[window + 7 : window + 22], 2)
        window += 22

        while bitLen15 > 0:
            end, version, expression = helper(packet, window)
            results.append(expression)
            versionSum += version
            bitLen15 -= end - window
            window = end

    else:
        bitLen11 = int(packet[window + 7 : window + 18], 2)
        window += 18

        for _ in range(bitLen11):
            end, version, expression = helper(packet, window)
            results.append(expression)
            versionSum += version
            window = end

    return end, versionSum, OPERATORS[getTypeID(packet, initialWindow)](results)


def both_part(data):
    bits = bin(int(data, 16))[2:]
    bits = "0" * (len(data) * 4 - len(bits)) + bits

    end, version, expression = helper(bits)
    return version, expression


def testcase():
    hexadecimal = open(
        os.path.join(os.path.dirname(__file__), "day-16-test.txt")
    ).read()

    assert both_part(hexadecimal) == (16, 15)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        testcase()

    hexadecimal = open(
        os.path.join(os.path.dirname(__file__), "day-16-input.txt")
    ).read()

    s = time.perf_counter()
    print("Part 1: {0}\nPart 2: {1}".format(*both_part(hexadecimal)))
    print(f"> {os.path.basename(__file__)} {round(time.perf_counter() - s, 7)} secs\n")
