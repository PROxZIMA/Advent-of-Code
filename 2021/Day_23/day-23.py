import os
import sys
import time
from functools import cache

ABCD = ["A", "B", "C", "D"]
A, B, C, D = ABCD

COSTS = {
    A: 1,
    B: 10,
    C: 100,
    D: 1000,
}


DOORS_HALL = {1: 2, 2: 4, 3: 6, 4: 8}

DOORS_LIST = [2, 4, 6, 8]

DOORS = set(DOORS_LIST)

TARGETS = {A: 2, B: 4, C: 6, D: 8}

STATE_ROOM = {A: 1, B: 2, C: 3, D: 4}


def stateTree(state):
    # Move top amphipod
    for i in range(1, 5):
        firstAmp = 0
        try:
            while state[i][firstAmp] is None:
                firstAmp += 1
        except IndexError:
            continue  # Nothing in this room, nothing to do

        newState = list(map(list, state))
        amp = newState[i][firstAmp]

        # If everthing under it is in the right place
        if TARGETS[amp] == DOORS_LIST[i - 1] and all(
            amp == other for other in state[i][firstAmp:]
        ):
            continue  # Don't move it out

        steps = firstAmp
        newState[i][firstAmp] = None
        possibleLocations = []

        for j in range(DOORS_HALL[i]):
            if j not in DOORS:
                possibleLocations.append(j)
            if newState[0][j] is not None:
                possibleLocations.clear()

        for j in range(DOORS_HALL[i], 11):
            if newState[0][j] is not None:
                break
            if j not in DOORS:
                possibleLocations.append(j)

        semiNewState = list(map(tuple, newState))
        hall = state[0]

        for p in possibleLocations:
            newHall = list(hall)
            newHall[p] = amp
            semiNewState[0] = tuple(newHall)
            yield tuple(semiNewState), (
                (1 + steps + abs(p - DOORS_HALL[i])) * COSTS[amp]
            )

    # Move into room
    for i, amp in enumerate(state[0]):
        if amp is None:
            continue

        room = STATE_ROOM[amp]
        roomSet = set(state[room])
        roomSet.discard(None)

        # If the room doesn't contain only its type, don't bother
        # If there is something there and it isn't me
        if roomSet and {amp} != roomSet:
            continue  # Keep out

        if i < TARGETS[amp]:
            sl = slice(i + 1, TARGETS[amp] + 1)
        else:
            sl = slice(TARGETS[amp], i)

        # Is the path to my room clear?
        for t in state[0][sl]:
            if t is not None:  # Curses... foiled again
                break
        else:  # Yep, let's go
            newState = list(map(list, state))
            newState[0][i] = None  # Remove from hall
            roomList = newState[room]

            for firstAmp, val in reversed(list(enumerate(roomList))):
                if val is None:
                    break

            roomList[firstAmp] = amp
            yield tuple(map(tuple, newState)), (
                1 + firstAmp + abs(i - TARGETS[amp])
            ) * COSTS[amp]


@cache
def getMinCost(state, target):
    if state == target:
        return 0
    stateCost = [float("inf")]

    for newState, newCost in stateTree(state):
        stateCost.append(newCost + getMinCost(newState, target))

    return min(stateCost)


def part1(data):
    letters = [c for c in data if c.isalpha()]
    state = ((None,) * 11,) + tuple(
        zip(*(letters[i * 4 : (i + 1) * 4] for i in range(2)))
    )
    target = ((None,) * 11,) + tuple(zip(*((ABCD,) * 2)))

    return getMinCost(state, target)


def part2(data):
    data = data.split("\n")
    data = "\n".join(data[:3] + ["  #D#C#B#A#", "  #D#B#A#C#"] + data[3:])

    letters = [c for c in data if c.isalpha()]
    state = ((None,) * 11,) + tuple(
        zip(*(letters[i * 4 : (i + 1) * 4] for i in range(4)))
    )
    target = ((None,) * 11,) + tuple(zip(*((ABCD,) * 4)))

    return getMinCost(state, target)


def testcase():
    maps = open(os.path.join(os.path.dirname(__file__), "day-23-test.txt")).read()

    assert part1(maps) == 12521
    assert part2(maps) == 44169


if __name__ == "__main__":
    if len(sys.argv) > 1:
        testcase()

    maps = open(os.path.join(os.path.dirname(__file__), "day-23-input.txt")).read()

    s = time.perf_counter()
    print(f"Part 1: {part1(maps)}")
    print(f"Part 2: {part2(maps)}")
    print(f"> {os.path.basename(__file__)} {round(time.perf_counter() - s, 7)} secs\n")
