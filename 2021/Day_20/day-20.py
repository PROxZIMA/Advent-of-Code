import sys, os, time


def isInGrid(i, j, rMin, rMax, cMin, cMax):
    return rMin <= i and i <= rMax and cMin <= j and j <= cMax


def getPixels(lightSet, i, j, rMin, rMax, cMin, cMax, bg):
    # Faster that pixels = 0; bit = 8; pixels += 1|0 << bit; bit -= 1
    pixels = ""
    for x in [i - 1, i, i + 1]:
        for y in [j - 1, j, j + 1]:
            pixels += (
                "1"
                if (x, y) in lightSet
                else "0"
                if isInGrid(x, y, rMin, rMax, cMin, cMax)
                else bg
            )
    return int(pixels, 2)


def extend(iea, lightSet, bg):
    newLightSet = set()
    rMin = min(r for r, _ in lightSet)
    rMax = max(r for r, _ in lightSet)
    cMin = min(c for _, c in lightSet)
    cMax = max(c for _, c in lightSet)

    for i in range(rMin - 1, rMax + 2):
        for j in range(cMin - 1, cMax + 2):
            if iea[getPixels(lightSet, i, j, rMin, rMax, cMin, cMax, bg)] == "#":
                newLightSet.add((i, j))

    return newLightSet


def both_part(iea, image):
    lightSet = set(
        (
            (x, y)
            for x, line in enumerate(image.split("\n"))
            for y, char in enumerate(line)
            if char == "#"
        )
    )
    lightSet_2 = 0
    for i in range(50):
        lightSet = extend(iea, lightSet, "1" if iea[0] == "#" and i % 2 != 0 else "0")
        if i == 1:
            lightSet_2 = len(lightSet)

    return lightSet_2, len(lightSet)


def testcase():
    ieaImage = open(os.path.join(os.path.dirname(__file__), "day-20-test.txt")).read()
    iea, image = ieaImage.split("\n\n")

    assert both_part(iea, image) == (35, 3351)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        testcase()

    ieaImage = open(os.path.join(os.path.dirname(__file__), "day-20-input.txt")).read()
    iea, image = ieaImage.split("\n\n")

    s = time.perf_counter()
    print("Part 1: {0}\nPart 2: {1}".format(*both_part(iea, image)))
    print(f"> {os.path.basename(__file__)} {round(time.perf_counter() - s, 7)} secs\n")
