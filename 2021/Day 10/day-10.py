import os
from collections import defaultdict


def both_part(data):
    syntax_error_score = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    auto_complete_score = {
        '(': 1,
        '[': 2,
        '{': 3,
        '<': 4
    }
    valid_chunk = {
        '{': '}',
        '(': ')',
        '[': ']',
        '<': '>'
    }
    scores, chunk_count = [], defaultdict(int)

    for chunks in data:
        stack, correct, completion_score = [], True, 0

        for chunk in chunks:
            if chunk in valid_chunk:
                stack.append(chunk)
            elif chunk != valid_chunk[stack.pop()]:
                chunk_count[chunk] += 1
                correct = False
                break

        if correct:
            for chunk in reversed(stack):
                completion_score *= 5
                completion_score += auto_complete_score[chunk]

            scores.append(completion_score)

    for chunk in chunk_count:
        chunk_count[chunk] *= syntax_error_score[chunk]

    return sum(chunk_count.values()), sorted(scores)[len(scores) // 2]


def testcase():
    navigation_subsystem = open(os.path.join(os.path.dirname(__file__), "day-10-test.txt")).read().split('\n')

    assert both_part(navigation_subsystem) == (26397, 288957)


if __name__ == "__main__":
    testcase()

    navigation_subsystem = open(os.path.join(os.path.dirname(__file__), "day-10-input.txt")).read().split('\n')

    print('Part 1: {0}\nPart 2: {1}'.format(*both_part(navigation_subsystem)))