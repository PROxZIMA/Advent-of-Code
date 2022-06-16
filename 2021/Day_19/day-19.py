import sys, os, time
from copy import deepcopy
from itertools import combinations
from numpy import array, cross, matmul, ndarray
from math import comb


def rotations():
    """Generate all possible rotation functions"""
    vectors = [
        (1, 0, 0),
        (-1, 0, 0),
        (0, 1, 0),
        (0, -1, 0),
        (0, 0, 1),
        (0, 0, -1),
    ]
    vectors = list(map(array, vectors))
    for vi in vectors:
        for vj in vectors:
            if vi.dot(vj) == 0:
                vk = cross(vi, vj)
                yield lambda x: matmul(x, array([vi, vj, vk]))


def fit(scanners, hashes, i, j, v):
    """Find the correct rotation/translation to make the jth scanner map fit the ith"""
    s1, s2 = scanners[i], scanners[j]
    for rot in rotations():
        s2t = rot(s2)
        p = hashes[i][v][0]
        for q in hashes[j][v]:
            diff = s1[p, :] - s2t[q, :]
            if len((b := set(map(tuple, s2t + diff))) & set(map(tuple, s1))) >= 12:
                return diff, b, rot


def map_hash(coords) -> dict:
    """
    Generate a hashset of sorted absolute coordinate differences
    between pairs of points
    """
    return {
        tuple(sorted(map(abs, coords[i, :] - coords[j, :]))): (i, j)
        for i, j in combinations(range(len(coords)), 2)
    }


def match(hashes):
    """Figure out which pairs of scanner aps have sufficient overlap"""
    for i, j in combinations(range(len(hashes)), 2):
        if len(m := set(hashes[i]) & set(hashes[j])) >= comb(12, 2):
            yield i, j, next(iter(m))


def both_part(scanners: list[ndarray]):
    """Given a list of scanner maps, return beacons set length and Manhattan distance between scanners"""
    scanners = deepcopy(scanners)
    positions = {0: (0, 0, 0)}
    hashes = list(map(map_hash, scanners))
    beacons = set(map(tuple, scanners[0]))
    while len(positions) < len(scanners):
        for i, j, v in match(hashes):
            if not (i in positions) ^ (j in positions):
                continue
            elif j in positions:
                i, j = j, i
            positions[j], new_beacons, rot = fit(scanners, hashes, i, j, v)
            scanners[j] = rot(scanners[j]) + positions[j]
            beacons |= new_beacons
    positions = [positions[i] for i in range(len(scanners))]

    return len(beacons), max(abs(x - y).sum() for x, y in combinations(positions, 2))


def testcase():
    coordinates = (
        open(os.path.join(os.path.dirname(__file__), "day-19-test.txt"))
        .read()
        .split("\n\n")
    )
    coordinates = [x.split("---\n")[-1].split("\n") for x in coordinates]
    coordinates = [
        array([tuple(map(int, y.split(","))) for y in x]) for x in coordinates
    ]

    assert both_part(coordinates) == (79, 3621)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        testcase()

    coordinates = (
        open(os.path.join(os.path.dirname(__file__), "day-19-input.txt"))
        .read()
        .split("\n\n")
    )
    coordinates = [x.split("---\n")[-1].split("\n") for x in coordinates]
    coordinates = [
        array([tuple(map(int, y.split(","))) for y in x]) for x in coordinates
    ]

    s = time.perf_counter()
    print("Part 1: {0}\nPart 2: {1}".format(*both_part(coordinates)))
    print(f"> {os.path.basename(__file__)} {round(time.perf_counter() - s, 7)} secs\n")
