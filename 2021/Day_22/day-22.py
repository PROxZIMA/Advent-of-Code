from collections import Counter
import sys, os, time


def both_part(data):
    cubes = Counter()
    within_range = 0

    for step in data:
        state, ranges = step.split(" ")
        x1, x2, y1, y2, z1, z2 = (
            int(num) for rng in ranges.split(",") for num in rng[2:].split("..")
        )

        if not (-50 <= x1 <= 50 or within_range):
            within_range = sum(
                (x2 - x1 + 1) * (y2 - y1 + 1) * (z2 - z1 + 1) * sign
                for (x1, x2, y1, y2, z1, z2), sign in cubes.items()
            )

        new_cubes = Counter()
        for (ex1, ex2, ey1, ey2, ez1, ez2), esign in cubes.items():
            ix1, ix2 = max(x1, ex1), min(x2, ex2)
            iy1, iy2 = max(y1, ey1), min(y2, ey2)
            iz1, iz2 = max(z1, ez1), min(z2, ez2)

            if ix1 <= ix2 and iy1 <= iy2 and iz1 <= iz2:
                new_cubes[(ix1, ix2, iy1, iy2, iz1, iz2)] -= esign

        if state == "on":
            new_cubes[(x1, x2, y1, y2, z1, z2)] += 1

        cubes.update(new_cubes)

    return within_range, sum(
        (x2 - x1 + 1) * (y2 - y1 + 1) * (z2 - z1 + 1) * sign
        for (x1, x2, y1, y2, z1, z2), sign in cubes.items()
    )


def testcase():
    reboot_steps = open(
        os.path.join(os.path.dirname(__file__), "day-22-test.txt")
    ).read()
    reboot_steps = reboot_steps.split("\n")

    assert both_part(reboot_steps) == (474140, 2758514936282235)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        testcase()

    reboot_steps = open(
        os.path.join(os.path.dirname(__file__), "day-22-input.txt")
    ).read()
    reboot_steps = reboot_steps.split("\n")

    s = time.perf_counter()
    print("Part 1: {0}\nPart 2: {1}".format(*both_part(reboot_steps)))
    print(f"> {os.path.basename(__file__)} {round(time.perf_counter() - s, 7)} secs\n")
